# -*- coding: utf-8 -*-
# 사회복지실천기술론 (제24회 2교시 26~50번) - v2 paper style, pink paper, cat mascot
# 제외한 문항(정답 확신 낮음): 29, 37, 39, 40, 41, 42, 47
EPS = {}
RED = "#e8431a"; GRN = "#12a37f"

# ---------------------------------------------------------------- EP1 실천지식·직면 (26,27번)
EPS[1] = dict(
    music=(96, 0, 61),
    lines=[
        dict(say="실천지식의 계층과 직면, 헷갈리지 않는 방법이 있어요!"),
        dict(say="실천지식은 큰 틀인 패러다임과 관점에서, 이론으로 점점 구체적이 돼요."),
        dict(say="그다음이 모델과 실천지혜예요. 문제분석과 개입방법을 구체적으로 제시하는 건 모델이죠."),
        dict(say="기출은 문제분석, 개입계획, 개입방법을 제시하는 실천지식을 물었고, 정답은 모델이에요."),
        dict(say="직면은 행동과 진술이 불일치할 때 적용하고, 이해와 자기성찰을 촉구해요."),
        dict(say="충분한 근거가 있을 때 하고, 즉각적인 행동변화가 이루어진다는 말은 틀려요."),
        dict(say="그럼 행동과 진술이 어긋날 때 쓰는 기법은, 직면일까요 반영일까요?"),
    ],
    scenes=[
        dict(type="hook", lines=[0], headline="실천지식의 계층과<br>[[직면]]"),
        dict(type="cards", lines=[1, 2], headline="실천지식,<br>[[큰 틀에서 구체적으로]]", rows=[
            dict(line=1, title="패러다임 · 관점", desc="세상을 보는 큰 틀"),
            dict(line=1, title="이론", desc="현상을 설명하는 체계"),
            dict(line=2, title="모델", desc="개입방법을 구체적으로 제시"),
            dict(line=2, title="실천지혜", desc="경험에서 얻은 실천 노하우"),
        ]),
        dict(type="exam", lines=[3], headline="이 설명,<br>[[무엇일까요?]]", tag="제24회 기출 응용 · 실천기술론 · 26번",
             html="문제분석 · 개입계획 ·<br>개입방법을 제시하는<br>[[실천지식]]은?", stamp="모델!", stamp_color=GRN, stamp_line=3, stamp_frac=0.8),
        dict(type="cards", lines=[4, 5], headline="[[직면]],<br>이건 맞고 이건 틀려요", rows=[
            dict(line=4, title="행동과 진술 불일치", desc="그럴 때 적용해요", mark="o"),
            dict(line=4, title="자기성찰 촉구", desc="이해를 돕는 방법", mark="o"),
            dict(line=5, title="충분한 근거 필요", desc="필요성에 확실한 근거가", mark="o"),
            dict(line=5, title="즉각적 행동변화", desc="저절로 이루어지지 않아요", mark="x"),
        ]),
        dict(type="cta", lines=[6], headline="[[댓글]]로 정답을<br>알려 주세요!", q="불일치할 때 쓰는 기법은?", buttons=[("직면?", 0), ("반영?", 1)]),
    ],
)

