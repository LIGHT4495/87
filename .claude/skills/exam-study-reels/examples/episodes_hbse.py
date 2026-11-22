# -*- coding: utf-8 -*-
# 「성장 마을 사건일지」 - 인간행동과 사회환경 (제24회 1~25번)
P = "#6c4df6"; T = "#0e9488"; C = "#e0344f"; A = "#c26a0e"
EPS = {}

# ---------------------------------------------------------------- EP1 성숙·성장·발달 (1,2번)
EPS[1] = dict(
    music=(104, 0, 21),
    lines=[
        dict(say="성숙, 성장, 발달, 이름은 비슷한데 뭐가 다를까요?"),
        dict(say="성숙은, 유전적인 내적 요인으로 정해진 시기에 일어나는 변화예요."),
        dict(say="성장은, 키와 몸무게처럼 눈에 보이는 양적 변화예요."),
        dict(say="발달은, 분화와 통합을 반복하며 이루어지는 변화예요."),
        dict(say="그래서 성장이 유전적, 내적 요인에 의한 변화라는 설명은 틀렸어요. 그건 성숙이에요."),
        dict(say="발달이론은 적응과 부적응을 판단하는 기준이 되고, 클라이언트 사정에도 유용해요."),
        dict(say="하지만 사회환경보다 생물학적 요소를 강조한다는 설명은, 틀려요."),
        dict(say="그럼 소근육과 대근육 중에, 먼저 발달하는 건 무엇일까요?"),
    ],
    scenes=[
        dict(type="hook", lines=[0], sub="인간발달의 기본", words=["성숙", "성장", "발달"], joiner=""),
        dict(type="cards", lines=[1, 2, 3], header="발달의 세 얼굴", rows=[
            dict(line=1, color=P, title="성숙", desc="유전적 · 내적 요인<br>정해진 시기의 변화"),
            dict(line=2, color=T, title="성장", desc="키 · 몸무게 같은<br>양적 변화"),
            dict(line=3, color=C, title="발달", desc="분화와 통합을<br>반복하는 변화"),
        ]),
        dict(type="exam", lines=[4], tag="제24회 기출 응용 · 인간행동 · 1번",
             html="[[성장]]은 유전적, 내적 요인으로<br>특정 시기에 일어나는<br>변화이다.", stamp="틀림!", stamp_color=C, stamp_line=4, stamp_frac=0.55),
        dict(type="cards", lines=[5, 6], header="발달이론과 사회복지실천", rows=[
            dict(line=5, color=T, title="판단 기준 제공", desc="적응 · 부적응 구분", mark="o"),
            dict(line=5, color=P, title="클라이언트 사정", desc="사정에 유용해요", mark="o"),
            dict(line=6, color=C, title="생물학적 요소 강조", desc="사회환경보다 더 중요?", mark="x"),
        ]),
        dict(type="cta", lines=[7], q="먼저 발달하는 근육은?", buttons=[("소근육?", P), ("대근육?", T)], hint="정답은 댓글로 남겨 주세요!"),
    ],
)

