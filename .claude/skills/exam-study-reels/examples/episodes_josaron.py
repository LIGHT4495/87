# -*- coding: utf-8 -*-
# Episode specs for 「조사리 마을 사건일지」 EP.2 - EP.9
# line: say (spoken, TTS) / cap (caption; defaults to say)
# scene types: hook, cards, exam, cta
P = "#6c4df6"; T = "#0e9488"; C = "#e0344f"; A = "#c26a0e"

EPS = {}

# ---------------------------------------------------------------- EP2
EPS[2] = dict(
    music=(104, 1, 11),
    lines=[
        dict(say="패널, 코호트, 경향연구, 뭐가 다를까요?"),
        dict(say="종단연구는, 시간을 두고 같은 주제를 여러 번 조사하는 방법이에요."),
        dict(say="패널 연구는, 매번 같은 사람에게 다시 묻는 연구예요."),
        dict(say="코호트 연구는, 같은 시기에 같은 경험을 한 집단을 조사해요."),
        dict(say="경향연구는, 전체 모집단의 변화를 보고 표본도 매번 새로 뽑아요."),
        dict(say="기출 사례예요. 십 대 자녀 집단에서, 오 년마다 새 표본을 뽑아 같은 설문을 했죠.",
             cap="기출 사례예요. 10대 자녀 집단에서, 5년마다 새 표본을 뽑아 같은 설문을 했죠."),
        dict(say="같은 사람을 따라간 게 아니니 패널이 아니고, 특정 집단이라서 코호트 연구예요."),
        dict(say="그럼 표본 탈락이 문제되는 연구는, 패널일까요 코호트일까요?"),
    ],
    scenes=[
        dict(type="hook", lines=[0], sub="종단연구 3총사", words=["패널", "코호트", "경향"], joiner=""),
        dict(type="cards", lines=[1, 2, 3, 4], header="종단연구 3총사", rows=[
            dict(line=2, color=P, title="패널 연구", desc="같은 사람을<br>계속 추적해요"),
            dict(line=3, color=T, title="코호트 연구", desc="같은 경험을 한 집단의 변화<br>표본은 매번 새로 가능"),
            dict(line=4, color=C, title="경향연구", desc="전체 모집단의 변화<br>표본은 매번 새로"),
        ]),
        dict(type="exam", lines=[5, 6], tag="제24회 기출 응용 · 조사론 · 28번",
             html="[[10대 자녀 집단]]에서<br>5년마다 새 표본을 뽑아<br>같은 설문으로 조사", stamp="코호트 연구!", stamp_color=T, stamp_line=6, stamp_frac=0.55),
        dict(type="cta", lines=[7], q="표본 탈락이 문제인 건?", buttons=[("패널?", P), ("코호트?", T)], hint="정답은 댓글로 남겨 주세요!"),
    ],
)

