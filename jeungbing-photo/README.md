# 증빙사진 도우미

기관 HWPX 양식의 `{사진}` `{날짜}` `{품목}` `{수량}` `{금액}` 표시를 찾아,
휴대폰으로 찍은 사진과 입력한 글자로 채운 HWPX 를 만든다. 서버 없이 브라우저에서만 동작.

- 열기: `index.html` 을 정적 호스팅(GitHub Pages 등)하거나 `npx serve .`
- 테스트: `npm ci && npm test`
- 동작: HWPX(ZIP) 안 `Contents/section*.xml` 의 표시를 치환, 사진은 `BinData/` + `content.hpf` 에 등록 후 `<hp:pic>` 삽입.
  물품이 여러 개면 본문을 복제해 쪽 나눔으로 이어 붙임.
- 양식은 IndexedDB 에 저장(이 기기에만).