# ---------------------------------------------------------------- EP2 이상행동·방어기제 (3,4번)
EPS[2] = dict(
    music=(100, 1, 22),
    lines=[
        dict(say="내 마음을 지키는 방어기제, 헷갈리지 않는 방법이 있어요!"),
        dict(say="먼저 이상행동이에요. 진단분류체계로 DSM이 유일하다는 설명은, 틀렸어요. 국제질병분류도 있어요."),
        dict(say="억압은, 받아들일 수 없는 생각이나 충동을 무의식 속으로 밀어 넣는 거예요."),
        dict(say="부정은, 고통스러운 현실을 아예 인정하지 않는 거예요."),
        dict(say="투사는, 내 충동이나 감정을 다른 사람 탓으로 돌리는 거예요."),
        dict(say="기출 사례예요. 고통스러운 일을 잊는 기억상실이나, 하기 싫은 과제를 깜빡 잊는 건, 억압이에요."),
        dict(say="승화는, 충동을 사회적으로 인정받는 활동으로 바꾸는 거예요."),
        dict(say="반동형성은, 속마음과 정반대로 행동하는 거예요."),
        dict(say="그럼 고통스러운 현실을 아예 인정하지 않는 건, 부정일까요 억압일까요?"),
    ],
    scenes=[
        dict(type="hook", lines=[0], sub="방어기제", words=["억압", "부정", "투사"], joiner=""),
        dict(type="exam", lines=[1], tag="제24회 기출 응용 · 인간행동 · 3번",
             html="진단분류체계는<br>[[DSM이 유일]]하다.", stamp="틀림!", stamp_color=C, stamp_line=1, stamp_frac=0.7),
        dict(type="cards", lines=[2, 3, 4], header="방어기제 ①", rows=[
            dict(line=2, color=P, title="억압", desc="받아들일 수 없는 충동을<br>무의식 속으로 추방"),
            dict(line=3, color=T, title="부정", desc="고통스러운 현실을<br>인정하지 않음"),
            dict(line=4, color=C, title="투사", desc="내 충동을<br>남의 탓으로 돌림"),
        ]),
        dict(type="exam", lines=[5], tag="제24회 기출 응용 · 인간행동 · 4번",
             html="고통스러운 일을 잊는<br>[[기억상실]], 하기 싫은<br>과제를 깜빡 잊음", stamp="억압!", stamp_color=T, stamp_line=5, stamp_frac=0.8),
        dict(type="cards", lines=[6, 7], header="방어기제 ②", rows=[
            dict(line=6, color=A, title="승화", desc="충동을 사회적으로<br>인정받는 활동으로"),
            dict(line=7, color=P, title="반동형성", desc="속마음과<br>정반대로 행동"),
        ]),
        dict(type="cta", lines=[8], q="현실을 인정하지 않는 건?", buttons=[("부정?", P), ("억압?", T)], hint="정답은 댓글로 남겨 주세요!"),
    ],
)

# ---------------------------------------------------------------- EP3 에릭슨 (5,21번)
EPS[3] = dict(
    music=(108, 2, 23),
    lines=[
        dict(say="에릭슨의 여덟 단계, 짝꿍을 기억해요!", cap="에릭슨의 8단계, 짝꿍을 기억해요!"),
        dict(say="영아기는 신뢰감 대 불신감, 걸음마기는 자율성 대 수치심과 의심이에요."),
        dict(say="삼 세에서 육 세 유아기는 주도성 대 죄책감, 학령기는 근면성 대 열등감이에요.", cap="3~6세 유아기는 주도성 대 죄책감, 학령기는 근면성 대 열등감이에요."),
        dict(say="청소년기는 정체감 대 역할혼미, 성인 초기는 친밀감 대 고립감이에요."),
        dict(say="중년기는 생산성 대 침체, 노년기는 자아통합 대 절망이에요."),
        dict(say="기출에서는 친밀감 대 역할혼미로 짝지었는데, 친밀감의 짝은 고립감이에요. 틀린 연결이죠."),
        dict(say="그럼 기본적 신뢰감을 형성하는 시기는, 영아기일까요 유아기일까요?"),
    ],
    scenes=[
        dict(type="hook", lines=[0], sub="심리사회적 발달", words=["에릭슨", "8단계"], joiner=""),
        dict(type="cards", lines=[1, 2], header="에릭슨 1~4단계", rows=[
            dict(line=1, color=P, title="영아기", desc="신뢰감 대 불신감"),
            dict(line=1, color=T, title="걸음마기", desc="자율성 대 수치심·의심"),
            dict(line=2, color=C, title="유아기 (3~6세)", desc="주도성 대 죄책감"),
            dict(line=2, color=A, title="학령기", desc="근면성 대 열등감"),
        ]),
        dict(type="cards", lines=[3, 4], header="에릭슨 5~8단계", rows=[
            dict(line=3, color=P, title="청소년기", desc="정체감 대 역할혼미"),
            dict(line=3, color=T, title="성인 초기", desc="친밀감 대 고립감"),
            dict(line=4, color=C, title="중년기", desc="생산성 대 침체"),
            dict(line=4, color=A, title="노년기", desc="자아통합 대 절망"),
        ]),
        dict(type="exam", lines=[5], tag="제24회 기출 응용 · 인간행동 · 5번",
             html="[[친밀감]] 대 [[역할혼미]]", stamp="틀림!", stamp_color=C, stamp_line=5, stamp_frac=0.75),
        dict(type="cta", lines=[6], q="기본적 신뢰감은?", buttons=[("영아기?", P), ("유아기?", T)], hint="정답은 댓글로 남겨 주세요!"),
    ],
)

