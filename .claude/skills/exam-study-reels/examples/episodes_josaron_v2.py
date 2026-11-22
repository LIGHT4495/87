# -*- coding: utf-8 -*-
# 사회복지조사론 — v2 엔진, 라떼 크림 종이 + 청록 포인트 + 거북이 박사 (EP1은 새로 구성, EP2~9는 v1 대본 변환)
import episodes_josaron as V1
from v1_to_v2 import convert, RED, GRN, CTA_HEAD

ANS = {
    2: (0, "정답은 패널 연구예요!", "정답은 패널 연구예요!"),
    3: (1, "정답은 비확률표집이에요!", "정답은 비확률표집이에요!"),
    4: (0, "정답은 일종 오류예요!", "정답은 1종 오류예요!"),
    5: (0, "정답은 등간척도예요!", "정답은 등간척도예요!"),
    6: (0, "정답은 내적타당도예요!", "정답은 내적타당도예요!"),
    7: (0, "정답은 비동일 통제집단이에요!", "정답은 비동일 통제집단이에요!"),
    9: (0, "정답은 델파이예요!", "정답은 델파이예요!"),
}
EPS = convert(V1.EPS, ANS)

EPS[1] = dict(
    music=(100, 0, 41),
    lines=[
        dict(say="일관되게 틀리는 사람, 신뢰도는 높을까요?"),
        dict(say="조사리 마을의 궁수 일관이는, 쏠 때마다 항상 같은 자리에 맞혀요."),
        dict(say="그런데 그 자리는, 과녁의 중심이 아니에요."),
        dict(say="그래서 신뢰도는 높지만, 타당도는 낮은 거죠."),
        dict(say="신뢰도는 일관성, 타당도는 정확성이에요."),
        dict(say="반면 정확이는, 재려는 중심을 정확히 맞혀요."),
        dict(say="신뢰도는 타당도의 필요조건일 뿐, 충분조건은 아니에요."),
        dict(say="그래서 신뢰도가 높아지면 타당도도 높아진다는 설명은, 틀린 거예요."),
        dict(say="그럼 요인분석은, 신뢰도일까요 타당도일까요?"),
        dict(say="정답은 타당도예요! 구성타당도를 확인해요.", pause=2.3),
    ],
    scenes=[
        dict(type="hook", lines=[0], headline="신뢰도<br>[[VS 타당도]]"),
        dict(type="versus", lines=[1, 2, 3, 4], headline="신뢰도<br>[[VS]] 타당도",
             left=dict(line=1, title="신뢰도", items=["일관성", "늘 같은 자리", "일관이 궁수"]),
             right=dict(line=4, title="타당도", items=["정확성", "중심을 맞힘", "정확이 궁수"])),
        dict(type="cards", lines=[5, 6], headline="[[필요조건 vs 충분조건]]", rows=[
            dict(line=5, title="타당도 높음", desc="재려는 것을 정확히 재요"),
            dict(line=6, title="신뢰도 높음", desc="타당도의 필요조건일 뿐"),
        ]),
        dict(type="exam", lines=[7], headline="이 설명,<br>[[맞을까요?]]", tag="제24회 기출 응용 · 조사론",
             html="신뢰도가 높아지면<br>[[타당도도 높아진다]]", stamp="틀림!", stamp_color=RED, stamp_line=7, stamp_frac=0.85),
        dict(type="cta", lines=[8, 9], headline=CTA_HEAD, q="요인분석은?", buttons=[("신뢰도?", 0), ("타당도?", 1)], reveal=dict(line=9, answer=1)),
    ],
)
EPS = dict(sorted(EPS.items()))

# v2 폭에 맞춘 문구 조정
for _sc in EPS[8]["scenes"]:
    for _r in _sc.get("rows", []):
        _r["desc"] = _r["desc"].replace("결혼식 · 민요 · 교통사고 · 요리책", "결혼식 · 민요 · 요리책 등")
