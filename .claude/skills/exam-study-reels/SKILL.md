---
name: exam-study-reels
description: 자격시험(예 사회복지사 1급) 기출문제 PDF를 읽고, 헷갈리는 개념 쌍을 캐릭터·이야기형 세로 릴스(1080×1920, 한국어 여성 음성·자막·배경음악, 오답 "틀림!" 도장, 댓글 퀴즈)로 영역별 시리즈 제작하는 워크플로. HyperFrames로 렌더링. "기출문제를 릴스/쇼츠/모션그래픽 영상으로", "수험생용 콘텐츠 영상 시리즈", "같은 틀로 다른 과목도", "바탕색 바꿔서", "이 영상 스타일처럼" 요청에 사용.
---

# 수험 기출 → 릴스 시리즈 제작 (exam-study-reels)

기출문제 PDF 한 권을 **개념 쌍(헷갈리는 것끼리) 단위의 30~55초 릴스 여러 편**으로 바꾼다.
한 편의 구성: **후킹 → 개념 카드 → 기출 응용 "틀림!" 도장 → 댓글 퀴즈**. 음성은 edge-tts(ko-KR-SunHiNeural), 음악은 직접 합성, 렌더링은 HyperFrames(HTML→MP4).

## 두 가지 스타일 엔진
| 엔진 | 모양 | 쓰임 |
|---|---|---|
| `ENGINE=v1` 카드 테마 | 단색 바탕(크림/하늘 등) + 보라·민트 카드 줄 + 다람쥐 캐릭터 + 하단 네이비 자막 | 조사론(크림), 인간행동(하늘색) |
| `ENGINE=v2` 종이·주황 모션 | 구겨진 종이 질감 바탕 + 굵은 검정 헤드라인/주황 강조 + 흰 알약 카드 패널 + 다크 목업/도장 + 주황 공에 매달린 캐릭터 | 실천론(세이지 그린 종이) — 사용자가 준 레퍼런스 모션그래픽 스타일 |
바탕색은 영역마다 바꾼다(피드에서 구분). 자세한 값과 바꾸는 법: `references/style-guide.md`.
- v2 옵션: `CHARACTER=swing`(주황 공에 매달린 여자아이, 기본) | `CHARACTER=cat`(책 더미에 앉아 손 흔드는 안경 고양이) | `CHARACTER=dog`(주황 스툴에 앉아 손 흔드는 강아지 — 꼬리·귀·손·눈 모션) · `PAPER_FILE=paper_pink.jpg`(종이색: `scripts/paper.py <out.jpg> "R,G,B"`로 영역별 생성).
- v2 확장(3교시 시리즈에서 추가): `CHARACTER=owl|beaver|penguin|rabbit|bear|turtle`(올빼미 박사·비버 팀장·펭귄 판사·토끼·곰·거북이), `STYLE=route|check|law`(노선도 / 결재 체크리스트+빨간펜 / 조문 § 카드), `ACCENT`·`ACCENT_T`·`ACCENT_L`·`ACCENT_RGB`(포인트 컬러), `PROGRESS=1`(HUD에 EP n/총편수 + 진행 막대), `TAIL=2.8`(정답 공개용 꼬리).
  - 정답 공개: 마지막 줄에 `pause=2.3`을 주고 cta에 `reveal=dict(line=정답줄, answer=정답버튼번호)` → 3·2·1 카운트다운 후 정답 버튼이 초록으로 강조.
  - `versus` 장면: 좌우 비교 카드(`left`/`right`=dict(line,title,items 2~4개)) + VS 배지.
  - 시리즈 프리셋은 `examples/presets.md` 참고.
- 지금까지: 조사론=v1 크림, 인간행동=v1 하늘색, 실천론=v2 세이지 + swing, 실천기술론=v2 연분홍 + cat, 지역사회복지론=v2 연보라 + dog, **정책론=버터옐로+네이비+올빼미+노선도, 행정론=아쿠아민트+코랄+비버+체크리스트, 법제론=연살구+딥그린+펭귄+조문카드**.

## 사전 조건
- `ffmpeg`/`ffprobe`, `node`/`npm`, `python3`, (선택) `uv`.
- HyperFrames CLI: `/root/.claude/skills/hyperframes/scripts/plugin-cli.mjs`가 있으면 사용, 없으면 `npx hyperframes@0.9.75`. HyperFrames 스킬이 있으면 **먼저 읽는다**(렌더 규칙).
- 네트워크: 클라우드 환경은 호스트 허용 목록이 있다. 음성에 `speech.platform.bing.com`이 필요하다(막히면 `update_environment`로 **그 호스트만** 요청 — 사용자 승인 필요. 사용 후 제거를 권고). 폰트·GSAP는 CDN이 아니라 **npm 레지스트리**로 받는다(`setup.sh`가 처리).

