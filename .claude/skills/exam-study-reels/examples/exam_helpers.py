# -*- coding: utf-8 -*-
# 에피소드 대본 작성 도우미: hook / exam / cta 장면을 한 줄로 만든다.
RED = "#e8431a"; GRN = "#12a37f"
CTA_HEAD = "[[댓글]]로 정답을<br>맞혀 보세요!"
Q = "이 설명,<br>[[맞을까요?]]"


def make(tag):
    def hook(i, h):
        return dict(type="hook", lines=[i], headline=h)

    def exam(i, q, html, stamp, ok=False, pre=0, h=None):
        return dict(type="exam", lines=list(range(i - pre, i + 1)), headline=h or Q, tag=f"{tag} · {q}번", html=html,
                    stamp=stamp, stamp_color=GRN if ok else RED, stamp_line=i, stamp_frac=0.85)

    def cta(a, b, q, buttons, ans):
        return dict(type="cta", lines=[a, b], headline=CTA_HEAD, q=q, buttons=[(t, k) for k, t in enumerate(buttons)],
                    reveal=dict(line=b, answer=ans))
    return hook, exam, cta