# ---------------------------------------------------------------- EP4 프로이트·융·아들러·로저스 (6,9번)
EPS[4] = dict(
    music=(102, 3, 24),
    lines=[
        dict(say="프로이트, 융, 아들러, 이론이 자꾸 섞이죠?"),
        dict(say="프로이트는 무의식과 리비도, 융은 집단무의식과 원형이에요."),
        dict(say="아들러는 열등감과 보상, 로저스는 인본주의예요."),
        dict(say="그래서 로저스에 출생순위와 생활양식을 연결하면 틀려요. 그건 아들러예요."),
        dict(say="융의 페르소나는 사회적 요구에 맞춘 가면, 그림자는 받아들이기 꺼리는 나의 일부예요."),
        dict(say="남성 내부의 여성성은 아니마, 여성 내부의 남성성은 아니무스예요."),
        dict(say="그럼 남성 안에 있는 여성성은, 아니마일까요 아니무스일까요?"),
    ],
    scenes=[
        dict(type="hook", lines=[0], sub="심리 역동 이론", words=["프로이트", "융", "아들러"], joiner=""),
        dict(type="cards", lines=[1, 2], header="학자와 키워드", rows=[
            dict(line=1, color=P, title="프로이트", desc="무의식 · 리비도"),
            dict(line=1, color=T, title="융", desc="집단무의식 · 원형"),
            dict(line=2, color=C, title="아들러", desc="열등감과 보상 · 출생순위"),
            dict(line=2, color=A, title="로저스", desc="인본주의 · 현상학적 장"),
        ]),
        dict(type="exam", lines=[3], tag="제24회 기출 응용 · 인간행동 · 9번",
             html="[[로저스]] -<br>출생순위와 생활양식", stamp="틀림!", stamp_color=C, stamp_line=3, stamp_frac=0.55),
        dict(type="cards", lines=[4, 5], header="융의 분석심리이론", rows=[
            dict(line=4, color=P, title="페르소나", desc="사회적 요구에 맞춘 가면"),
            dict(line=4, color=T, title="그림자", desc="받아들이기 꺼리는 나의 일부"),
            dict(line=5, color=C, title="아니마", desc="남성 내부의 여성성"),
            dict(line=5, color=A, title="아니무스", desc="여성 내부의 남성성"),
        ]),
        dict(type="cta", lines=[6], q="남성 안의 여성성은?", buttons=[("아니마?", P), ("아니무스?", T)], hint="정답은 댓글로 남겨 주세요!"),
    ],
)