# ---------------------------------------------------------------- EP3
EPS[3] = dict(
    music=(108, 2, 12),
    lines=[
        dict(say="확률표집과 비확률표집, 어떻게 구분할까요?"),
        dict(say="확률표집은, 모집단의 누가 뽑힐지 확률을 알 수 있는 방법이에요."),
        dict(say="비확률표집은, 할당, 눈덩이, 임의, 유의표집이 있어요."),
        dict(say="특히 할당표집은 이름과 달리 비확률표집이에요. 확률표집이라는 설명은 틀렸죠."),
        dict(say="표본이 커질수록, 표집오차는 줄어들어요."),
        dict(say="신뢰수준을 구십오에서 구십구 퍼센트로 높이면, 표본도 더 커져야 해요.",
             cap="신뢰수준을 95%에서 99%로 높이면, 표본도 더 커져야 해요."),
        dict(say="하지만 모수와 통계치의 유사성이 표본크기와 무관하다는 말은, 틀려요."),
        dict(say="그럼 눈덩이표집은, 확률표집일까요 비확률표집일까요?"),
    ],
    scenes=[
        dict(type="hook", lines=[0], sub="표집 · 표본크기", words=["확률표집", "비확률표집"], joiner="VS"),
        dict(type="cards", lines=[1, 2], header="표집 방법", rows=[
            dict(line=1, color=P, title="확률표집", desc="뽑힐 확률을 알 수 있어요<br>단순무작위 · 체계적 · 층화 · 군집"),
            dict(line=2, color=T, title="비확률표집", desc="뽑힐 확률을 알 수 없어요<br>할당 · 눈덩이 · 임의 · 유의"),
        ]),
        dict(type="exam", lines=[3], tag="제24회 기출 응용 · 조사론 · 39번",
             html="[[할당표집]]은<br>확률표집이다.", stamp="틀림!", stamp_color=C, stamp_line=3, stamp_frac=0.72),
        dict(type="cards", lines=[4, 5, 6], header="표본크기", rows=[
            dict(line=4, color=T, title="표본이 클수록", desc="표집오차는 줄어요", mark="o"),
            dict(line=5, color=P, title="신뢰수준 95→99%", desc="표본을 늘려야 해요", mark="o"),
            dict(line=6, color=C, title="모수와 통계치", desc="유사성은 표본크기와 무관?", mark="x"),
        ]),
        dict(type="cta", lines=[7], q="눈덩이표집은?", buttons=[("확률?", P), ("비확률?", T)], hint="정답은 댓글로 남겨 주세요!"),
    ],
)

# ---------------------------------------------------------------- EP4
EPS[4] = dict(
    music=(102, 3, 13),
    lines=[
        dict(say="일종 오류와 이종 오류, 어떻게 구분할까요?", cap="1종 오류와 2종 오류, 어떻게 구분할까요?"),
        dict(say="판사 부엉이의 재판에서, 영가설은 피고는 무죄라는 가정이에요."),
        dict(say="무죄인 사람에게 유죄를 내리면 일종 오류, 참인 영가설을 기각한 거예요.",
             cap="무죄인 사람에게 유죄를 내리면 1종 오류, 참인 영가설을 기각한 거예요."),
        dict(say="유죄인 사람을 무죄로 풀어 주면 이종 오류, 거짓인 영가설을 기각하지 못한 거죠.",
             cap="유죄인 사람을 무죄로 풀어 주면 2종 오류, 거짓인 영가설을 기각하지 못한 거죠."),
        dict(say="그리고 검증력은, 거짓인 영가설을 제대로 기각할 확률이에요."),
        dict(say="그래서 검증력이 영가설이 참일 때 기각할 확률이라는 설명은, 틀렸어요."),
        dict(say="그럼 신뢰수준을 높이면 줄어드는 건, 일종 오류일까요 이종 오류일까요?",
             cap="그럼 신뢰수준을 높이면 줄어드는 건, 1종 오류일까요 2종 오류일까요?"),
    ],
    scenes=[
        dict(type="hook", lines=[0], sub="가설 검증", words=["1종 오류", "2종 오류"], joiner="VS"),
        dict(type="cards", lines=[1, 2, 3, 4], header="판사 부엉이의 재판", rows=[
            dict(line=2, color=C, title="1종 오류", desc="무죄인데 유죄 판결<br>참인 영가설을 기각"),
            dict(line=3, color=P, title="2종 오류", desc="유죄인데 무죄 판결<br>거짓 영가설을 못 기각"),
            dict(line=4, color=T, title="검증력", desc="영가설이 거짓일 때<br>제대로 기각할 확률"),
        ]),
        dict(type="exam", lines=[5], tag="제24회 기출 응용 · 조사론 · 31번",
             html="검증력은 [[영가설이 참일 때]]<br>기각할 확률이다.", stamp="틀림!", stamp_color=C, stamp_line=5, stamp_frac=0.7),
        dict(type="cta", lines=[6], q="신뢰수준을 높이면?", buttons=[("1종?", P), ("2종?", C)], hint="정답은 댓글로 남겨 주세요!"),
    ],
)

