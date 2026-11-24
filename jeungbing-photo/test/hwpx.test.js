const test = require('node:test');
const assert = require('node:assert/strict');
const { DOMParser, XMLSerializer } = require('@xmldom/xmldom');
const JSZip = require('jszip');
globalThis.DOMParser = DOMParser;
globalThis.XMLSerializer = XMLSerializer;
const Hwpx = require('../hwpx.js');

// 1x1 JPEG with EXIF DateTimeOriginal 2025:03:07 (hand-built)
function jpegWithExif(dateStr) {
  const ascii = Buffer.from(dateStr + '\0', 'latin1'); // 20 bytes
  // TIFF (little endian): header(8) + IFD0(2+12+4) + ExifIFD(2+12+4) + string
  const tiff = Buffer.alloc(8 + 18 + 18 + ascii.length);
  tiff.write('II', 0); tiff.writeUInt16LE(42, 2); tiff.writeUInt32LE(8, 4);
  let o = 8; tiff.writeUInt16LE(1, o); o += 2;
  tiff.writeUInt16LE(0x8769, o); tiff.writeUInt16LE(4, o + 2); tiff.writeUInt32LE(1, o + 4); tiff.writeUInt32LE(26, o + 8); o += 12;
  tiff.writeUInt32LE(0, o); o += 4;
  tiff.writeUInt16LE(1, o); o += 2;
  tiff.writeUInt16LE(0x9003, o); tiff.writeUInt16LE(2, o + 2); tiff.writeUInt32LE(ascii.length, o + 4); tiff.writeUInt32LE(44, o + 8); o += 12;
  tiff.writeUInt32LE(0, o); o += 4;
  ascii.copy(tiff, o);
  const exif = Buffer.concat([Buffer.from('Exif\0\0', 'latin1'), tiff]);
  const app1 = Buffer.alloc(4); app1.writeUInt16BE(0xffe1, 0); app1.writeUInt16BE(exif.length + 2, 2);
  return Buffer.concat([Buffer.from([0xff, 0xd8]), app1, exif, Buffer.from([0xff, 0xd9])]);
}

test('EXIF 촬영일 읽기', () => {
  const j = jpegWithExif('2025:03:07 14:22:01');
  const ab = j.buffer.slice(j.byteOffset, j.byteOffset + j.length);
  assert.equal(Hwpx.parseExifDate(ab), '2025. 03. 07.');
  assert.equal(Hwpx.parseExifDate(new Uint8Array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]).buffer), null);
});

test('예시 양식: 표시 인식', async () => {
  const buf = await Hwpx.buildSampleTemplate();
  const info = await Hwpx.inspectTemplate(buf);
  assert.deepEqual(info.tokens, ['품목', '날짜', '수량', '금액', '사진']);
  assert.equal(info.hasPhoto, true);
});

test('HWP(비 ZIP) 거부', async () => {
  await assert.rejects(Hwpx.inspectTemplate(Buffer.from('not a zip file at all')), /HWPX/);
});

test('3장 채우기: 글자·사진·쪽나눔·manifest', async () => {
  const tpl = await Hwpx.buildSampleTemplate();
  const jpg = jpegWithExif('2025:03:07 14:22:01');
  const mk = (n) => ({
    values: { 품목: '물품' + n, 날짜: '2026. 11. 2' + n + '.', 수량: String(n), 금액: n + ',000' },
    photo: { data: new Uint8Array(jpg), width: 4000, height: 3000, ext: 'jpg' },
  });
  const out = await Hwpx.fillTemplate(tpl, [mk(1), mk(2), mk(3)]);
  const zip = await JSZip.loadAsync(out);
  const names = Object.keys(zip.files);
  assert.equal(names[0], 'mimetype');
  ['BinData/image1.jpg', 'BinData/image2.jpg', 'BinData/image3.jpg'].forEach((n) => assert.ok(zip.file(n), n));

  const sec = await zip.file('Contents/section0.xml').async('string');
  assert.ok(!/\{[^{}]+\}/.test(sec), '남은 표시 없음');
  ['물품1', '물품2', '물품3', '2026. 11. 21.', '3,000원'].forEach((s) => assert.ok(sec.includes(s), s));
  assert.equal((sec.match(/<hp:pic /g) || []).length, 3);
  assert.equal((sec.match(/<hp:secPr /g) || []).length, 1, 'secPr 는 첫 장에만');
  assert.equal((sec.match(/pageBreak="1"/g) || []).length, 2);
  assert.ok(!sec.includes('linesegarray'));

  const ids = [...sec.matchAll(/<hp:pic [^>]*\bid="(\d+)"/g)].map((m) => m[1]);
  assert.equal(new Set(ids).size, 3, 'pic id 중복 없음');
  const refs = [...sec.matchAll(/binaryItemIDRef="([^"]+)"/g)].map((m) => m[1]);
  assert.deepEqual(refs, ['image1', 'image2', 'image3']);

  const hpf = await zip.file('Contents/content.hpf').async('string');
  refs.forEach((r) => assert.ok(hpf.includes('id="' + r + '"'), 'manifest ' + r));

  // 사진 크기: 셀(33520-1020-200 = 32300 폭) 안에서 4:3 유지
  const m = sec.match(/<hp:curSz width="(\d+)" height="(\d+)"/);
  const w = +m[1], h = +m[2];
  assert.ok(w <= 33520 && h <= 26000, `fit ${w}x${h}`);
  assert.ok(Math.abs(w / h - 4 / 3) < 0.01);

  // 결과도 XML 로 다시 파싱 가능
  const re = new DOMParser({ errorHandler: { error: (e) => { throw new Error(e); }, fatalError: (e) => { throw new Error(e); } } }).parseFromString(sec, 'text/xml');
  assert.ok(re.documentElement);
});

test('토큰이 여러 run 으로 쪼개진 경우도 치환', async () => {
  const tpl = await Hwpx.buildSampleTemplate();
  const zip = await JSZip.loadAsync(tpl);
  let sec = await zip.file('Contents/section0.xml').async('string');
  sec = sec.replace('<hp:t>{품목}</hp:t></hp:run>', '<hp:t>{품</hp:t></hp:run><hp:run charPrIDRef="0"><hp:t>목}</hp:t></hp:run>');
  zip.file('Contents/section0.xml', sec);
  const buf = await zip.generateAsync({ type: 'uint8array' });
  const info = await Hwpx.inspectTemplate(buf);
  assert.ok(info.tokens.includes('품목'));
  const out = await Hwpx.fillTemplate(buf, [{ values: { 품목: '복사용지' }, photo: null }]);
  const s = await (await JSZip.loadAsync(out)).file('Contents/section0.xml').async('string');
  assert.ok(s.includes('복사용지'));
  assert.ok(!s.includes('{'));
});

test('사진 없이도(빈칸) 생성', async () => {
  const tpl = await Hwpx.buildSampleTemplate();
  const out = await Hwpx.fillTemplate(tpl, [{ values: { 품목: 'A' }, photo: null }]);
  const s = await (await JSZip.loadAsync(out)).file('Contents/section0.xml').async('string');
  assert.ok(!s.includes('<hp:pic '));
  assert.ok(!/\{[^{}]+\}/.test(s));
});