## 작업 순서
1. **문제지 읽기**: PDF는 `Read`의 `pages` 파라미터로 20쪽 이하씩. 과목 경계를 찾는다(예: 2교시 1~25번 실천론, 26번부터 실천기술론).
2. **문항 풀이와 정답표 작성**: 공식 정답표가 있으면 반드시 대조한다(정답 오류 사례: 지역사회복지론 55번을 이론으로 추정해 틀렸다가 정답표로 정정). 정답표가 없으면 직접 풀고 **확신도**를 기록한다. 확신이 낮거나 교재마다 다를 수 있는 문항은 **제작에서 제외**하고 사용자에게 알린다(`references/lessons.md`의 정확도 규칙).
3. **편 구성**: 25문항 ≈ 8~10편. 개념 쌍/묶음 단위(예: 신뢰도 vs 타당도, 인보관 vs 자선조직협회). 한 편에 카드 장면 1~3개 + "틀림!" 장면 1~2개 + 퀴즈.
4. **콘텐츠 파일 작성**: `episodes_<이름>.py` (스키마: `references/schema.md`, 실제 예: `examples/`). 발음이 어려운 숫자/영문은 `say`(읽는 말)와 `cap`(자막)을 분리.
5. **작업공간 준비(1회)**: `bash scripts/setup.sh` (폰트·GSAP·종이 텍스처·venv).
6. **파이프라인**:
   ```bash
   export REELS_WORK=$PWD/reels_work REELS_CONTENT=<episodes 파일이 있는 폴더>
   export EPMOD=episodes_<이름> SERIESDIR=series_<이름> ENGINE=v1|v2 BRAND='시리즈 이름'
   # v1이면 바탕색: GROUND='#e3f0ff' BLOB_A='rgba(255,201,60,0.34)' BLOB_B='rgba(108,77,246,0.16)'
   # v2 예: PAPER_FILE=paper_pink.jpg CHARACTER=cat  (종이는 $REELS_WORK/assets_src/에 paper.py로 미리 생성)
   python3 scripts/lint_content.py            # 글자 넘침 + 자막 4줄 이상 사전 점검(필수, 통과할 때까지 문구 수정)
   bash scripts/run_pipeline.sh tts           # 음성 생성 → 길이로 타이밍 계산
   bash scripts/run_pipeline.sh html          # 장면/자막 HTML 생성
   bash scripts/run_pipeline.sh audio         # 해설 + 음악 믹스(해설 중 음악 자동 감소)
   bash scripts/run_pipeline.sh check         # 릴스 안전영역·대비·레이아웃 검사
   bash scripts/run_pipeline.sh snapshot 1 4  # 대표 편 contact sheet → Read로 눈으로 확인
   bash scripts/run_pipeline.sh render        # 3편씩 병렬 렌더(편당 2~4분)
   ```
   `all`은 tts→html→audio→check까지. 렌더는 오래 걸리니 `run_in_background`로 돌리고 완료 알림을 기다린다.
7. **눈으로 검수**: snapshot의 contact sheet를 최소 2~3편 열어 본다(줄바꿈 이상, 겹침, 도장 위치). 문제는 템플릿/콘텐츠를 고쳐 html→check 반복.
8. **전달**: `SendUserFile`로 MP4들을 보낸다(여러 파일 한 번에). 아래 "보고 규칙" 따르기.

## 콘텐츠 규칙 (요약)
- 한 줄 해설(`say`)은 4~7초, **자막이 3줄을 넘으면 카드를 가리므로 약 45자 이내**(lint가 검사). 한 편 총 35~55초. 마지막 줄은 댓글 퀴즈(정답은 고정 댓글로 공개).
- 카드 행: 제목 짧게(2줄 금지), 설명은 N=4일 때 한 줄. `mark`로 ○/✕.
- `exam` 장면은 **틀린 문장을 따옴표 카드로 보여 주고 도장**. 정답 보기는 "정답!" 등 초록 도장.
- 기출 원문을 그대로 옮기지 말고 **개념으로 풀어 쓰기** + "제N회 기출 응용" 출처 표기.
- 규격: 안전영역(릴스) 위 288px ~ 아래 1248px, 좌우 120px. 자막 하단은 y=1240 이내.

## 보고 규칙 (사용자에게)
- 편 목록·길이·다룬 기출 번호, 퀴즈 정답표.
- **정답 대조 필요**(정답표가 없었다면 직접 푼 것임을 명시, 낮은 확신 문항 나열), 제외한 문항과 이유.
- AI 음성 발음 어색함 가능, 파일은 임시 폴더라 즉시 내려받기, 열어 둔 네트워크 호스트 제거 권고.
- 다음 제안: 인스타 캡션/해시태그/고정 댓글, 다른 영역 확장, 바탕색 변경.

## 파일
- `scripts/setup.sh` 작업공간 준비 · `scripts/run_pipeline.sh` 단계 실행 · `scripts/build_ep.py`(v1 엔진, TTS·타이밍·오디오 공용) · `scripts/build_v2.py`(v2 엔진) · `scripts/music.py` · `scripts/paper.py` · `scripts/lint_content.py` · `scripts/summarize_checks.py`
- `references/schema.md` 콘텐츠 스키마 · `references/style-guide.md` 디자인 값 · `references/lessons.md` 함정·교훈
- `examples/episodes_josaron.py`(조사론 8편, v1) · `examples/episodes_hbse.py`(인간행동 10편, v1) · `examples/episodes_prac.py`(실천론 10편, v2) · `examples/episodes_tech.py`(실천기술론 9편, v2 + 분홍 종이 + 고양이) · `examples/episodes_community.py`(지역사회복지론 9편, v2 + 연보라 종이 + 강아지) · `episodes_policy.py`(정책론 9편) · `episodes_admin.py`(행정론 7편) · `episodes_law.py`(법제론 8편)