# ---------------------------------------------------------------- EP5
EPS[5] = dict(
    music=(110, 0, 14),
    lines=[
        dict(say="명목, 서열, 등간, 비율, 헷갈리지 않는 방법이 있어요!"),
        dict(say="명목은 이름표, 서열은 순위만 알려 줘요."),
        dict(say="등간은 간격이 같고, 비율은 절대영점이 있어요."),
        dict(say="기출 사례의 임금은 비율, 성별은 명목, 교육수준은 서열이에요."),
        dict(say="보가더스와 거트만은 누적척도, 리커트는 총합평정 방식이에요."),
        dict(say="의미차별척도는 유사가 아니라, 반대 의미의 형용사 한 쌍을 써요."),
        dict(say="그럼 섭씨 온도는, 등간일까요 비율일까요?"),
    ],
    scenes=[
        dict(type="hook", lines=[0], sub="측정수준 · 척도", words=["명목", "서열", "등간", "비율"], joiner=""),
        dict(type="cards", lines=[1, 2], header="측정수준 4계단", rows=[
            dict(line=1, color=P, title="명목", desc="이름표 · 분류만 (성별)"),
            dict(line=1, color=T, title="서열", desc="순서 · 순위 (학력, 석차)"),
            dict(line=2, color=C, title="등간", desc="간격이 같음 (섭씨 온도)"),
            dict(line=2, color=A, title="비율", desc="절대영점 있음 (임금, 나이)"),
        ]),
        dict(type="exam", lines=[3], tag="제24회 기출 응용 · 조사론 · 34번",
             html="임금 → [[비율]]<br>성별 → [[명목]]<br>교육수준 → [[서열]]", stamp="정답!", stamp_color=T, stamp_line=3, stamp_frac=0.8),
        dict(type="cards", lines=[4, 5], header="척도 4총사", rows=[
            dict(line=4, color=P, title="보가더스척도", desc="사회적 거리 · 누적척도"),
            dict(line=4, color=T, title="거트만척도", desc="문항이 서열적 · 누적척도"),
            dict(line=4, color=C, title="리커트척도", desc="총합평정 · 척도 개발에 용이"),
            dict(line=5, color=A, title="의미차별척도", desc="반대 의미 형용사 한 쌍"),
        ]),
        dict(type="cta", lines=[6], q="섭씨 온도는?", buttons=[("등간?", P), ("비율?", T)], hint="정답은 댓글로 남겨 주세요!"),
    ],
)

# ---------------------------------------------------------------- EP6
EPS[6] = dict(
    music=(106, 1, 15),
    lines=[
        dict(say="내적타당도와 외적타당도, 헷갈리지 않는 방법!"),
        dict(say="내적타당도는, 결과가 독립변수 때문이라고 확신하는 정도예요."),
        dict(say="외적타당도는, 결과를 다른 대상과 상황에 일반화할 수 있는 정도예요."),
        dict(say="우연한 외부 사건이나 중도 탈락은, 내적타당도를 해쳐요."),
        dict(say="표본의 대표성이 낮으면, 외적타당도가 떨어져요."),
        dict(say="그래서 내적이 높으면 외적도 높다는 말은 틀려요. 한쪽을 높이면 다른 쪽이 낮아지기 쉬워요."),
        dict(say="그럼 실험 중에 참가자가 빠지는 탈락은, 내적일까요 외적일까요?"),
    ],
    scenes=[
        dict(type="hook", lines=[0], sub="조사설계", words=["내적타당도", "외적타당도"], joiner="VS"),
        dict(type="cards", lines=[1, 2, 3, 4], header="타당도 4장면", rows=[
            dict(line=1, color=P, title="내적타당도", desc="독립변수 때문이라 확신하는 정도"),
            dict(line=2, color=T, title="외적타당도", desc="다른 대상·상황에 일반화하는 정도"),
            dict(line=3, color=C, title="내적 저해요인", desc="우연한 사건 · 중도 탈락"),
            dict(line=4, color=A, title="외적 저해요인", desc="표본의 대표성이 낮을 때"),
        ]),
        dict(type="exam", lines=[5], tag="제24회 기출 응용 · 조사론 · 45번",
             html="[[내적타당도가 높으면]]<br>외적타당도도 높다.", stamp="틀림!", stamp_color=C, stamp_line=5, stamp_frac=0.45),
        dict(type="cta", lines=[6], q="참가자 탈락은?", buttons=[("내적?", P), ("외적?", T)], hint="정답은 댓글로 남겨 주세요!"),
    ],
)