# ---------------------------------------------------------------- EP2 정신역동·심리사회모델 (28,34번)
EPS[2] = dict(
    music=(92, 1, 62),
    lines=[
        dict(say="정신역동모델과 심리사회모델, 개입기술이 헷갈려요!"),
        dict(say="정신역동모델의 자유연상은 떠오르는 대로 말하게 하고, 초점화는 핵심 문제에 집중해요."),
        dict(say="꿈분석은 무의식의 미해결 과제로 통찰을 주고, 훈습은 통찰을 반복해 행동으로 옮겨요."),
        dict(say="그래서 훈습이 핵심문제의 원인에 초점을 맞춘다는 설명은 틀려요."),
        dict(say="심리사회모델의 지지하기는 격려로 불안을 줄이고, 직접적 영향은 필요한 조언과 제안을 해요."),
        dict(say="탐색, 기술, 환기는 클라이언트의 감정을 표현하게 도와 문제인식을 높여요."),
        dict(say="그래서 사회복지사의 감정을 표출한다는 설명은 틀려요. 표현하는 건 클라이언트의 감정이에요."),
        dict(say="그럼 필요한 조언이나 제안을 하는 기술은, 지지하기일까요 직접적 영향일까요?"),
    ],
    scenes=[
        dict(type="hook", lines=[0], headline="정신역동 · 심리사회모델<br>[[개입기술]]"),
        dict(type="cards", lines=[1, 2], headline="[[정신역동모델]]<br>개입기술", rows=[
            dict(line=1, title="자유연상", desc="떠오르는 대로 말하게 해요"),
            dict(line=1, title="초점화", desc="핵심 문제에 초점을 맞춰요"),
            dict(line=2, title="꿈분석", desc="무의식의 미해결 과제로 통찰"),
            dict(line=2, title="훈습", desc="통찰을 반복해 행동 변화로"),
        ]),
        dict(type="exam", lines=[3], headline="이 설명,<br>[[맞을까요?]]", tag="제24회 기출 응용 · 실천기술론 · 28번",
             html="[[훈습]]은 이야기 중<br>핵심문제의 원인에<br>초점을 맞춘다", stamp="틀림!", stamp_color=RED, stamp_line=3, stamp_frac=0.55),
        dict(type="cards", lines=[4, 5], headline="[[심리사회모델]]<br>개입기술", rows=[
            dict(line=4, title="지지하기", desc="문제해결능력을 인정하고<br>격려해 불안을 줄여요"),
            dict(line=4, title="직접적 영향", desc="필요한 조언이나<br>제안을 해요"),
            dict(line=5, title="탐색 · 기술 · 환기", desc="클라이언트의 감정을<br>표현하게 도와요"),
        ]),
        dict(type="exam", lines=[6], headline="이 설명,<br>[[맞을까요?]]", tag="제24회 기출 응용 · 실천기술론 · 34번",
             html="탐색-기술-환기:<br>[[사회복지사의 감정]]을 표출한다", stamp="틀림!", stamp_color=RED, stamp_line=6, stamp_frac=0.5),
        dict(type="cta", lines=[7], headline="[[댓글]]로 정답을<br>알려 주세요!", q="조언과 제안은?", buttons=[("지지하기?", 0), ("직접적 영향?", 1)]),
    ],
)

# ---------------------------------------------------------------- EP3 해결중심·과제중심 (30,31번)
EPS[3] = dict(
    music=(100, 2, 63),
    lines=[
        dict(say="해결중심모델의 질문기법, 질문마다 이름이 달라요!"),
        dict(say="기적질문은 해결됐다고 상상해 보는 질문, 예외질문은 문제가 없었던 때를 묻는 질문이에요."),
        dict(say="척도질문은 점수로 수준을 묻고, 대처질문은 어려움을 어떻게 견뎌 왔는지 물어요."),
        dict(say="기출 문장은 해결됐다고 상상해 보라는 질문을 예외질문이라 불렀어요. 그건 기적질문이에요."),
        dict(say="과제중심모델의 초기단계는 표적문제 우선순위, 서비스 계약, 초기 과제를 정해요."),
        dict(say="과제이행을 위한 계획은 초기단계가 아니라 중간단계 과업이에요."),
        dict(say="그럼 문제가 모두 해결됐다고 상상해 보게 하는 질문은, 기적질문일까요 예외질문일까요?"),
    ],
    scenes=[
        dict(type="hook", lines=[0], headline="해결중심모델의<br>[[질문기법]]"),
        dict(type="cards", lines=[1, 2], headline="질문 이름,<br>[[짝맞추기]]", rows=[
            dict(line=1, title="기적질문", desc="문제가 모두 해결됐다고 상상"),
            dict(line=1, title="예외질문", desc="문제가 없었던 때는 언제인지"),
            dict(line=2, title="척도질문", desc="점수로 현재 수준을 물어요"),
            dict(line=2, title="대처질문", desc="어려움을 어떻게 견뎌 왔는지"),
        ]),
        dict(type="exam", lines=[3], headline="이 이름,<br>[[맞을까요?]]", tag="제24회 기출 응용 · 실천기술론 · 30번",
             html="[[예외질문]]: 문제가<br>모두 해결됐다고 상상했을 때<br>무엇이 달라질까요?", stamp="기적질문!", stamp_color=GRN, stamp_line=3, stamp_frac=0.85),
        dict(type="cards", lines=[4, 5], headline="과제중심모델<br>[[초기 vs 중간]]", rows=[
            dict(line=4, title="초기단계", desc="표적문제 우선순위 · 서비스 계약<br>초기 과제 결정"),
            dict(line=5, title="중간단계", desc="과제이행을 위한 계획과<br>실행 점검"),
        ]),
        dict(type="cta", lines=[6], headline="[[댓글]]로 정답을<br>알려 주세요!", q="상상해 보게 하는 질문은?", buttons=[("기적?", 0), ("예외?", 1)]),
    ],
)

