# -*- coding: utf-8 -*-
# v1(카드 테마) 대본을 v2(종이 모션) 스키마로 변환하고, 정답 공개(카운트다운)를 붙인다.
import copy
RED = "#e8431a"; GRN = "#12a37f"
CTA_HEAD = "[[댓글]]로 정답을<br>맞혀 보세요!"


def convert(eps, answers):
    """answers: {ep: (정답 버튼 인덱스, 읽는 말, 자막)} — 없으면 정답 공개 없이 변환."""
    out = {}
    for n, ep in eps.items():
        e = copy.deepcopy(ep)
        sc2 = []
        for sc in e["scenes"]:
            t = sc["type"]
            if t == "hook":
                words = " · ".join(sc["words"]) if sc.get("joiner", "") == "" else f' {sc["joiner"]} '.join(sc["words"])
                sc2.append(dict(type="hook", lines=sc["lines"], headline=f'{sc.get("sub", "")}<br>[[{words}]]'))
            elif t == "cards":
                rows = [{k: v for k, v in r.items() if k != "color"} for r in sc["rows"]]
                sc2.append(dict(type="cards", lines=sc["lines"], headline=f'[[{sc.get("header", "핵심 정리")}]]', rows=rows))
            elif t == "exam":
                ok = sc["stamp_color"] == "T"
                sc2.append(dict(type="exam", lines=sc["lines"], headline="이 사례,<br>[[어떤 걸까요?]]" if ok else "이 설명,<br>[[맞을까요?]]",
                                tag=sc["tag"], html=sc["html"], stamp=sc["stamp"], stamp_color=GRN if ok else RED,
                                stamp_line=sc["stamp_line"], stamp_frac=sc["stamp_frac"]))
            elif t == "cta":
                buttons = [(b[0], i) for i, b in enumerate(sc["buttons"])]
                cta = dict(type="cta", lines=sc["lines"], headline=CTA_HEAD, q=sc["q"], buttons=buttons)
                if n in answers:
                    idx, say, cap = answers[n]
                    li = len(e["lines"])
                    e["lines"] = e["lines"] + [dict(say=say, cap=cap, pause=2.3)]
                    cta["lines"] = sc["lines"] + [li]
                    cta["reveal"] = dict(line=li, answer=idx)
                sc2.append(cta)
        e["scenes"] = sc2
        out[n] = e
    return out
