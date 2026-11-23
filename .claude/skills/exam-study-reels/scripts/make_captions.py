# -*- coding: utf-8 -*-
# 에피소드 대본(EPS)에서 인스타 캡션 · 해시태그 · 고정 댓글(정답) 초안을 자동으로 만든다.
#   REELS_CONTENT=<examples> EPMOD=episodes_policy python3 scripts/make_captions.py "사회복지정책론" "#사회복지정책과제도" [출력.md]
# - 캡션 첫 줄: hook 헤드라인  /  고정 댓글: cta.reveal 의 정답 줄(없으면 "정답 확인 필요")
# - 에피소드에 caption="..." (캡션 첫 줄) / answer="..." (고정 댓글) 를 직접 적으면 그것을 우선 사용
# - 해시태그: 공통 + 과목 태그(인자) + 환경변수 HASHTAGS(공백 구분)로 추가
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault("EPMOD", os.environ.get("EPMOD", ""))
from build_ep import EPS

COMMON = "#사회복지사1급 #사회복지사 #사회복지사시험 #사회복지사1급기출 #사회복지사1급공부 #사회복지공부 #자격증공부 #수험생 #기출분석 #릴스공부"
EXAM_TAG = os.environ.get("EXAM_TAG", "#24회사회복지사")
EXAM_NAME = os.environ.get("EXAM_NAME", "제24회")   # 예: EXAM_NAME=제22회 EXAM_TAG=#22회사회복지사
clean = lambda s: re.sub(r"\s+", " ", re.sub(r"<br>|\[\[|\]\]", " ", s)).strip()


def hook_title(ep):
    for sc in ep["scenes"]:
        if sc["type"] == "hook":
            return clean(sc.get("headline") or " ".join(sc.get("words", [])))
    return ""


def answer_text(ep):
    if ep.get("answer"):
        return ep["answer"]
    for sc in ep["scenes"]:
        if sc["type"] == "cta" and sc.get("reveal"):
            ln = ep["lines"][sc["reveal"]["line"]]
            return clean(ln.get("cap", ln["say"]))
    return "정답 확인 필요 (대본에 reveal 또는 answer가 없어요)"


subject = sys.argv[1] if len(sys.argv) > 1 else "사회복지"
subj_tag = sys.argv[2] if len(sys.argv) > 2 else ""
out = sys.argv[3] if len(sys.argv) > 3 else None
extra = os.environ.get("HASHTAGS", "")
tags = " ".join(x for x in [COMMON, EXAM_TAG, subj_tag, extra] if x)
lines = [f"# {subject} 캡션 · 해시태그 · 고정 댓글 초안", "", "## 해시태그 (캡션 맨 아래에 복사)", tags, ""]
for n, ep in sorted(EPS.items()):
    title = ep.get("caption") or hook_title(ep)
    lines += [f"## EP{n} · {title}", "", "**캡션**",
              f"{title}! {EXAM_NAME} 기출 응용으로 헷갈리는 개념을 이야기로 정리했어요.",
              "정답은 고정 댓글에 있어요. 먼저 댓글로 맞혀 보세요 👇",
              "저장해 두고 시험 전날 다시 보면 헷갈림 끝!", "", tags, "",
              "**고정 댓글**", answer_text(ep), ""]
text = "\n".join(lines)
if out:
    open(out, "w", encoding="utf-8").write(text); print("wrote", out)
else:
    print(text)