# ---------------------------------------------------------------- EP4 인지행동모델 (32,33번)
EPS[4] = dict(
    music=(98, 3, 64),
    lines=[
        dict(say="인지행동모델, 기법 이름과 설명을 짝지어요!"),
        dict(say="모델링은 관찰학습으로 행동을 배우고, 체계적 둔감화는 이완으로 불안을 줄여요."),
        dict(say="인지재구조화는 왜곡된 사고를 바꾸고, 역설적 의도는 두려운 행동을 일부러 해 보게 해요."),
        dict(say="그래서 체계적 둔감화가 비합리적 신념의 당위성을 검토한다는 설명은 틀려요."),
        dict(say="치료적 동맹이 중요하고, 문답으로 인지를 고치며, 비합리적 신념을 원인으로 봐요."),
        dict(say="하지만 시간을 제한하지 않고 개입한다는 말은 틀려요. 단기적이고 시간 제한적이에요."),
        dict(say="그럼 이완과 불안 위계로 불안을 줄이는 기법은, 체계적 둔감화일까요 모델링일까요?"),
    ],
    scenes=[
        dict(type="hook", lines=[0], headline="인지행동모델의<br>[[개입기법]]"),
        dict(type="cards", lines=[1, 2], headline="인지행동<br>[[기법 4가지]]", rows=[
            dict(line=1, title="모델링", desc="관찰학습으로 행동을 습득"),
            dict(line=1, title="체계적 둔감화", desc="이완과 불안 위계로 불안 감소"),
            dict(line=2, title="인지재구조화", desc="왜곡된 사고를 바꿔요"),
            dict(line=2, title="역설적 의도", desc="두려운 행동을 일부러 해 봐요"),
        ]),
        dict(type="exam", lines=[3], headline="이 설명,<br>[[맞을까요?]]", tag="제24회 기출 응용 · 실천기술론 · 32번",
             html="[[체계적 둔감화]]는<br>비합리적 신념의 당위성을<br>검토한다", stamp="틀림!", stamp_color=RED, stamp_line=3, stamp_frac=0.7),
        dict(type="cards", lines=[4, 5], headline="인지행동모델<br>[[특징]]", rows=[
            dict(line=4, title="치료적 동맹", desc="협력관계가 중요해요", mark="o"),
            dict(line=4, title="소크라테스식 문답", desc="질문으로 인지를 수정", mark="o"),
            dict(line=4, title="비합리적 신념", desc="행동 · 정서 문제의 원인", mark="o"),
            dict(line=5, title="시간 제한 없음", desc="단기 · 시간 제한적이에요", mark="x"),
        ]),
        dict(type="cta", lines=[6], headline="[[댓글]]로 정답을<br>알려 주세요!", q="불안을 줄이는 기법은?", buttons=[("둔감화?", 0), ("모델링?", 1)]),
    ],
)

# ---------------------------------------------------------------- EP5 실천모델 특징 (35번)
EPS[5] = dict(
    music=(104, 0, 65),
    lines=[
        dict(say="사회복지 실천모델, 특징을 짝지어 볼까요?"),
        dict(say="과제중심모델은 클라이언트가 우선 해결하기 원하는 문제를 중요하게 다뤄요."),
        dict(say="클라이언트중심모델은 지금 여기의 경험과 감정을 중시해요."),
        dict(say="임파워먼트모델은 잠재력 발휘와 자원연계를, 위기개입모델은 단기 집중 개입을 강조해요."),
        dict(say="그래서 클라이언트중심모델이 과거경험을 주로 다룬다는 설명은 틀려요."),
        dict(say="그럼 단기 집중 개입을 하는 모델은, 위기개입일까요 임파워먼트일까요?"),
    ],
    scenes=[
        dict(type="hook", lines=[0], headline="실천모델,<br>[[특징 짝맞추기]]"),
        dict(type="cards", lines=[1, 2, 3], headline="실천모델<br>[[핵심 특징]]", rows=[
            dict(line=1, title="과제중심모델", desc="클라이언트가 원하는 문제 우선"),
            dict(line=2, title="클라이언트중심모델", desc="지금 여기의 경험과 감정"),
            dict(line=3, title="임파워먼트모델", desc="잠재력 발휘와 자원연계"),
            dict(line=3, title="위기개입모델", desc="단기 집중 개입"),
        ]),
        dict(type="exam", lines=[4], headline="이 설명,<br>[[맞을까요?]]", tag="제24회 기출 응용 · 실천기술론 · 35번",
             html="[[클라이언트중심모델]]은<br>과거경험을 주로 다룬다", stamp="틀림!", stamp_color=RED, stamp_line=4, stamp_frac=0.6),
        dict(type="cta", lines=[5], headline="[[댓글]]로 정답을<br>알려 주세요!", q="단기 집중 개입은?", buttons=[("위기개입?", 0), ("임파워먼트?", 1)]),
    ],
)