# ---------------------------------------------------------------- EP7
EPS[7] = dict(
    music=(104, 2, 16),
    lines=[
        dict(say="실험설계와 단일사례설계, 어떻게 다를까요?"),
        dict(say="무작위 배정 없이 두 집단을 사전, 사후로 비교하면, 비동일 통제집단 설계예요."),
        dict(say="사후검사만 하는 정태적 집단비교는, 타당도가 낮아요."),
        dict(say="솔로몬 사 집단은, 두 가지 통제집단 설계를 합친 거예요.", cap="솔로몬 4집단은, 두 가지 통제집단 설계를 합친 거예요."),
        dict(say="단일사례설계에서, 기초선이 안정적이면 평균을 비교해요."),
        dict(say="불안정하면, 변화의 기울기까지 보는 경향선 접근을 써요."),
        dict(say="기초선을 만들 시간이 없을 땐, 비에이비 설계가 적합해요.", cap="기초선을 만들 시간이 없을 땐, BAB설계가 적합해요."),
        dict(say="그래서 평균비교가 불안정한 기초선을 기울기까지 분석한다는 설명은, 틀렸어요."),
        dict(say="그럼 무작위 배정이 없는 설계는, 비동일 통제집단일까요 솔로몬일까요?"),
    ],
    scenes=[
        dict(type="hook", lines=[0], sub="조사설계", words=["실험설계", "단일사례설계"], joiner="VS"),
        dict(type="cards", lines=[1, 2, 3], header="집단 실험설계", rows=[
            dict(line=1, color=P, title="비동일 통제집단", desc="무작위 배정 없는 비교집단<br>사전 · 사후검사"),
            dict(line=2, color=C, title="정태적 집단비교", desc="사후검사만<br>내적·외적 타당도 낮음"),
            dict(line=3, color=T, title="솔로몬 4집단", desc="통제집단 사전사후 설계와<br>사후 설계를 합침"),
        ]),
        dict(type="cards", lines=[4, 5, 6], header="단일사례설계", rows=[
            dict(line=4, color=T, title="평균비교", desc="기초선이 안정적일 때"),
            dict(line=5, color=P, title="경향선 접근", desc="불안정할 때 기울기까지 분석"),
            dict(line=6, color=A, title="BAB설계", desc="기초선 만들 시간이 없을 때"),
        ]),
        dict(type="exam", lines=[7], tag="제24회 기출 응용 · 조사론 · 47번",
             html="[[평균비교]]는<br>기초선이 불안정할 때<br>기울기까지 고려한다.", stamp="틀림!", stamp_color=C, stamp_line=7, stamp_frac=0.75),
        dict(type="cta", lines=[8], q="무작위 배정이 없는 건?", buttons=[("비동일?", P), ("솔로몬?", T)], hint="정답은 댓글로 남겨 주세요!"),
    ],
)