# ---------------------------------------------------------------- EP5 스키너·반두라 (7,8번)
EPS[5] = dict(
    music=(110, 0, 25),
    lines=[
        dict(say="스키너와 반두라, 강화와 관찰학습을 정리해요!"),
        dict(say="고정비율은 일정한 횟수의 반응 후에, 고정간격은 일정한 시간이 지난 후에 강화해요."),
        dict(say="변동비율과 변동간격은, 그 횟수와 시간이 일정하지 않아요."),
        dict(say="그래서 고정간격강화가 일정한 수의 반응 후에 강화한다는 설명은 틀렸어요. 그건 고정비율이에요."),
        dict(say="반두라의 관찰학습은, 주의집중과 기억 단계를 먼저 거쳐요."),
        dict(say="기억한 정보를 구체적 행동으로 옮기는 게 운동재생, 동기가 있어야 실제로 해요."),
        dict(say="그럼 기억한 정보를 행동으로 옮기는 과정은, 기억일까요 운동재생일까요?"),
    ],
    scenes=[
        dict(type="hook", lines=[0], sub="학습이론", words=["스키너", "반두라"], joiner="VS"),
        dict(type="cards", lines=[1, 2], header="스키너의 강화계획", rows=[
            dict(line=1, color=P, title="고정비율", desc="일정한 횟수의 반응 후 강화"),
            dict(line=1, color=T, title="고정간격", desc="일정한 시간이 지난 후 강화"),
            dict(line=2, color=C, title="변동비율", desc="일정치 않은 횟수 후 강화"),
            dict(line=2, color=A, title="변동간격", desc="일정치 않은 시간 후 강화"),
        ]),
        dict(type="exam", lines=[3], tag="제24회 기출 응용 · 인간행동 · 7번",
             html="[[고정간격]]강화는<br>일정한 수의 반응 후에<br>강화한다.", stamp="틀림!", stamp_color=C, stamp_line=3, stamp_frac=0.6),
        dict(type="cards", lines=[4, 5], header="반두라의 관찰학습", rows=[
            dict(line=4, color=P, title="주의집중", desc="모델의 행동에 주목"),
            dict(line=4, color=T, title="기억", desc="상징적 표상으로 저장 · 연습"),
            dict(line=5, color=C, title="운동재생", desc="기억한 정보를 행동으로 실행"),
            dict(line=5, color=A, title="동기화", desc="강화를 기대해야 수행"),
        ]),
        dict(type="cta", lines=[6], q="행동으로 옮기는 과정은?", buttons=[("기억?", P), ("운동재생?", T)], hint="정답은 댓글로 남겨 주세요!"),
    ],
)

# ---------------------------------------------------------------- EP6 피아제·벡 (10,11번)
EPS[6] = dict(
    music=(106, 1, 26),
    lines=[
        dict(say="피아제와 벡, 생각이 자라고 생각이 꼬이는 이야기!"),
        dict(say="감각운동기에는 대상영속성이 생기고, 전조작기에는 상징적 사고와 물활론적 사고를 해요."),
        dict(say="구체적 조작기에는 보존개념을, 형식적 조작기에는 추상적 사고를 얻어요."),
        dict(say="그래서 전조작기에 보존개념이나 추상적 사고가 가능하다는 설명은, 틀렸어요."),
        dict(say="벡의 인지적 왜곡에는, 개인화와 이분법적 사고가 있어요."),
        dict(say="또 과잉일반화와 임의적 추론도 있어요. 기출에서는 네 개 모두 정답이었죠."),
        dict(say="그럼 한 번 실패했다고 항상 실패한다고 생각하면, 개인화일까요 과잉일반화일까요?"),
    ],
    scenes=[
        dict(type="hook", lines=[0], sub="인지 이론", words=["피아제", "벡"], joiner="&"),
        dict(type="cards", lines=[1, 2], header="피아제의 4단계", rows=[
            dict(line=1, color=P, title="감각운동기", desc="대상영속성 (0~2세)"),
            dict(line=1, color=T, title="전조작기", desc="상징적 사고 · 물활론 · 가상놀이"),
            dict(line=2, color=C, title="구체적 조작기", desc="보존개념 획득"),
            dict(line=2, color=A, title="형식적 조작기", desc="추상적 사고 · 가설 검증"),
        ]),
        dict(type="exam", lines=[3], tag="제24회 기출 응용 · 인간행동 · 11번",
             html="[[전조작기]]에<br>보존개념이 획득되고<br>추상적 사고가 가능하다.", stamp="틀림!", stamp_color=C, stamp_line=3, stamp_frac=0.75),
        dict(type="cards", lines=[4, 5], header="벡의 인지적 왜곡", rows=[
            dict(line=4, color=P, title="개인화", desc="상관없는 일을 내 탓으로"),
            dict(line=4, color=T, title="이분법적 사고", desc="흑 아니면 백으로 판단"),
            dict(line=5, color=C, title="과잉일반화", desc="한 번의 경험을 전부로 확대"),
            dict(line=5, color=A, title="임의적 추론", desc="근거 없이 결론을 내림"),
        ]),
        dict(type="cta", lines=[6], q="한 번 실패하면 늘 실패?", buttons=[("개인화?", P), ("과잉일반화?", T)], hint="정답은 댓글로 남겨 주세요!"),
    ],
)