# ---------------------------------------------------------------- EP6 가족치료모델 (36,38번)
EPS[6] = dict(
    music=(94, 1, 66),
    lines=[
        dict(say="가족치료모델, 목표와 기법을 짝지어요!"),
        dict(say="구조적 모델은 재구조화와 합류, 전략적 모델은 문제 해결과 역설적 기법을 써요."),
        dict(say="경험적 모델은 성장과 동적 가족화, 다세대 모델은 자아분화와 가계도, 코칭을 써요."),
        dict(say="그래서 경험적 모델의 목표를 증상 제거로 짝지으면 틀려요. 경험적 모델은 성장이 목표예요."),
        dict(say="다세대전수과정은 미분화된 관계패턴이 세대에 걸쳐 반복되는 거고, 가족투사과정은 미성숙한 부모가 불안을 자녀에게 투사하는 거예요."),
        dict(say="하지만 삼각관계 속 자녀의 자아분화 수준이 높아진다는 말은 틀려요. 오히려 낮아져요."),
        dict(say="그럼 합류 기법을 쓰는 모델은, 구조적 모델일까요 전략적 모델일까요?"),
    ],
    scenes=[
        dict(type="hook", lines=[0], headline="가족치료모델,<br>[[목표와 기법]]"),
        dict(type="cards", lines=[1, 2], headline="모델별<br>[[목표 · 기법]]", rows=[
            dict(line=1, title="구조적 모델", desc="가족구조 재구조화 · 합류"),
            dict(line=1, title="전략적 모델", desc="문제 해결 · 역설적 기법"),
            dict(line=2, title="경험적 모델", desc="개인 · 가족 성장 · 동적 가족화"),
            dict(line=2, title="다세대 모델", desc="자아분화 · 가계도 · 코칭"),
        ]),
        dict(type="exam", lines=[3], headline="이 연결,<br>[[맞을까요?]]", tag="제24회 기출 응용 · 실천기술론 · 36번",
             html="[[경험적 모델]] - 증상 제거 -<br>동적 가족화", stamp="틀림!", stamp_color=RED, stamp_line=3, stamp_frac=0.6),
        dict(type="cards", lines=[4, 5], headline="다세대 모델,<br>[[맞는 말 · 틀린 말]]", rows=[
            dict(line=4, title="다세대전수과정", desc="미분화된 관계패턴이<br>세대에 걸쳐 반복", mark="o"),
            dict(line=4, title="가족투사과정", desc="미성숙한 부모가 불안을<br>자녀에게 투사", mark="o"),
            dict(line=5, title="삼각관계 속 자녀", desc="자아분화 수준이<br>높아진다", mark="x"),
        ]),
        dict(type="cta", lines=[6], headline="[[댓글]]로 정답을<br>알려 주세요!", q="합류 기법의 모델은?", buttons=[("구조적?", 0), ("전략적?", 1)]),
    ],
)