# ---------------------------------------------------------------- EP8
EPS[8] = dict(
    music=(100, 3, 17),
    lines=[
        dict(say="근거이론과 문화기술지, 질적연구의 대표 주자예요!"),
        dict(say="근거이론은, 모은 자료에서 이론을 만들어요. 개방, 축, 선택 코딩이 대표 기법이죠."),
        dict(say="문화기술지는, 한 집단의 생활양식을 깊이 이해하는 방법이에요."),
        dict(say="그래서 문화기술지가 개방, 축, 선택코딩을 쓴다는 설명은 틀렸어요. 그건 근거이론이에요."),
        dict(say="또 하나, 분석단위 중 사회적 가공물은, 결혼식, 민요, 교통사고, 요리책 같은 것들이에요."),
        dict(say="하지만 유권자 집단은, 가공물이 아니라 집단이에요."),
        dict(say="그럼 참여관찰에서, 연구자의 편향은 통제될까요?"),
    ],
    scenes=[
        dict(type="hook", lines=[0], sub="질적연구", words=["근거이론", "문화기술지"], joiner="VS"),
        dict(type="cards", lines=[1, 2], header="질적연구 방법", rows=[
            dict(line=1, color=P, title="근거이론", desc="자료에서 이론 생성<br>개방 · 축 · 선택 코딩"),
            dict(line=2, color=T, title="문화기술지", desc="집단의 생활양식 이해<br>문화인류학과 관계 깊음"),
        ]),
        dict(type="exam", lines=[3], tag="제24회 기출 응용 · 조사론 · 50번",
             html="[[문화기술지]]는 개방코딩,<br>축코딩, 선택코딩으로<br>인과조건을 발견한다.", stamp="틀림!", stamp_color=C, stamp_line=3, stamp_frac=0.6),
        dict(type="cards", lines=[4, 5], header="분석단위", rows=[
            dict(line=4, color=T, title="사회적 가공물", desc="결혼식 · 민요 · 교통사고 · 요리책", mark="o"),
            dict(line=5, color=C, title="유권자 집단", desc="가공물이 아니라 집단이에요", mark="x"),
        ]),
        dict(type="cta", lines=[6], q="참여관찰의 편향은?", buttons=[("통제됨?", P), ("개입됨?", T)], hint="정답은 댓글로 남겨 주세요!"),
    ],
)

# ---------------------------------------------------------------- EP9
EPS[9] = dict(
    music=(108, 1, 18),
    lines=[
        dict(say="우편설문, 대면면접, 델파이, 초점집단면접, 한 번에 정리해요!"),
        dict(say="우편설문은, 비용이 적고 익명성이 높지만 응답률이 낮아요."),
        dict(say="대면면접은, 응답률이 높고 결측치가 적지만 비용이 많이 들어요."),
        dict(say="그래서 대면면접이 비용을 절감한다는 설명은, 틀렸어요."),
        dict(say="델파이는, 익명의 전문가에게 설문을 여러 번 반복해 합의를 얻어요."),
        dict(say="초점집단면접은, 소집단이 토론하는 방식이라 일반화가 어려워요."),
        dict(say="그럼 패널의 후광효과를 막기 쉬운 건, 델파이일까요 초점집단면접일까요?"),
    ],
    scenes=[
        dict(type="hook", lines=[0], sub="자료수집 방법", words=["우편설문", "대면면접", "델파이", "FGI"], joiner=""),
        dict(type="cards", lines=[1, 2], header="우편설문 vs 대면면접", rows=[
            dict(line=1, color=P, title="우편설문", desc="비용 저렴 · 익명성 보장<br>응답률 낮음"),
            dict(line=2, color=T, title="대면면접", desc="응답률 높음 · 결측치 적음<br>비용이 많이 듦"),
        ]),
        dict(type="exam", lines=[3], tag="제24회 기출 응용 · 조사론 · 40번",
             html="[[대면면접]]은 우편설문보다<br>비용이 절감된다.", stamp="틀림!", stamp_color=C, stamp_line=3, stamp_frac=0.6),
        dict(type="cards", lines=[4, 5], header="델파이 vs 초점집단면접", rows=[
            dict(line=4, color=A, title="델파이", desc="익명 전문가에게 반복 설문<br>합의 도출"),
            dict(line=5, color=C, title="초점집단면접", desc="소집단 토론으로 자료 수집<br>일반화는 어려움"),
        ]),
        dict(type="cta", lines=[6], q="후광효과 방지는?", buttons=[("델파이?", P), ("FGI?", T)], hint="정답은 댓글로 남겨 주세요!"),
    ],
)
