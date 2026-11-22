# -*- coding: utf-8 -*-
# 시리즈 한눈에 보기 — 8과목 × 8캐릭터 소개 릴스 (v2 엔진, cast/subject 장면)
S = [  # 과목, 캐릭터, 종이, 포인트색, 한 줄 소개, 교시
    ("사회복지조사론", "turtle", "paper_sand.jpg", "#0f8a8a", "1교시"),
    ("인간행동과 사회환경", "rabbit", "paper_sky.jpg", "#d9487a", "1교시"),
    ("사회복지실천론", "bear", "paper.jpg", "#8a5530", "2교시"),
    ("사회복지실천기술론", "cat", "paper_pink.jpg", "#dc480e", "2교시"),
    ("지역사회복지론", "dog", "paper_lavender.jpg", "#dc480e", "2교시"),
    ("사회복지정책론", "owl", "paper_yellow.jpg", "#1f3a68", "3교시"),
    ("사회복지행정론", "beaver", "paper_aqua.jpg", "#e0523f", "3교시"),
    ("사회복지법제론", "penguin", "paper_peach.jpg", "#1d5c4a", "3교시"),
]
NAMES = ["조사론", "인간행동", "실천론", "기술론", "지역복지", "정책론", "행정론", "법제론"]
ITEMS = [dict(char=c, accent=a, name=NAMES[i]) for i, (_, c, _, a, _) in enumerate(S)]
LINES = [
    "사회복지사 일 급 기출, 여덟 과목을 여덟 친구와 함께해요!",
    "조사론은 느긋한 거북이 박사와, 통계도 천천히 이해해요.",
    "인간행동은 통통 튀는 토끼와, 발달 이론을 쏙쏙 외워요.",
    "실천론은 포근한 곰과, 가치와 윤리를 차근차근 정리해요.",
    "실천기술론은 안경 쓴 고양이와, 기법을 짝지어 봐요.",
    "지역사회복지론은 꼬리 흔드는 강아지와, 이론을 사례로 맞혀요.",
    "정책론은 올빼미 박사와, 노선도처럼 흐름을 따라가요.",
    "행정론은 씩씩한 비버 팀장과, 결재 체크리스트로 점검해요.",
    "법제론은 판사 펭귄과, 조문을 판결로 정리해요.",
    "저장해 두고, 시험 전날 다시 만나요!",
]
CAPS = {0: "사회복지사 1급 기출, 여덟 과목을 여덟 친구와 함께해요!"}
EPS = {1: dict(
    music=(100, 1, 61),
    lines=[dict(say=t, **({"cap": CAPS[i]} if i in CAPS else {})) for i, t in enumerate(LINES)],
    scenes=[dict(type="cast", lines=[0], headline="8과목<br>[[한눈에 보기]]", items=ITEMS, paper="paper_sand.jpg")]
    + [dict(type="subject", lines=[i + 1], headline=f"{S[i][4]}<br>[[{S[i][0]}]]", char=S[i][1], paper=S[i][2], accent=S[i][3])
       for i in range(8)]
    + [dict(type="cast", lines=[9], headline="저장하고<br>[[시험 전날 복습!]]", items=ITEMS, paper="paper_sand.jpg")],
)}