# ---------------------------------------------------------------- EP7 집단 구성·자기노출 (43,45,48번)
EPS[7] = dict(
    music=(90, 2, 67),
    lines=[
        dict(say="집단 실천에서 자주 틀리는 포인트를 모았어요!"),
        dict(say="폐쇄집단은 역할과 집단규범이 안정적이고 응집력이 높아요."),
        dict(say="개방집단은 새로운 성원이 들어올 수 있는 집단이에요."),
        dict(say="아동집단의 규모는 성인집단보다 작은 것이 좋아요."),
        dict(say="그래서 개방집단의 응집력이 강하게 나타난다는 설명은 틀렸어요."),
        dict(say="자기노출 수준은 집단발달단계와 무관하다는 말은 틀려요."),
        dict(say="초기의 지나친 자기노출은 집단에 부정적 영향을 줄 수 있고, 내용은 집단 목표와 관련 있어야 해요."),
        dict(say="또 집단 내 의사소통은 초기에는 사회복지사 중심, 점차 집단 중심으로 이루어지는 게 바람직해요."),
        dict(say="그럼 응집력이 높게 나타나는 집단은, 폐쇄집단일까요 개방집단일까요?"),
    ],
    scenes=[
        dict(type="hook", lines=[0], headline="집단사회복지실천,<br>[[헷갈리는 포인트]]"),
        dict(type="cards", lines=[1, 2, 3], headline="집단 [[구성]]", rows=[
            dict(line=1, title="폐쇄집단", desc="역할과 규범이 안정적<br>응집력이 높아요"),
            dict(line=2, title="개방집단", desc="새로운 성원이<br>들어올 수 있어요"),
            dict(line=3, title="아동집단", desc="규모는 성인집단보다<br>작은 것이 좋아요"),
        ]),
        dict(type="exam", lines=[4], headline="이 설명,<br>[[맞을까요?]]", tag="제24회 기출 응용 · 실천기술론 · 48번",
             html="[[개방집단]]은 집단응집력이<br>강하게 나타난다", stamp="틀림!", stamp_color=RED, stamp_line=4, stamp_frac=0.7),
        dict(type="cards", lines=[5, 6], headline="[[자기노출]],<br>맞는 말 · 틀린 말", rows=[
            dict(line=5, title="발달단계와 무관", desc="단계에 맞게 조절해요", mark="x"),
            dict(line=6, title="초기의 지나친 노출", desc="집단에 부정적 영향", mark="o"),
            dict(line=6, title="집단 목표와 관련", desc="내용은 목표와 연결", mark="o"),
        ]),
        dict(type="exam", lines=[7], headline="이 설명,<br>[[맞을까요?]]", tag="제24회 기출 응용 · 실천기술론 · 43번",
             html="의사소통은 초기에 [[집단 중심]],<br>이후에 사회복지사 중심", stamp="틀림!", stamp_color=RED, stamp_line=7, stamp_frac=0.55),
        dict(type="cta", lines=[8], headline="[[댓글]]로 정답을<br>알려 주세요!", q="응집력이 높은 집단은?", buttons=[("폐쇄?", 0), ("개방?", 1)]),
    ],
)

# ---------------------------------------------------------------- EP8 치료집단·목표설정 (44,46번)
EPS[8] = dict(
    music=(102, 3, 68),
    lines=[
        dict(say="치료집단의 유형과 목표설정을 정리해요!"),
        dict(say="지지집단은 비슷한 경험을 나누며 대처 능력을 키우고, 교육집단은 지식과 기술을 배워요."),
        dict(say="행동적 집단은 재강화와 조건화로 증상을 완화하는 집단이에요."),
        dict(say="기출 사례는 공포증 클라이언트가 재강화와 조건화로 증상을 완화하는 집단이라, 행동적 집단이에요."),
        dict(say="집단목표는 집단지도자와 성원의 토론으로 수정할 수 있고, 개인목표와 양립할 수 있어야 해요."),
        dict(say="또 구체적이고 측정 가능해야 하고, 표현되지 않은 욕구도 고려해요."),
        dict(say="그럼 공포증을 재강화와 조건화로 완화하는 집단은, 행동적 집단일까요 분석적 집단일까요?"),
    ],
    scenes=[
        dict(type="hook", lines=[0], headline="치료집단 유형과<br>[[목표설정]]"),
        dict(type="cards", lines=[1, 2], headline="집단의<br>[[유형]]", rows=[
            dict(line=1, title="지지집단", desc="비슷한 경험을 나누며<br>대처 능력을 키워요"),
            dict(line=1, title="교육집단", desc="필요한 지식과 기술을<br>배워요"),
            dict(line=2, title="행동적 집단", desc="재강화 · 조건화로<br>증상을 완화해요"),
        ]),
        dict(type="exam", lines=[3], headline="이 집단,<br>[[무엇일까요?]]", tag="제24회 기출 응용 · 실천기술론 · 44번",
             html="공포증 클라이언트가 모여<br>재강화 · 조건화로 증상 완화", stamp="행동적 집단!", stamp_color=GRN, stamp_line=3, stamp_frac=0.85),
        dict(type="cards", lines=[4, 5], headline="집단 [[목표설정]],<br>이건 모두 맞아요", rows=[
            dict(line=4, title="토론으로 수정", desc="지도자와 성원이 함께", mark="o"),
            dict(line=4, title="개인목표와 양립", desc="집단 · 개인목표가 함께", mark="o"),
            dict(line=5, title="구체적이고 측정 가능", desc="누구나 확인할 수 있게", mark="o"),
            dict(line=5, title="숨은 욕구도 고려", desc="표현되지 않은 욕구까지", mark="o"),
        ]),
        dict(type="cta", lines=[6], headline="[[댓글]]로 정답을<br>알려 주세요!", q="공포증 완화 집단은?", buttons=[("행동적?", 0), ("분석적?", 1)]),
    ],
)