# ---------------------------------------------------------------- EP7 체계이론 (12,13번)
EPS[7] = dict(
    music=(104, 2, 27),
    lines=[
        dict(say="일반체계이론과 생태체계이론, 용어가 자꾸 헷갈려요!"),
        dict(say="일반체계이론의 항상성은, 체계가 균형을 유지하려는 자기조절 경향이에요."),
        dict(say="엔트로피는 무질서가 늘어나는 경향이고, 시너지는 상호작용으로 커지는 효과예요."),
        dict(say="홀론은, 전체이면서 동시에 더 큰 체계의 부분이에요."),
        dict(say="생태체계이론의 대처는, 스트레스에 대응해 적합성을 회복하려는 노력이에요."),
        dict(say="호혜성은 서로 주고받는 영향이고, 다중종결성은 같은 출발에서 다른 결과가 나오는 거예요."),
        dict(say="기출 문제는, 스트레스 상황에서 개인이 쓰는 반응과 전략이 뭐냐고 물었어요. 정답은 대처예요."),
        dict(say="그럼 체계가 균형을 유지하려는 경향은, 항상성일까요 엔트로피일까요?"),
    ],
    scenes=[
        dict(type="hook", lines=[0], sub="체계이론", words=["일반체계", "생태체계"], joiner="VS"),
        dict(type="cards", lines=[1, 2, 3], header="일반체계이론 용어", rows=[
            dict(line=1, color=P, title="항상성", desc="균형을 유지하려는 경향"),
            dict(line=2, color=T, title="엔트로피", desc="무질서가 커지는 경향"),
            dict(line=2, color=C, title="시너지", desc="상호작용으로 커지는 효과"),
            dict(line=3, color=A, title="홀론", desc="전체이면서 동시에 부분"),
        ]),
        dict(type="cards", lines=[4, 5], header="생태체계이론 용어", rows=[
            dict(line=4, color=P, title="대처", desc="스트레스에 대응하는<br>노력과 전략"),
            dict(line=5, color=T, title="호혜성", desc="개인과 환경이<br>서로 영향을 줌"),
            dict(line=5, color=C, title="다중종결성", desc="같은 출발,<br>다른 결과"),
        ]),
        dict(type="exam", lines=[6], tag="제24회 기출 응용 · 인간행동 · 13번",
             html="스트레스 상황에서<br>개인이 사용하는<br>[[반응과 전략]]은?", stamp="대처!", stamp_color=T, stamp_line=6, stamp_frac=0.75),
        dict(type="cta", lines=[7], q="균형 유지 경향은?", buttons=[("항상성?", P), ("엔트로피?", T)], hint="정답은 댓글로 남겨 주세요!"),
    ],
)

