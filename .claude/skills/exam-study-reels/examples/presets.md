# 시리즈 프리셋 (환경변수)
공통: ENGINE=v2 PROGRESS=1 TAIL=2.8 · 종이: `python scripts/paper.py $REELS_WORK/assets_src/paper_X.jpg "R,G,B"`

## 정책론 (버터옐로 + 네이비, 올빼미, 노선도)
CHARACTER=owl STYLE=route PAPER_FILE=paper_yellow.jpg (252,240,188) ACCENT='#1f3a68' ACCENT_T='#1f3a68' ACCENT_L='#9db8ee' ACCENT_RGB='31,58,104'

## 행정론 (아쿠아민트 + 코랄, 비버, 결재 체크리스트)
CHARACTER=beaver STYLE=check PAPER_FILE=paper_aqua.jpg (198,236,232) ACCENT='#e0523f' ACCENT_T='#d94a38' ACCENT_L='#ff9c8c' ACCENT_RGB='224,82,63'

## 법제론 (연살구 + 딥그린, 펭귄 판사, 조문 카드)
CHARACTER=penguin STYLE=law PAPER_FILE=paper_peach.jpg (255,222,204) ACCENT='#1d5c4a' ACCENT_T='#1d5c4a' ACCENT_L='#7fd3b6' ACCENT_RGB='29,92,74'

## 새 캐릭터 후보 (미리보기 확인 완료)
- 토끼 `CHARACTER=rabbit` — 흰 토끼, 쫑긋 귀·손 흔들기. 추천 조합: 연노랑 종이 + 로즈 `#d9487a`
- 곰 `CHARACTER=bear` — 스카프 두른 갈색 곰, 책 더미. 추천 조합: 하늘색 종이 + 브라운 `#8a5530`
- 거북이 `CHARACTER=turtle` — 안경 쓴 거북이 박사, 바위 위. 추천 조합: 크림 종이 + 청록 `#0f8a8a`
(ACCENT 값은 캐릭터 소품·배지·버튼에 쓰이니 `ACCENT/ACCENT_T/ACCENT_L/ACCENT_RGB`를 함께 맞춰 주세요)