# ---------------------------------------------------------------- EP9 기록·단일사례설계 (49,50번)
EPS[9] = dict(
    music=(96, 0, 69),
    lines=[
        dict(say="문제중심기록과 단일사례설계, 마지막 정리예요!"),
        dict(say="에스는 클라이언트가 말하는 주관적 정보, 오는 사회복지사가 관찰한 객관적 정보예요.",
             cap="S는 클라이언트가 말하는 주관적 정보, O는 사회복지사가 관찰한 객관적 정보예요."),
        dict(say="에이는 문제에 대한 견해와 해석인 사정, 피는 문제해결 방법에 관한 계획이에요.",
             cap="A는 문제에 대한 견해와 해석인 사정, P는 문제해결 방법에 관한 계획이에요."),
        dict(say="그래서 문제해결에 활용 가능한 자원 정보가 들어간다는 설명은, 포함되지 않는 내용이에요."),
        dict(say="단일사례설계에서 가장 기본적인 유형은 에이비 설계예요. 기초선 다음에 개입을 하죠.",
             cap="단일사례설계에서 가장 기본적인 유형은 AB설계예요. 기초선 다음에 개입을 하죠."),
        dict(say="에이비에이비 설계는 개입을 중단했다가 다시 하면서 효과를 확인하고, 에이비씨 설계는 서로 다른 개입을 이어 적용해요.",
             cap="ABAB설계는 개입을 중단했다가 다시 하며 효과를 확인하고, ABC설계는 서로 다른 개입을 이어 적용해요."),
        dict(say="그래서 가장 기본적인 유형이 에이비에이비 설계라는 말은 틀려요. 가장 기본은 에이비 설계예요.",
             cap="그래서 가장 기본적인 유형이 ABAB설계라는 말은 틀려요. 가장 기본은 AB설계예요."),
        dict(say="그럼 문제중심기록에서 사회복지사가 관찰한 정보는, 주관적일까요 객관적일까요?"),
    ],
    scenes=[
        dict(type="hook", lines=[0], headline="문제중심기록과<br>[[단일사례설계]]"),
        dict(type="cards", lines=[1, 2], headline="문제중심기록<br>[[SOAP]]", rows=[
            dict(line=1, title="주관적 정보", desc="클라이언트가 말하는 문제", badge="S"),
            dict(line=1, title="객관적 정보", desc="사회복지사가 관찰한 정보", badge="O"),
            dict(line=2, title="사정", desc="문제에 대한 견해 · 해석", badge="A"),
            dict(line=2, title="계획", desc="문제해결 방법에 관한 계획", badge="P"),
        ]),
        dict(type="exam", lines=[3], headline="이 내용,<br>[[포함될까요?]]", tag="제24회 기출 응용 · 실천기술론 · 49번",
             html="문제중심기록에는<br>[[활용 가능한 자원 정보]]가<br>포함된다", stamp="틀림!", stamp_color=RED, stamp_line=3, stamp_frac=0.7),
        dict(type="cards", lines=[4, 5], headline="단일사례설계<br>[[기본 유형]]", rows=[
            dict(line=4, title="AB설계", desc="가장 기본 유형<br>기초선(A) 후 개입(B)"),
            dict(line=5, title="ABAB설계", desc="개입을 중단했다<br>다시 시작해 효과 확인"),
            dict(line=5, title="ABC설계", desc="서로 다른 개입을<br>이어서 적용"),
        ]),
        dict(type="exam", lines=[6], headline="이 설명,<br>[[맞을까요?]]", tag="제24회 기출 응용 · 실천기술론 · 50번",
             html="가장 기본적인 유형은<br>[[ABAB설계]]이다", stamp="틀림!", stamp_color=RED, stamp_line=6, stamp_frac=0.6),
        dict(type="cta", lines=[7], headline="[[댓글]]로 정답을<br>알려 주세요!", q="관찰한 정보는?", buttons=[("주관적?", 0), ("객관적?", 1)]),
    ],
)