# ---------------------------------------------------------------- EP8 사회환경체계 (14~17번)
EPS[8] = dict(
    music=(100, 3, 28),
    lines=[
        dict(say="미시, 중간, 외, 거시, 사회환경체계를 한눈에 정리해요!"),
        dict(say="미시체계는, 가족처럼 나와 직접 상호작용하는 환경이에요."),
        dict(say="중간체계는, 그런 미시체계들 사이의 관계예요."),
        dict(say="외체계는, 직접 참여하지 않아도 영향을 주는 부모의 직장 같은 곳이에요."),
        dict(say="거시체계는, 문화와 가치, 이념, 법과 정책 같은 사회구조적 맥락이에요."),
        dict(say="그래서 중간체계가 내부체계와 외체계의 관계라는 설명은, 틀렸어요."),
        dict(say="집단의 최소 단위는, 삼 인이 아니라 이 인 이상이에요.", cap="집단의 최소 단위는, 3인이 아니라 2인 이상이에요."),
        dict(say="또 다른 문화에 배타적인 태도를 취하라는 말도 틀려요. 문화적 역량이 필요해요."),
        dict(say="그럼 문화와 가치, 법과 정책 같은 맥락은, 중간체계일까요 거시체계일까요?"),
    ],
    scenes=[
        dict(type="hook", lines=[0], sub="브론펜브레너", words=["미시", "중간", "외", "거시"], joiner=""),
        dict(type="cards", lines=[1, 2, 3, 4], header="브론펜브레너의 체계", rows=[
            dict(line=1, color=P, title="미시체계", desc="나와 직접 상호작용 (가족)"),
            dict(line=2, color=T, title="중간체계", desc="미시체계들 사이의 관계"),
            dict(line=3, color=C, title="외체계", desc="참여는 안 해도 영향 (부모 직장)"),
            dict(line=4, color=A, title="거시체계", desc="문화 · 가치 · 이념 · 법 · 정책"),
        ]),
        dict(type="exam", lines=[5], tag="제24회 기출 응용 · 인간행동 · 14번",
             html="[[중간체계]]는 내부체계와<br>외체계 간 관계이다.", stamp="틀림!", stamp_color=C, stamp_line=5, stamp_frac=0.6),
        dict(type="cards", lines=[6, 7], header="집단과 문화", rows=[
            dict(line=6, color=C, title="집단은 3인 이상?", desc="최소 단위는 2인 이상", mark="x"),
            dict(line=7, color=A, title="배타적 태도?", desc="열린 태도 · 문화적 역량", mark="x"),
        ]),
        dict(type="cta", lines=[8], q="문화·법·정책 맥락은?", buttons=[("중간?", P), ("거시?", T)], hint="정답은 댓글로 남겨 주세요!"),
    ],
)

# ---------------------------------------------------------------- EP9 태아~유아기 (18~21번)
EPS[9] = dict(
    music=(108, 1, 29),
    lines=[
        dict(say="태아부터 유아기까지, 헷갈리는 포인트만 모았어요!"),
        dict(say="임신부의 불안이나 우울이 태아 발달에 영향이 없다는 설명은, 틀렸어요. 영향을 줄 수 있어요."),
        dict(say="모로반사는 갑작스러운 자극에 팔을 벌리고, 파악반사는 손바닥을 건드리면 꽉 쥐어요."),
        dict(say="발바닥을 긁으면 발가락이 부채처럼 펴지는 건 바빈스키반사, 뺨을 건드리면 고개를 돌리는 건 탐색반사예요."),
        dict(say="영아기에는 대상영속성이 생기고, 발달은 머리에서 다리로, 몸통에서 팔다리로 진행돼요."),
        dict(say="기본적 신뢰감은 유아기가 아니라, 영아기의 과제예요."),
        dict(say="그럼 발바닥을 긁으면 발가락이 펴지는 반사는, 바빈스키일까요 모로일까요?"),
    ],
    scenes=[
        dict(type="hook", lines=[0], sub="생애주기 ①", words=["태아", "영아기", "유아기"], joiner=""),
        dict(type="exam", lines=[1], tag="제24회 기출 응용 · 인간행동 · 18번",
             html="임신부의 불안이나 우울은<br>[[태아 발달에 영향이 없다.]]", stamp="틀림!", stamp_color=C, stamp_line=1, stamp_frac=0.55),
        dict(type="cards", lines=[2, 3], header="신생아 반사", rows=[
            dict(line=2, color=P, title="모로반사", desc="갑작스러운 자극에 팔을 벌려요"),
            dict(line=2, color=T, title="파악반사", desc="손바닥을 건드리면 꽉 쥐어요"),
            dict(line=3, color=C, title="바빈스키반사", desc="발바닥을 긁으면 발가락이 펴져요"),
            dict(line=3, color=A, title="탐색반사", desc="뺨을 건드리면 그쪽으로 고개"),
        ]),
        dict(type="cards", lines=[4, 5], header="영아기 · 유아기", rows=[
            dict(line=4, color=T, title="영아기: 대상영속성", desc="눈앞에 없어도 있다는 걸 알아요", mark="o"),
            dict(line=4, color=P, title="머리에서 다리로", desc="몸통에서 팔다리로 발달", mark="o"),
            dict(line=5, color=C, title="유아기에 신뢰감 형성?", desc="신뢰감은 영아기의 과제", mark="x"),
        ]),
        dict(type="cta", lines=[6], q="발가락이 펴지는 반사는?", buttons=[("바빈스키?", P), ("모로?", T)], hint="정답은 댓글로 남겨 주세요!"),
    ],
)

