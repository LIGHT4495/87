(function () {
  'use strict';

  var PHOTO = '사진', DATE = '날짜';
  var MAX_SIDE = 1600;           // 사진 긴 변 최대 픽셀 (한글 파일 크기를 줄이기 위함)
  var $ = function (id) { return document.getElementById(id); };

  var state = {
    tpl: null,          // { name, buf(ArrayBuffer), tokens[], isSample }
    items: [],          // [{ id, values:{}, photo:{data,width,height,ext,url}|null, dateTouched }]
    nextId: 1
  };

  /* ---------- 저장(IndexedDB, 이 기기에만) ---------- */
  var DB = {
    open: function () {
      return new Promise(function (res, rej) {
        if (!window.indexedDB) return rej(new Error('no idb'));
        var r = indexedDB.open('jeungbing-photo', 1);
        r.onupgradeneeded = function () { r.result.createObjectStore('kv'); };
        r.onsuccess = function () { res(r.result); };
        r.onerror = function () { rej(r.error); };
      });
    },
    get: function (k) {
      return DB.open().then(function (db) {
        return new Promise(function (res, rej) {
          var q = db.transaction('kv').objectStore('kv').get(k);
          q.onsuccess = function () { res(q.result); };
          q.onerror = function () { rej(q.error); };
        });
      }).catch(function () { return undefined; });
    },
    set: function (k, v) {
      return DB.open().then(function (db) {
        return new Promise(function (res, rej) {
          var tx = db.transaction('kv', 'readwrite');
          tx.objectStore('kv').put(v, k);
          tx.oncomplete = res; tx.onerror = function () { rej(tx.error); };
        });
      }).catch(function () { /* 저장 못 해도 사용은 가능 */ });
    },
    del: function (k) {
      return DB.open().then(function (db) {
        return new Promise(function (res) {
          var tx = db.transaction('kv', 'readwrite');
          tx.objectStore('kv').delete(k);
          tx.oncomplete = res; tx.onerror = res;
        });
      }).catch(function () {});
    }
  };

  /* ---------- 작은 도우미 ---------- */
  function h(tag, attrs) {
    var el = document.createElement(tag);
    Object.keys(attrs || {}).forEach(function (k) {
      if (k === 'text') el.textContent = attrs[k];
      else if (k.slice(0, 2) === 'on') el.addEventListener(k.slice(2), attrs[k]);
      else if (attrs[k] === true) el.setAttribute(k, '');
      else if (attrs[k] !== false && attrs[k] != null) el.setAttribute(k, attrs[k]);
    });
    for (var i = 2; i < arguments.length; i++) {
      var c = arguments[i];
      if (c != null) el.appendChild(typeof c === 'string' ? document.createTextNode(c) : c);
    }
    return el;
  }
  function setStatus(msg, kind) {
    var s = $('status');
    s.textContent = msg || '';
    s.className = 'status' + (kind ? ' ' + kind : '');
  }
  function fmtToday(d) { return Hwpx.formatDate(d.getFullYear(), d.getMonth() + 1, d.getDate()); }
  function commas(s) {
    var d = String(s).replace(/[^\d]/g, '');
    return d.replace(/\B(?=(\d{3})+(?!\d))/g, ',');
  }
  function baseName(n) { return String(n || '양식').replace(/\.[^.]+$/, ''); }
  function download(bytes, filename) {
    var blob = new Blob([bytes], { type: 'application/hwp+zip' });
    var a = h('a', { href: URL.createObjectURL(blob), download: filename });
    document.body.appendChild(a); a.click();
    setTimeout(function () { URL.revokeObjectURL(a.href); a.remove(); }, 4000);
    return blob;
  }

  /* ---------- 양식 ---------- */
  async function loadTemplate(buf, name, isSample, persist) {
    var info = await Hwpx.inspectTemplate(buf);
    if (!info.tokens.length) {
      var e = new Error('양식에서 {사진}·{날짜} 같은 중괄호 표시를 찾지 못했어요. 한글에서 칸에 표시를 적고 HWPX로 다시 저장해 주세요.');
      e.code = 'NO_TOKENS';
      throw e;
    }
    state.tpl = { name: name, buf: buf, tokens: info.tokens, isSample: !!isSample };
    if (persist) await DB.set('template', { name: name, buf: buf });
    renderTemplate();
    renderItems();
  }

  async function useSample() {
    var bytes = await Hwpx.buildSampleTemplate();
    await loadTemplate(bytes.buffer.slice(bytes.byteOffset, bytes.byteOffset + bytes.byteLength), '물품 구입 증빙 사진 양식.hwpx', true, false);
  }

  function showTplError(msg) {
    var el = $('tplError');
    el.textContent = msg || '';
    el.hidden = !msg;
  }

  async function onTemplateFile(file) {
    showTplError('');
    if (!file) return;
    if (/\.hwp$/i.test(file.name)) {
      return showTplError('HWP 파일은 안 돼요. 한글에서 "파일 → 다른 이름으로 저장 → HWPX"로 저장한 뒤 올려 주세요.');
    }
    if (!/\.hwpx$/i.test(file.name)) {
      return showTplError('HWPX 파일(.hwpx)만 올릴 수 있어요.');
    }
    try {
      var buf = await file.arrayBuffer();
      await loadTemplate(buf, file.name, false, true);
      setStatus('양식을 기억해 뒀어요. 다음부터는 바로 사진만 찍으면 돼요.', 'ok');
    } catch (e) {
      showTplError(e.message || '양식을 읽지 못했어요.');
    }
  }

  function renderTemplate() {
    var t = state.tpl;
    $('tplBadge').textContent = t.isSample ? '예시 양식 사용 중' : '내 양식: ' + t.name;
    $('resetTpl').hidden = t.isSample;
    var chips = $('chips');
    chips.textContent = '';
    t.tokens.forEach(function (k) {
      chips.appendChild(h('span', { class: 'chip' + (k === PHOTO ? ' photo' : ''), text: '{' + k + '}' }));
    });
  }

  /* ---------- 사진 처리 ---------- */
  async function decodeToJpeg(file) {
    var bmp = null, w, h2;
    if (window.createImageBitmap) {
      try { bmp = await createImageBitmap(file); } catch (e) { bmp = null; }
    }
    var src;
    if (bmp) { src = bmp; w = bmp.width; h2 = bmp.height; }
    else {
      src = await new Promise(function (res, rej) {
        var url = URL.createObjectURL(file), img = new Image();
        img.onload = function () { URL.revokeObjectURL(url); res(img); };
        img.onerror = function () { URL.revokeObjectURL(url); rej(new Error('decode')); };
        img.src = url;
      });
      w = src.naturalWidth; h2 = src.naturalHeight;
    }
    var scale = Math.min(1, MAX_SIDE / Math.max(w, h2));
    var cw = Math.max(1, Math.round(w * scale)), ch = Math.max(1, Math.round(h2 * scale));
    var cv = document.createElement('canvas');
    cv.width = cw; cv.height = ch;
    var ctx = cv.getContext('2d');
    ctx.fillStyle = '#fff'; ctx.fillRect(0, 0, cw, ch);
    ctx.drawImage(src, 0, 0, cw, ch);
    if (bmp && bmp.close) bmp.close();
    var blob = await new Promise(function (res) { cv.toBlob(res, 'image/jpeg', 0.85); });
    if (!blob) throw new Error('encode');
    return { data: new Uint8Array(await blob.arrayBuffer()), width: cw, height: ch, ext: 'jpg', blob: blob };
  }

  async function onPhoto(item, file) {
    if (!file) return;
    setStatus('사진을 불러오는 중…');
    try {
      var exifDate = Hwpx.parseExifDate(await file.slice(0, 262144).arrayBuffer());
      var p = await decodeToJpeg(file);
      if (item.photo && item.photo.url) URL.revokeObjectURL(item.photo.url);
      p.url = URL.createObjectURL(p.blob);
      item.photo = p;
      if (!item.dateTouched) {
        item.values[DATE] = exifDate || fmtToday(file.lastModified ? new Date(file.lastModified) : new Date());
      }
      renderItems();
      setStatus('');
    } catch (e) {
      setStatus('이 사진은 읽을 수 없어요. 아이폰이라면 카메라 설정에서 "높은 호환성"으로 찍어 주세요.', 'err');
    }
  }

  /* ---------- 칸 채우기 화면 ---------- */
  function newItem() {
    return { id: state.nextId++, values: {}, photo: null, dateTouched: false };
  }

  var CAM_SVG = '<svg viewBox="0 0 24 24" width="30" height="30" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 8h3l1.5-2h7L17 8h3a1 1 0 0 1 1 1v9a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V9a1 1 0 0 1 1-1z"/><circle cx="12" cy="13" r="3.5"/></svg>';

  function fileInput(onFile, capture) {
    var inp = h('input', { type: 'file', accept: 'image/*', hidden: true });
    if (capture) inp.setAttribute('capture', 'environment');
    inp.addEventListener('change', function () {
      var f = inp.files && inp.files[0];
      inp.value = '';
      onFile(f);
    });
    return inp;
  }

  function photoArea(item) {
    var cam = fileInput(function (f) { onPhoto(item, f); }, true);
    var pick = fileInput(function (f) { onPhoto(item, f); }, false);
    var box = h('div', { class: 'shot' + (item.photo ? ' filled' : '') }, h('span', { class: 'tag', text: '사진' }), cam, pick);
    if (item.photo) {
      box.appendChild(h('div', {},
        h('img', { src: item.photo.url, alt: '찍은 사진 미리보기' }),
        h('div', { class: 'row' },
          h('button', { type: 'button', class: 'btn ghost', text: '다시 찍기', onclick: function () { cam.click(); } }),
          h('button', { type: 'button', class: 'btn ghost', text: '다른 사진 고르기', onclick: function () { pick.click(); } }))));
    } else {
      var camBtn = h('button', { type: 'button', class: 'cam', 'aria-label': '눌러서 사진 찍기', onclick: function () { cam.click(); } });
      camBtn.innerHTML = CAM_SVG;
      box.appendChild(h('div', {}, camBtn, h('strong', { text: '눌러서 찍기' }),
        h('button', { type: 'button', class: 'alt', text: '또는 사진 고르기', onclick: function () { pick.click(); } })));
    }
    return box;
  }

  function fieldFor(item, key) {
    var id = 'f' + item.id + '-' + key;
    var money = key === '금액', num = key === '수량';
    var ph = key === DATE ? (state.tpl.tokens.indexOf(PHOTO) >= 0 ? '사진에서 자동' : '예) ' + fmtToday(new Date())) : '';
    var inp = h('input', {
      id: id, type: 'text', value: item.values[key] || '', placeholder: ph, autocomplete: 'off',
      inputmode: money || num ? 'numeric' : 'text', enterkeyhint: 'next'
    });
    inp.addEventListener('input', function () {
      if (money) inp.value = commas(inp.value);
      item.values[key] = inp.value;
      if (key === DATE) item.dateTouched = inp.value !== '';
    });
    return h('div', { class: 'field' }, h('label', { for: id, text: key }), inp);
  }

  function renderItems() {
    var box = $('items');
    box.textContent = '';
    var hasPhoto = state.tpl.tokens.indexOf(PHOTO) >= 0;
    var keys = state.tpl.tokens.filter(function (k) { return k !== PHOTO; });
    state.items.forEach(function (item, idx) {
      var head = h('div', { class: 'item-head' }, h('h3', { text: (idx + 1) + '번째 장' }));
      if (state.items.length > 1) {
        head.appendChild(h('button', {
          type: 'button', class: 'rm', text: '이 장 지우기',
          onclick: function () {
            if (item.photo && item.photo.url) URL.revokeObjectURL(item.photo.url);
            state.items = state.items.filter(function (x) { return x !== item; });
            renderItems();
          }
        }));
      }
      var el = h('div', { class: 'item' }, head);
      if (hasPhoto) el.appendChild(photoArea(item));
      keys.forEach(function (k) { el.appendChild(fieldFor(item, k)); });
      box.appendChild(el);
    });
    $('count').textContent = '지금 ' + state.items.length + '장';
  }

  /* ---------- 한글 파일 만들기 ---------- */
  var lastBlob = null, lastName = '';

  async function make() {
    var t = state.tpl;
    var hasPhoto = t.tokens.indexOf(PHOTO) >= 0;
    var used = state.items.filter(function (it) {
      return it.photo || Object.keys(it.values).some(function (k) { return it.values[k]; });
    });
    if (!used.length) return setStatus('사진을 찍거나 칸을 채워 주세요.', 'err');
    if (hasPhoto && used.some(function (it) { return !it.photo; }) &&
        !window.confirm('사진이 없는 장이 있어요. 그 장은 사진 칸을 비워 둘까요?')) return;

    var btn = $('makeBtn');
    btn.disabled = true; setStatus('한글 파일을 만드는 중…');
    try {
      var bytes = await Hwpx.fillTemplate(t.buf, used.map(function (it) {
        return { values: it.values, photo: it.photo ? { data: it.photo.data, width: it.photo.width, height: it.photo.height, ext: it.photo.ext } : null };
      }));
      lastName = baseName(t.name).replace(/\s*양식$/, '') + '_' + Hwpx.formatDate.apply(null, [new Date().getFullYear(), new Date().getMonth() + 1, new Date().getDate()]).replace(/[^\d]/g, '') + '.hwpx';
      lastBlob = download(bytes, lastName);
      setStatus('만들어졌어요! (' + used.length + '장) 카카오톡 \'나와의 채팅\' 등으로 컴퓨터에 옮겨 한글에서 여세요.', 'ok');
      var canShare = false;
      try { canShare = !!(navigator.canShare && navigator.canShare({ files: [new File([lastBlob], lastName, { type: lastBlob.type })] })); } catch (e) {}
      $('shareBtn').hidden = !canShare;
    } catch (e) {
      setStatus('파일을 만들지 못했어요: ' + (e.message || e), 'err');
    } finally {
      btn.disabled = false;
    }
  }

  async function share() {
    if (!lastBlob) return;
    try {
      await navigator.share({ files: [new File([lastBlob], lastName, { type: lastBlob.type })], title: lastName });
    } catch (e) { /* 사용자가 취소 */ }
  }

  /* ---------- 시작 ---------- */
  function wire() {
    $('sampleBtn').addEventListener('click', async function () {
      var bytes = await Hwpx.buildSampleTemplate();
      download(bytes, '증빙사진_예시양식.hwpx');
    });
    $('tplInput').addEventListener('change', function (e) { onTemplateFile(e.target.files[0]); e.target.value = ''; });
    var drop = $('drop');
    ['dragenter', 'dragover'].forEach(function (ev) {
      drop.addEventListener(ev, function (e) { e.preventDefault(); drop.classList.add('over'); });
    });
    ['dragleave', 'drop'].forEach(function (ev) {
      drop.addEventListener(ev, function (e) { e.preventDefault(); drop.classList.remove('over'); });
    });
    drop.addEventListener('drop', function (e) { onTemplateFile(e.dataTransfer.files[0]); });
    drop.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); $('tplInput').click(); } });
    $('resetTpl').addEventListener('click', async function () {
      await DB.del('template'); showTplError(''); await useSample();
    });
    $('addBtn').addEventListener('click', function () {
      state.items.push(newItem()); renderItems();
      var cards = $('items').children; cards[cards.length - 1].scrollIntoView({ behavior: 'smooth', block: 'start' });
    });
    $('makeBtn').addEventListener('click', make);
    $('shareBtn').addEventListener('click', share);
  }

  async function init() {
    wire();
    state.items = [newItem()];
    var saved = await DB.get('template');
    try {
      if (saved && saved.buf) await loadTemplate(saved.buf, saved.name, false, false);
      else await useSample();
    } catch (e) {
      await useSample();
    }
  }
  init();
})();
