# 콘텐츠 스키마 (`episodes_<이름>.py`)

파일 하나에 `EPS = {}` 딕셔너리를 두고 `EPS[번호] = dict(...)`로 편을 정의한다. `EPMOD=episodes_<이름>`, `REELS_CONTENT=<폴더>`로 가리킨다. 실제 예: `examples/`.

```python
EPS[1] = dict(
    music=(104, 0, 21),          # (BPM 88~110, 코드 진행 회전 0~3, 랜덤 시드) — 편마다 다르게
    lines=[                       # 해설 한 줄 = 자막 한 장 = 화면 단서 하나
        dict(say="읽을 문장"),                                   # 자막도 같은 문장
        dict(say="신뢰수준을 구십오 퍼센트로", cap="신뢰수준을 95%로"),  # 읽는 말과 자막을 분리
    ],
    scenes=[ ... ],               # 아래 장면 타입. 모든 줄(lines 인덱스)이 정확히 한 장면에 속해야 한다
)
```

## 줄(lines)
- `say`: TTS가 읽는 문장. **숫자·영문은 한글로 풀어 쓴다**(1종→일종, A4→에이포, BAB→비에이비, 95%→구십오 퍼센트).
- `cap`(선택): 화면 자막. 없으면 `say`. 자막은 자동 줄바꿈(한 줄 약 16자, 최대 3~4줄).
- 한 줄 4~7초(약 25~45자). 줄 사이 0.45초 간격, 맨 앞 0.3초, 맨 뒤 2초 여유가 자동으로 들어간다.

## 장면(scenes) — 공통
`type`, `lines`(이 장면이 차지하는 줄 인덱스 목록, 연속이어야 함). 장면 길이는 줄 길이로 자동 결정된다.
`[[강조]]` 표기: 헤드라인/예시문에서 강조(주황 글자 또는 형광펜).

## v1 엔진 (카드 테마)
| type | 필드 |
|---|---|
| `hook` | `sub`(작은 부제), `words`(큰 제목 단어 2~4개), `joiner`("VS"/"&"/"") |
| `cards` | `header`(노란 칩), `rows`: `dict(line, color, title, desc, mark?)` — 행 1~4개 |
| `exam` | `tag`(예: "제24회 기출 응용 · 조사론 · 28번"), `html`(예시문, `<br>`·`[[ ]]`), `stamp`, `stamp_color`, `stamp_line`, `stamp_frac`(0~1, 그 줄의 어느 시점에 도장) |
| `cta` | `q`(질문, 14자 이내), `buttons`=[(글자, 색), (글자, 색)], `hint` |
- 색: `P`(보라 #6c4df6) `T`(민트 #0e9488) `C`(코랄 #e0344f) `A`(호박 #c26a0e) — `episodes_*.py`에서 문자열로 직접 지정.

## v2 엔진 (종이·주황 모션)
| type | 필드 |
|---|---|
| `hook` | `headline`(2줄, `<br>`·`[[ ]]`) — 캐릭터가 공을 타고 흔들림 |
| `cards` | `headline`, `rows`: `dict(line, title, desc, mark?, badge?)` — 번호 배지 자동 01.. (`badge="05"`로 지정 가능) |
| `exam` | `headline`, `tag`, `html`, `stamp`, `stamp_color`(오답 `#e8431a` / 정답 `#12a37f`), `stamp_line`, `stamp_frac` |
| `cta` | `headline`, `q`, `buttons`=[(글자, 0), (글자, 1)] (0=주황, 1=크림) |

## 행(rows) 규칙
- `line`: 이 행이 **나타나는 줄**. 같은 줄의 행들은 0.2초 간격으로 차례로 나타남.
- `desc`의 `<br>`로 2줄. 행이 4개면 한 줄만(작은 글씨). 행 3개 이하일 때 2줄 가능.
- `mark`: `"o"`(○ 맞음) / `"x"`(✕ 틀림). 마크가 있으면 글자 폭이 줄어드니 제목 9자 이내.

## 글자 폭 한계 (넘치면 줄바꿈이 깨짐)
- 예시문(`exam.html`): 한 줄 약 13자(영문·숫자는 절반). `<br>`로 직접 끊는다. 3줄까지.
- 퀴즈 버튼: 한 줄에 2개 — 각 5~6자 이내("민주주의?" 가능, "비동일 통제집단?" 불가).
- 퀴즈 질문(`q`): 14자 이내.
- `python3 scripts/lint_content.py`로 한계를 사전 점검한다.

## v2 추가 항목
- 줄(line): `pause`(초) — 이 줄 앞에 침묵을 넣는다(정답 공개 카운트다운용, 보통 2.3).
- `versus`: `headline`, `left`/`right`=dict(`line`, `title`(7자 이내), `items`(2~4개, 각 9자 이내)) — 좌우 비교 + VS 배지.
- `cta.reveal`: dict(`line`=정답을 말하는 줄, `answer`=정답 버튼 인덱스) — 3-2-1 카운트다운 뒤 정답 강조.
- `exam`을 여러 줄에 걸치려면 `lines=[앞줄, ..., stamp_line]`.
- 환경변수: CHARACTER(owl|beaver|penguin 추가), STYLE(route|check|law), ACCENT*, PROGRESS, TAIL — SKILL.md 참고.

## 캡션 자동 생성용 선택 필드 (에피소드 수준)
- `caption`: 캡션 첫 줄(기본: hook 헤드라인) · `answer`: 고정 댓글 문구(기본: cta.reveal 정답 줄). `scripts/make_captions.py`가 사용.
