/*
 * hwpx.js — HWPX 양식에서 {표시}를 찾아 글자·사진으로 채우는 모듈 (브라우저/Node 공용)
 *
 * HWPX = ZIP 안에 XML(Contents/section0.xml 등)이 들어 있는 한글 문서 형식.
 *  - {사진}  : 사진을 BinData/ 에 넣고 <hp:pic> 로 삽입 (셀 크기에 맞춰 비율 유지)
 *  - 그 외 {이름} : 입력한 글자로 치환
 *  - 물품이 여러 개면 양식(본문 전체)을 복제해 쪽 나눔으로 이어 붙임
 *
 * 외부 의존: JSZip, DOMParser/XMLSerializer (Node 에서는 @xmldom/xmldom 을 전역에 주입)
 */
(function (root) {
  'use strict';

  var NS = {
    hp: 'http://www.hancom.co.kr/hwpml/2011/paragraph',
    hc: 'http://www.hancom.co.kr/hwpml/2011/core',
    opf: 'http://www.idpf.org/2007/opf/'
  };
  var XML_DECL = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n';
  var TOKEN_SRC = '\\{([^{}]+)\\}';
  var PHOTO = '사진';

  var getJSZip = function () {
    return root.JSZip || (typeof require === 'function' ? require('jszip') : null);
  };

  /* ---------- XML 보조 ---------- */
  function parseXml(str) {
    return new root.DOMParser().parseFromString(str, 'text/xml');
  }
  function serializeXml(doc) {
    return XML_DECL + new root.XMLSerializer().serializeToString(doc);
  }
  function elChildren(node) {
    var out = [];
    for (var c = node.firstChild; c; c = c.nextSibling) if (c.nodeType === 1) out.push(c);
    return out;
  }
  function byTag(node, name) {
    return Array.prototype.slice.call(node.getElementsByTagName(name));
  }
  function textOf(el) {
    var s = '';
    for (var c = el.firstChild; c; c = c.nextSibling) if (c.nodeType === 3 || c.nodeType === 4) s += c.nodeValue;
    return s;
  }
  function onlyText(el) {
    for (var c = el.firstChild; c; c = c.nextSibling) if (c.nodeType === 1) return false;
    return true;
  }
  function setText(el, s) {
    while (el.firstChild) el.removeChild(el.firstChild);
    if (s) el.appendChild(el.ownerDocument.createTextNode(s));
  }
  function ancestor(node, name) {
    for (var p = node.parentNode; p; p = p.parentNode) if (p.nodeName === name) return p;
    return null;
  }
  function attrNum(el, name, dflt) {
    var v = el && el.getAttribute(name);
    var n = v == null || v === '' ? NaN : Number(v);
    return isNaN(n) ? dflt : n;
  }

  /* 문단(hp:p)의 직속 run 안에 있는 단순 글자(hp:t) 목록 */
  function plainTexts(p) {
    var out = [];
    elChildren(p).forEach(function (run) {
      if (run.nodeName !== 'hp:run') return;
      elChildren(run).forEach(function (c) {
        if (c.nodeName === 'hp:t' && onlyText(c)) out.push(c);
      });
    });
    return out;
  }

  /* 한 문단 안의 토큰이 서로 다른 글자 조각(run)에 쪼개져 있으면 첫 조각으로 합침 */
  function mergeSplitTokens(ts) {
    var joined = ts.map(textOf).join('');
    var total = (joined.match(new RegExp(TOKEN_SRC, 'g')) || []).length;
    if (!total) return;
    var each = 0;
    ts.forEach(function (t) {
      each += (textOf(t).match(new RegExp(TOKEN_SRC, 'g')) || []).length;
    });
    if (each === total) return;
    setText(ts[0], joined);
    for (var i = 1; i < ts.length; i++) setText(ts[i], '');
  }

  function allParagraphs(roots) {
    var out = [];
    roots.forEach(function (r) {
      if (r.nodeName === 'hp:p') out.push(r);
      byTag(r, 'hp:p').forEach(function (p) { out.push(p); });
    });
    return out;
  }

  /* ---------- 양식 분석 ---------- */
  function sectionPaths(zip) {
    return Object.keys(zip.files)
      .filter(function (n) { return /^Contents\/section\d+\.xml$/.test(n); })
      .sort(function (a, b) { return parseInt(a.match(/\d+/)[0], 10) - parseInt(b.match(/\d+/)[0], 10); });
  }

  function findTokens(doc) {
    var names = [];
    allParagraphs([doc.documentElement]).forEach(function (p) {
      var joined = plainTexts(p).map(textOf).join('');
      var re = new RegExp(TOKEN_SRC, 'g'), m;
      while ((m = re.exec(joined))) {
        var name = m[1].trim();
        if (name && names.indexOf(name) < 0) names.push(name);
      }
    });
    return names;
  }

  async function openZip(buf) {
    var JSZip = getJSZip();
    try {
      return await JSZip.loadAsync(buf);
    } catch (e) {
      var err = new Error('HWPX 파일이 아니에요. (한글에서 "다른 이름으로 저장 → HWPX"로 저장해 주세요)');
      err.code = 'NOT_ZIP';
      throw err;
    }
  }

  /** 양식 안의 {표시} 목록(나온 순서)과 섹션 정보를 돌려줌 */
  async function inspectTemplate(buf) {
    var zip = await openZip(buf);
    var secs = sectionPaths(zip);
    if (!secs.length) {
      var err = new Error('HWPX 양식이 아니에요. (Contents/section0.xml 없음)');
      err.code = 'NOT_HWPX';
      throw err;
    }
    var tokens = [], target = null;
    for (var i = 0; i < secs.length; i++) {
      var doc = parseXml(await zip.file(secs[i]).async('string'));
      findTokens(doc).forEach(function (t) { if (tokens.indexOf(t) < 0) tokens.push(t); });
      if (target === null && findTokens(doc).length) target = secs[i];
    }
    return { tokens: tokens, sectionPath: target, hasPhoto: tokens.indexOf(PHOTO) >= 0 };
  }

  /* ---------- 사진 삽입 ---------- */
  function picBox(p) {
    var tc = ancestor(p, 'hp:tc');
    if (tc) {
      var sz = byTag(tc, 'hp:cellSz')[0];
      var mg = byTag(tc, 'hp:cellMargin')[0];
      if (sz) {
        var w = attrNum(sz, 'width', 0) - attrNum(mg, 'left', 510) - attrNum(mg, 'right', 510);
        var h = attrNum(sz, 'height', 0) - attrNum(mg, 'top', 141) - attrNum(mg, 'bottom', 141);
        if (w > 1500) {
          // 키가 작은 칸(보통 글자 칸)이면 폭에 맞추고 칸이 늘어나게 둠
          if (h < 8000) h = 30000;
          return { w: w - 200, h: h - 200 };
        }
      }
    }
    return { w: 36000, h: 27000 };
  }

  function makePic(doc, ctx, photo, box) {
    var ratio = photo.width / photo.height;
    var W, H;
    if (box.w / box.h > ratio) { H = box.h; W = H * ratio; } else { W = box.w; H = W / ratio; }
    W = Math.max(1, Math.floor(W)); H = Math.max(1, Math.floor(H));
    var id = String(ctx.nextId++);
    var xml =
      '<hp:pic xmlns:hp="' + NS.hp + '" xmlns:hc="' + NS.hc + '" id="' + id + '" zOrder="' + ctx.z++ + '" numberingType="PICTURE" textWrap="TOP_AND_BOTTOM" textFlow="BOTH_SIDES" lock="0" dropcapstyle="None" href="" groupLevel="0" instid="' + id + '" reverse="0">' +
      '<hp:offset x="0" y="0"/>' +
      '<hp:orgSz width="' + W + '" height="' + H + '"/>' +
      '<hp:curSz width="' + W + '" height="' + H + '"/>' +
      '<hp:flip horizontal="0" vertical="0"/>' +
      '<hp:rotationInfo angle="0" centerX="' + Math.floor(W / 2) + '" centerY="' + Math.floor(H / 2) + '" rotateimage="1"/>' +
      '<hp:renderingInfo>' +
      '<hc:transMatrix e1="1" e2="0" e3="0" e4="0" e5="1" e6="0"/>' +
      '<hc:scaMatrix e1="1" e2="0" e3="0" e4="0" e5="1" e6="0"/>' +
      '<hc:rotMatrix e1="1" e2="0" e3="0" e4="0" e5="1" e6="0"/>' +
      '</hp:renderingInfo>' +
      '<hc:img binaryItemIDRef="' + photo.binId + '" bright="0" contrast="0" effect="REAL_PIC" alpha="0"/>' +
      '<hp:imgRect><hc:pt0 x="0" y="0"/><hc:pt1 x="' + W + '" y="0"/><hc:pt2 x="' + W + '" y="' + H + '"/><hc:pt3 x="0" y="' + H + '"/></hp:imgRect>' +
      '<hp:imgClip left="0" right="' + W + '" top="0" bottom="' + H + '"/>' +
      '<hp:inMargin left="0" right="0" top="0" bottom="0"/>' +
      '<hp:imgDim dimwidth="' + W + '" dimheight="' + H + '"/>' +
      '<hp:effects/>' +
      '<hp:sz width="' + W + '" widthRelTo="ABSOLUTE" height="' + H + '" heightRelTo="ABSOLUTE" protect="0"/>' +
      '<hp:pos treatAsChar="1" affectLSpacing="0" flowWithText="1" allowOverlap="0" holdAnchorAndSO="0" vertRelTo="PARA" horzRelTo="PARA" vertAlign="TOP" horzAlign="LEFT" vertOffset="0" horzOffset="0"/>' +
      '<hp:outMargin left="0" right="0" top="0" bottom="0"/>' +
      '</hp:pic>';
    var frag = parseXml(xml).documentElement;
    return doc.importNode(frag, true);
  }

  /* ---------- 문단 치환 ---------- */
  function fillParagraph(doc, p, item, ctx) {
    var ts = plainTexts(p);
    if (!ts.length) return false;
    mergeSplitTokens(ts);
    var changed = false;

    ts.forEach(function (t) {
      var text = textOf(t);
      if (!new RegExp(TOKEN_SRC).test(text)) return;
      changed = true;

      // 글자/토큰 조각으로 나눔
      var segs = [], last = 0, re = new RegExp(TOKEN_SRC, 'g'), m;
      while ((m = re.exec(text))) {
        if (m.index > last) segs.push({ text: text.slice(last, m.index) });
        segs.push({ token: m[1].trim() });
        last = re.lastIndex;
      }
      if (last < text.length) segs.push({ text: text.slice(last) });

      var hasPhotoSeg = segs.some(function (s) { return s.token === PHOTO && item.photo; });
      if (!hasPhotoSeg) {
        setText(t, segs.map(function (s) {
          if (s.text != null) return s.text;
          if (s.token === PHOTO) return '';
          var v = item.values[s.token];
          return v == null ? '' : String(v);
        }).join(''));
        return;
      }

      // 사진이 들어가면 run 을 쪼개 [앞글자][사진][뒷글자] 로 만듦
      var run = t.parentNode;
      var anchor = run;
      var box = picBox(p);
      segs.forEach(function (s) {
        var nr = run.cloneNode(false);
        if (s.token === PHOTO) {
          nr.appendChild(makePic(doc, ctx, item.photo, box));
        } else {
          var nt = t.cloneNode(false);
          var str = s.text != null ? s.text : (item.values[s.token] == null ? '' : String(item.values[s.token]));
          if (!str) return;
          nt.appendChild(doc.createTextNode(str));
          nr.appendChild(nt);
        }
        run.parentNode.insertBefore(nr, anchor.nextSibling);
        anchor = nr;
      });
      run.removeChild(t);
      if (!elChildren(run).length) run.parentNode.removeChild(run);
    });

    if (changed) {
      elChildren(p).forEach(function (c) { if (c.nodeName === 'hp:linesegarray') p.removeChild(c); });
    }
    return changed;
  }

  function stripSectionHeader(node) {
    // 두 번째 장부터는 쪽 설정(secPr)·단 설정(colPr)이 또 들어가면 안 됨
    byTag(node, 'hp:secPr').forEach(function (e) { e.parentNode.removeChild(e); });
    byTag(node, 'hp:ctrl').forEach(function (ctrl) {
      if (byTag(ctrl, 'hp:colPr').length && ctrl.parentNode) ctrl.parentNode.removeChild(ctrl);
    });
    byTag(node, 'hp:run').forEach(function (r) {
      if (!elChildren(r).length && r.parentNode) r.parentNode.removeChild(r);
    });
  }

  /* ---------- BinData / manifest ---------- */
  function nextImageNumber(zip, hpfDoc) {
    var max = 0;
    Object.keys(zip.files).forEach(function (n) {
      var m = n.match(/^BinData\/image(\d+)\./);
      if (m) max = Math.max(max, parseInt(m[1], 10));
    });
    if (hpfDoc) {
      byTag(hpfDoc, 'opf:item').forEach(function (it) {
        var m = (it.getAttribute('id') || '').match(/^image(\d+)$/);
        if (m) max = Math.max(max, parseInt(m[1], 10));
      });
    }
    return max + 1;
  }

  /**
   * 양식에 값을 채워 새 HWPX 를 만든다.
   * @param {ArrayBuffer|Uint8Array} templateBuf  기관 양식(.hwpx)
   * @param {Array} items  [{ values:{품목,날짜,수량,금액,...}, photo:{data:Uint8Array,width,height,ext:'jpg'|'png'} }]
   * @returns {Promise<Uint8Array>}
   */
  async function fillTemplate(templateBuf, items) {
    if (!items || !items.length) throw new Error('채울 물품이 없어요.');
    var zip = await openZip(templateBuf);
    var info = await inspectTemplate(templateBuf);
    if (!info.sectionPath) {
      var err = new Error('양식에서 {사진}·{날짜} 같은 표시를 찾지 못했어요.');
      err.code = 'NO_TOKENS';
      throw err;
    }

    // content.hpf (manifest)
    var hpfPath = Object.keys(zip.files).filter(function (n) { return /(^|\/)content\.hpf$/.test(n); })[0];
    var hpfDoc = hpfPath ? parseXml(await zip.file(hpfPath).async('string')) : null;
    var manifest = hpfDoc ? byTag(hpfDoc, 'opf:manifest')[0] : null;
    var imgNo = nextImageNumber(zip, hpfDoc);

    // 사진을 BinData 에 등록
    var prepared = items.map(function (it) {
      var out = { values: it.values || {}, photo: null };
      if (it.photo && it.photo.data) {
        var ext = (it.photo.ext || 'jpg').toLowerCase();
        var binId = 'image' + imgNo++;
        var fname = binId + '.' + ext;
        zip.file('BinData/' + fname, it.photo.data);
        if (manifest) {
          var item = hpfDoc.createElementNS(NS.opf, 'opf:item');
          item.setAttribute('id', binId);
          item.setAttribute('href', 'BinData/' + fname);
          item.setAttribute('media-type', ext === 'png' ? 'image/png' : 'image/jpeg');
          item.setAttribute('isEmbeded', '1');
          manifest.appendChild(item);
        }
        out.photo = { binId: binId, width: it.photo.width, height: it.photo.height };
      }
      return out;
    });

    // 본문 복제 + 치환
    var doc = parseXml(await zip.file(info.sectionPath).async('string'));
    var rootEl = doc.documentElement;
    var kids = elChildren(rootEl);
    kids.forEach(function (k) { rootEl.removeChild(k); });
    var ctx = { nextId: 1900000000 + Math.floor(Math.random() * 1000000), z: 1000 };

    prepared.forEach(function (item, idx) {
      var copies = kids.map(function (k) { return k.cloneNode(true); });
      if (idx > 0) {
        copies.forEach(stripSectionHeader);
        if (copies[0] && copies[0].nodeName === 'hp:p') copies[0].setAttribute('pageBreak', '1');
      }
      allParagraphs(copies).forEach(function (p) { fillParagraph(doc, p, item, ctx); });
      copies.forEach(function (c) {
        byTag(c, 'hp:linesegarray').forEach(function (l) { l.parentNode.removeChild(l); });
        if (c.nodeName === 'hp:p') elChildren(c).forEach(function (x) { if (x.nodeName === 'hp:linesegarray') c.removeChild(x); });
        rootEl.appendChild(c);
      });
    });

    zip.file(info.sectionPath, serializeXml(doc));
    if (hpfDoc) zip.file(hpfPath, serializeXml(hpfDoc));
    if (zip.file('mimetype')) zip.file('mimetype', await zip.file('mimetype').async('string'), { compression: 'STORE' });

    return zip.generateAsync({ type: 'uint8array', compression: 'DEFLATE', mimeType: 'application/hwp+zip' });
  }

  /* ---------- EXIF 촬영일 ---------- */
  function pad2(n) { return (n < 10 ? '0' : '') + n; }
  function formatDate(y, m, d) { return y + '. ' + pad2(m) + '. ' + pad2(d) + '.'; }

  function readTiffDate(v, base, end) {
    if (base + 8 > end) return null;
    var little = v.getUint16(base) === 0x4949;
    var g16 = function (o) { return v.getUint16(o, little); };
    var g32 = function (o) { return v.getUint32(o, little); };
    var readStr = function (entry) {
      var count = g32(entry + 4), off = count > 4 ? base + g32(entry + 8) : entry + 8;
      if (off + count > v.byteLength) return null;
      var s = '';
      for (var i = 0; i < count - 1; i++) s += String.fromCharCode(v.getUint8(off + i));
      return s;
    };
    var scan = function (ifd, wanted) {
      var found = {};
      if (ifd + 2 > end) return found;
      var n = g16(ifd);
      for (var i = 0; i < n; i++) {
        var e = ifd + 2 + i * 12;
        if (e + 12 > end) break;
        var tag = g16(e);
        if (wanted.indexOf(tag) >= 0) found[tag] = e;
      }
      return found;
    };
    var ifd0 = base + g32(base + 4);
    var f0 = scan(ifd0, [0x8769, 0x0132]);
    var dt = null;
    if (f0[0x8769]) {
      var f1 = scan(base + g32(f0[0x8769] + 8), [0x9003, 0x9004]);
      var e = f1[0x9003] || f1[0x9004];
      if (e) dt = readStr(e);
    }
    if (!dt && f0[0x0132]) dt = readStr(f0[0x0132]);
    var m = dt && dt.match(/^(\d{4}):(\d{2}):(\d{2})/);
    if (!m || m[1] === '0000') return null;
    return { y: +m[1], m: +m[2], d: +m[3] };
  }

  /** JPEG 의 촬영일을 "2026. 11. 24." 형태로. 없으면 null */
  function parseExifDate(arrayBuffer) {
    try {
      var v = new DataView(arrayBuffer);
      if (v.byteLength < 12 || v.getUint16(0) !== 0xffd8) return null;
      var off = 2;
      while (off + 4 < v.byteLength) {
        var marker = v.getUint16(off); off += 2;
        if (marker === 0xffda || (marker & 0xff00) !== 0xff00) break;
        var len = v.getUint16(off);
        if (marker === 0xffe1 && v.getUint32(off + 2) === 0x45786966) {
          var r = readTiffDate(v, off + 8, off + len);
          return r ? formatDate(r.y, r.m, r.d) : null;
        }
        off += len;
      }
    } catch (e) { /* 읽을 수 없으면 날짜 없음 */ }
    return null;
  }

  /* ---------- 예시 양식(.hwpx) 만들기 ---------- */
  var NSDECL =
    'xmlns:ha="http://www.hancom.co.kr/hwpml/2011/app" xmlns:hp="http://www.hancom.co.kr/hwpml/2011/paragraph" ' +
    'xmlns:hp10="http://www.hancom.co.kr/hwpml/2016/paragraph" xmlns:hs="http://www.hancom.co.kr/hwpml/2011/section" ' +
    'xmlns:hc="http://www.hancom.co.kr/hwpml/2011/core" xmlns:hh="http://www.hancom.co.kr/hwpml/2011/head" ' +
    'xmlns:hhs="http://www.hancom.co.kr/hwpml/2011/history" xmlns:hm="http://www.hancom.co.kr/hwpml/2011/master-page" ' +
    'xmlns:hpf="http://www.hancom.co.kr/schema/2011/hpf" xmlns:dc="http://purl.org/dc/elements/1.1/" ' +
    'xmlns:opf="http://www.idpf.org/2007/opf/" xmlns:epub="http://www.idpf.org/2007/ops" ' +
    'xmlns:config="urn:oasis:names:tc:opendocument:xmlns:config:1.0"';

  function sampleHeader() {
    var langs = ['HANGUL', 'LATIN', 'HANJA', 'JAPANESE', 'OTHER', 'SYMBOL', 'USER'];
    var fonts = langs.map(function (l) {
      return '<hh:fontface lang="' + l + '" fontCnt="1"><hh:font id="0" face="맑은 고딕" type="TTF" isEmbedded="0"/></hh:fontface>';
    }).join('');
    var bd = function (id, type, fill) {
      var b = function (n) { return '<hh:' + n + 'Border type="' + type + '" width="0.12 mm" color="#000000"/>'; };
      return '<hh:borderFill id="' + id + '" threeD="0" shadow="0" centerLine="NONE" breakCellSeparateLine="0">' +
        '<hh:slash type="NONE" Crooked="0" isCounter="0"/><hh:backSlash type="NONE" Crooked="0" isCounter="0"/>' +
        b('left') + b('right') + b('top') + b('bottom') +
        '<hh:diagonal type="SOLID" width="0.1 mm" color="#000000"/>' +
        (fill ? '<hc:fillBrush><hc:winBrush faceColor="' + fill + '" hatchColor="#999999" alpha="0"/></hc:fillBrush>' : '') +
        '</hh:borderFill>';
    };
    var same = function (n) {
      return '<hh:fontRef hangul="0" latin="0" hanja="0" japanese="0" other="0" symbol="0" user="0"/>' +
        '<hh:ratio hangul="100" latin="100" hanja="100" japanese="100" other="100" symbol="100" user="100"/>' +
        '<hh:spacing hangul="0" latin="0" hanja="0" japanese="0" other="0" symbol="0" user="0"/>' +
        '<hh:relSz hangul="100" latin="100" hanja="100" japanese="100" other="100" symbol="100" user="100"/>' +
        '<hh:offset hangul="0" latin="0" hanja="0" japanese="0" other="0" symbol="0" user="0"/>' + n +
        '<hh:underline type="NONE" shape="SOLID" color="#000000"/><hh:strikeout shape="NONE" color="#000000"/>' +
        '<hh:outline type="NONE"/><hh:shadow type="NONE" color="#B2B2B2" offsetX="10" offsetY="10"/>';
    };
    var charPr = function (id, h, extra) {
      return '<hh:charPr id="' + id + '" height="' + h + '" textColor="#000000" shadeColor="none" useFontSpace="0" useKerning="0" symMark="NONE" borderFillIDRef="1">' + same(extra) + '</hh:charPr>';
    };
    var paraPr = function (id, align) {
      return '<hh:paraPr id="' + id + '" tabPrIDRef="0" condense="0" fontLineHeight="0" snapToGrid="1" suppressLineNumbers="0" checked="0">' +
        '<hh:align horizontal="' + align + '" vertical="BASELINE"/><hh:heading type="NONE" idRef="0" level="0"/>' +
        '<hh:breakSetting breakLatinWord="KEEP_WORD" breakNonLatinWord="KEEP_WORD" widowOrphan="0" keepWithNext="0" keepLines="0" pageBreakBefore="0" lineWrap="BREAK"/>' +
        '<hh:autoSpacing eAsianEng="0" eAsianNum="0"/>' +
        '<hh:margin><hc:intent value="0" unit="HWPUNIT"/><hc:left value="0" unit="HWPUNIT"/><hc:right value="0" unit="HWPUNIT"/><hc:prev value="0" unit="HWPUNIT"/><hc:next value="0" unit="HWPUNIT"/></hh:margin>' +
        '<hh:lineSpacing type="PERCENT" value="130" unit="HWPUNIT"/>' +
        '<hh:border borderFillIDRef="1" offsetLeft="0" offsetRight="0" offsetTop="0" offsetBottom="0" connect="0" ignoreMargin="0"/>' +
        '</hh:paraPr>';
    };
    var style = function (id, name, eng, pp, cp) {
      return '<hh:style id="' + id + '" type="PARA" name="' + name + '" engName="' + eng + '" paraPrIDRef="' + pp + '" charPrIDRef="' + cp + '" nextStyleIDRef="' + id + '" langID="1042" lockForm="0"/>';
    };
    return XML_DECL + '<hh:head ' + NSDECL + ' version="1.4" secCnt="1">' +
      '<hh:beginNum page="1" footnote="1" endnote="1" pic="1" tbl="1" equation="1"/>' +
      '<hh:refList>' +
      '<hh:fontfaces itemCnt="7">' + fonts + '</hh:fontfaces>' +
      '<hh:borderFills itemCnt="3">' + bd(1, 'NONE') + bd(2, 'SOLID') + bd(3, 'SOLID', '#F2F2F2') + '</hh:borderFills>' +
      '<hh:charProperties itemCnt="3">' + charPr(0, 1000, '') + charPr(1, 2000, '<hh:bold/>') + charPr(2, 1000, '<hh:bold/>') + '</hh:charProperties>' +
      '<hh:tabProperties itemCnt="1"><hh:tabPr id="0" autoTabLeft="0" autoTabRight="0"/></hh:tabProperties>' +
      '<hh:paraProperties itemCnt="2">' + paraPr(0, 'JUSTIFY') + paraPr(1, 'CENTER') + '</hh:paraProperties>' +
      '<hh:styles itemCnt="1">' + style(0, '바탕글', 'Normal', 0, 0) + '</hh:styles>' +
      '</hh:refList>' +
      '<hh:compatibleDocument targetProgram="HWP2018"><hh:layoutCompatibility/></hh:compatibleDocument>' +
      '<hh:docOption><hh:linkinfo path="" pageInherit="0" footnoteInherit="0"/></hh:docOption>' +
      '<hh:trackchageConfig flags="56"/>' +
      '</hh:head>';
  }

  function sampleSection() {
    var P = function (inner, pp, cp) {
      return '<hp:p id="0" paraPrIDRef="' + (pp || 0) + '" styleIDRef="0" pageBreak="0" columnBreak="0" merged="0">' +
        '<hp:run charPrIDRef="' + (cp || 0) + '">' + inner + '</hp:run></hp:p>';
    };
    var T = function (s) { return '<hp:t>' + s + '</hp:t>'; };
    var cell = function (col, row, w, h, body, fill) {
      return '<hp:tc name="" header="0" hasMargin="0" protect="0" editable="0" dirty="0" borderFillIDRef="' + (fill ? 3 : 2) + '">' +
        '<hp:subList id="" textDirection="HORIZONTAL" lineWrap="BREAK" vertAlign="CENTER" linkListIDRef="0" linkListNextIDRef="0" textWidth="0" textHeight="0" hasTextRef="0" hasNumRef="0">' +
        body + '</hp:subList>' +
        '<hp:cellAddr colAddr="' + col + '" rowAddr="' + row + '"/><hp:cellSpan colSpan="1" rowSpan="1"/>' +
        '<hp:cellSz width="' + w + '" height="' + h + '"/><hp:cellMargin left="510" right="510" top="141" bottom="141"/></hp:tc>';
    };
    var W1 = 9000, W2 = 33520;
    var rows = [['품목', '{품목}', 3200], ['구입일', '{날짜}', 3200], ['수량', '{수량}', 3200], ['금액', '{금액}원', 3200], ['사진', '{사진}', 26000]];
    var totalH = rows.reduce(function (a, r) { return a + r[2]; }, 0);
    var trs = rows.map(function (r, i) {
      return '<hp:tr>' + cell(0, i, W1, r[2], P(T(r[0]), 1, 2), true) + cell(1, i, W2, r[2], P(T(r[1]), 0, 0), false) + '</hp:tr>';
    }).join('');
    var tbl = '<hp:tbl id="1000000001" zOrder="0" numberingType="TABLE" textWrap="TOP_AND_BOTTOM" textFlow="BOTH_SIDES" lock="0" dropcapstyle="None" pageBreak="CELL" repeatHeader="0" rowCnt="' + rows.length + '" colCnt="2" cellSpacing="0" borderFillIDRef="2" noAdjust="0">' +
      '<hp:sz width="' + (W1 + W2) + '" widthRelTo="ABSOLUTE" height="' + totalH + '" heightRelTo="ABSOLUTE" protect="0"/>' +
      '<hp:pos treatAsChar="1" affectLSpacing="0" flowWithText="1" allowOverlap="0" holdAnchorAndSO="0" vertRelTo="PARA" horzRelTo="PARA" vertAlign="TOP" horzAlign="LEFT" vertOffset="0" horzOffset="0"/>' +
      '<hp:outMargin left="0" right="0" top="0" bottom="0"/><hp:inMargin left="510" right="510" top="141" bottom="141"/>' +
      trs + '</hp:tbl>';

    var noteNum = function (t) {
      return '<hp:footNotePr><hp:autoNumFormat type="DIGIT" userChar="" prefixChar="" suffixChar=")" supscript="0"/>' +
        '<hp:noteLine length="-1" type="SOLID" width="0.12 mm" color="#000000"/><hp:noteSpacing betweenNotes="283" belowLine="567" aboveLine="850"/>' +
        '<hp:numbering type="CONTINUOUS" newNum="1"/><hp:placement place="EACH_COLUMN" beneathText="0"/></hp:footNotePr>';
    };
    var endNote = noteNum().replace(/footNotePr/g, 'endNotePr').replace('EACH_COLUMN', 'END_OF_DOCUMENT');
    var pbf = function (t) {
      return '<hp:pageBorderFill type="' + t + '" borderFillIDRef="1" textBorder="PAPER" headerInside="0" footerInside="0" fillArea="PAPER"><hp:offset left="1417" right="1417" top="1417" bottom="1417"/></hp:pageBorderFill>';
    };
    var secPr = '<hp:secPr id="" textDirection="HORIZONTAL" spaceColumns="1134" tabStop="8000" tabStopVal="4000" tabStopUnit="HWPUNIT" outlineShapeIDRef="0" memoShapeIDRef="0" textVerticalWidthHead="0" masterPageCnt="0">' +
      '<hp:grid lineGrid="0" charGrid="0" wonggojiFormat="0"/><hp:startNum pageStartsOn="BOTH" page="0" pic="0" tbl="0" equation="0"/>' +
      '<hp:visibility hideFirstHeader="0" hideFirstFooter="0" hideFirstMasterPage="0" border="SHOW_ALL" fill="SHOW_ALL" hideFirstPageNum="0" hideFirstEmptyLine="0" showLineNumber="0"/>' +
      '<hp:lineNumberShape restartType="0" countBy="0" distance="0" startNumber="0"/>' +
      '<hp:pagePr landscape="WIDELY" width="59528" height="84186" gutterType="LEFT_ONLY"><hp:margin header="4252" footer="4252" gutter="0" left="8504" right="8504" top="5668" bottom="4252"/></hp:pagePr>' +
      noteNum() + endNote + pbf('BOTH') + pbf('EVEN') + pbf('ODD') + '</hp:secPr>' +
      '<hp:ctrl><hp:colPr id="" type="NEWSPAPER" layout="LEFT" colCount="1" sameSz="1" sameGap="0"/></hp:ctrl>';

    return XML_DECL + '<hs:sec ' + NSDECL + '>' +
      P(secPr + T('물품 구입 증빙 사진'), 1, 1) +
      P('', 0, 0) +
      P(tbl + T(''), 0, 0) +
      '</hs:sec>';
  }

  /** "예시 양식 내려받기"용 HWPX 를 만든다 */
  async function buildSampleTemplate() {
    var JSZip = getJSZip();
    var zip = new JSZip();
    zip.file('mimetype', 'application/hwp+zip', { compression: 'STORE' });
    zip.file('version.xml', XML_DECL + '<hv:HCFVersion xmlns:hv="http://www.hancom.co.kr/hwpml/2011/version" tagetApplication="WORDPROCESSOR" major="5" minor="1" micro="1" buildNumber="0" os="1" xmlVersion="1.4" application="Hancom Office Hangul" appVersion="11, 0, 0, 0 WIN32LEWindows_10"/>');
    zip.file('META-INF/container.xml', XML_DECL + '<ocf:container xmlns:ocf="urn:oasis:names:tc:opendocument:xmlns:container" xmlns:hpf="http://www.hancom.co.kr/schema/2011/hpf"><ocf:rootfiles><ocf:rootfile full-path="Contents/content.hpf" media-type="application/hwpml-package+xml"/></ocf:rootfiles></ocf:container>');
    zip.file('META-INF/manifest.xml', XML_DECL + '<odf:manifest xmlns:odf="urn:oasis:names:tc:opendocument:xmlns:manifest:1.0"/>');
    zip.file('Contents/content.hpf', XML_DECL + '<opf:package ' + NSDECL + ' version="" unique-identifier="" id="">' +
      '<opf:metadata><opf:title>물품 구입 증빙 사진 양식</opf:title><opf:language>ko</opf:language></opf:metadata>' +
      '<opf:manifest><opf:item id="header" href="Contents/header.xml" media-type="application/xml"/>' +
      '<opf:item id="section0" href="Contents/section0.xml" media-type="application/xml"/>' +
      '<opf:item id="settings" href="settings.xml" media-type="application/xml"/></opf:manifest>' +
      '<opf:spine><opf:itemref idref="header" linear="yes"/><opf:itemref idref="section0" linear="yes"/></opf:spine></opf:package>');
    zip.file('Contents/header.xml', sampleHeader());
    zip.file('Contents/section0.xml', sampleSection());
    zip.file('settings.xml', XML_DECL + '<ha:HWPApplicationSetting xmlns:ha="http://www.hancom.co.kr/hwpml/2011/app" xmlns:config="urn:oasis:names:tc:opendocument:xmlns:config:1.0"><ha:CaretPosition listIDRef="0" paraIDRef="0" pos="0"/></ha:HWPApplicationSetting>');
    return zip.generateAsync({ type: 'uint8array', compression: 'DEFLATE', mimeType: 'application/hwp+zip' });
  }

  var api = {
    inspectTemplate: inspectTemplate,
    fillTemplate: fillTemplate,
    buildSampleTemplate: buildSampleTemplate,
    parseExifDate: parseExifDate,
    formatDate: formatDate
  };
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
  else root.Hwpx = api;
})(typeof globalThis !== 'undefined' ? globalThis : this);