# ---------------------------------------------------------------- EP10 청소년~노년기 (22~25번)
EPS[10] = dict(
    music=(104, 2, 30),
    lines=[
        dict(say="청소년기부터 노년기까지, 마지막 정리예요!"),
        dict(say="마샤는, 위기를 겪었는지와 결정을 했는지로 정체감을 나눠요. 둘 다 하면 성취예요."),
        dict(say="위기 속에서 여러 역할을 실험하지만 아직 결정을 못 했다면, 유예예요."),
        dict(say="위기 없이 정해진 대로 받아들이면 유실, 위기도 결정도 없으면 혼란이에요."),
        dict(say="하비거스트의 청년기 과업은, 가정 꾸리기, 직업생활 시작, 마음에 맞는 사회집단 형성이에요. 삶의 의미를 되돌아보는 건 아니에요."),
        dict(say="노년기 과제로 에릭슨은, 자아통합 대 절망을 제시했어요."),
        dict(say="펙은 자아분화, 신체초월, 자아초월을, 버틀러는 인생 회고를 강조했죠."),
        dict(say="그래서 결정성 지능은 감퇴하고 유동성 지능이 향상된다는 말은, 거꾸로예요."),
        dict(say="그럼 자아분화 대 역할몰입을 제시한 학자는, 펙일까요 하비거스트일까요?"),
    ],
    scenes=[
        dict(type="hook", lines=[0], sub="생애주기 ②", words=["청소년", "청년", "노년"], joiner=""),
        dict(type="cards", lines=[1, 2, 3], header="마샤의 정체감 유형", rows=[
            dict(line=1, color=P, title="정체감 성취", desc="위기 경험 후 결정 완료"),
            dict(line=2, color=T, title="정체감 유예", desc="위기 중 · 아직 결정 못 함"),
            dict(line=3, color=C, title="정체감 유실", desc="위기 없이 주어진 결정 수용"),
            dict(line=3, color=A, title="정체감 혼란", desc="위기도 결정도 없는 상태"),
        ]),
        dict(type="exam", lines=[4], tag="제24회 기출 응용 · 인간행동 · 23번",
             html="청년기 과업:<br>[[삶의 의미를 되돌아보고<br>의미 있는 활동을 찾는다]]", stamp="아니에요!", stamp_color=C, stamp_line=4, stamp_frac=0.85),
        dict(type="cards", lines=[5, 6], header="노년기 발달과제", rows=[
            dict(line=5, color=P, title="에릭슨", desc="자아통합 대 절망"),
            dict(line=6, color=T, title="펙", desc="자아분화 · 신체초월 · 자아초월"),
            dict(line=6, color=A, title="버틀러", desc="인생 회고"),
        ]),
        dict(type="exam", lines=[7], tag="제24회 기출 응용 · 인간행동 · 24번",
             html="[[결정성 지능]]은 감퇴하고<br>유동성 지능은 향상된다.", stamp="거꾸로!", stamp_color=C, stamp_line=7, stamp_frac=0.6),
        dict(type="cta", lines=[8], q="자아분화 대 역할몰입은?", buttons=[("펙?", P), ("하비거스트?", T)], hint="정답은 댓글로 남겨 주세요!"),
    ],
)
