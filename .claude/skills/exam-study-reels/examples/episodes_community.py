# -*- coding: utf-8 -*-
# 사회복지실천(지역사회복지론) 제24회 2교시 51~75번 - v2 paper style, lavender paper, puppy mascot
# 제외한 문항(정답 확신 낮음): 59, 60, 61, 62, 66, 69, 71, 72
EPS = {}
RED = "#e8431a"; GRN = "#12a37f"
CTA_HEAD = "[[댓글]]로 정답을<br>알려 주세요!"

# ---------------------------------------------------------------- EP1 이념·워렌 비교척도 (51,52번)
EPS[1] = dict(
    music=(94, 1, 71),
    lines=[
        dict(say="지역사회복지의 이념과 워렌의 비교척도, 헷갈리지 않는 방법!"),
        dict(say="이념에는 정상화, 탈시설화, 사회통합, 주민참여, 네트워크가 있어요."),
        dict(say="그중 네트워크는 서비스 제공자뿐 아니라 다양한 사회적 관계를 조직화하는 거예요."),
        dict(say="기출은 사회적 인간관계의 조직화와 관련된 이념을 물었고, 정답은 네트워크예요."),
        dict(say="워렌의 비교척도는 지역적 자치성과 서비스 영역의 일치성,"),
        dict(say="지역에 대한 주민의 심리적 동일시, 그리고 수평적 유형이에요."),
        dict(say="기출에서 단위 조직들이 구조적, 기능적으로 관련된 정도는 수평적 유형이에요."),
        dict(say="그럼 주민이 지역에 갖는 소속감은, 심리적 동일시일까요 수평적 유형일까요?"),
    ],
    scenes=[
        dict(type="hook", lines=[0], headline="지역사회복지<br>[[이념과 비교척도]]"),
        dict(type="cards", lines=[1, 2], headline="지역사회복지<br>[[이념]]", rows=[
            dict(line=1, title="정상화 · 탈시설화", desc="지역사회 안에서 일상적인 삶을"),
            dict(line=1, title="사회통합", desc="소외 없이 함께 살아가요"),
            dict(line=1, title="주민참여", desc="주민이 직접 참여해요"),
            dict(line=2, title="네트워크", desc="서비스 제공자와 사회적 관계 조직화"),
        ]),
        dict(type="exam", lines=[3], headline="이 설명,<br>[[무엇일까요?]]", tag="제24회 기출 응용 · 지역사회복지론 · 51번",
             html="서비스 제공자뿐 아니라<br>다양한 사회적 인간관계를<br>조직화하는 [[이념]]은?", stamp="네트워크!", stamp_color=GRN, stamp_line=3, stamp_frac=0.85),
        dict(type="cards", lines=[4, 5], headline="워렌의<br>[[비교척도]]", rows=[
            dict(line=4, title="지역적 자치성", desc="지역이 독자적으로 결정하는 정도"),
            dict(line=4, title="서비스 영역의 일치성", desc="학교 · 공공시설이 같은 지역에서"),
            dict(line=5, title="심리적 동일시", desc="주민이 지역에 갖는 소속감"),
            dict(line=5, title="수평적 유형", desc="단위 조직이 구조적 · 기능적 관련"),
        ]),
        dict(type="exam", lines=[6], headline="이 척도,<br>[[무엇일까요?]]", tag="제24회 기출 응용 · 지역사회복지론 · 52번",
             html="단위 조직들이<br>구조적 · 기능적으로<br>관련된 정도는?", stamp="수평적 유형!", stamp_color=GRN, stamp_line=6, stamp_frac=0.85),
        dict(type="cta", lines=[7], headline=CTA_HEAD, q="주민의 소속감은?", buttons=[("동일시?", 0), ("수평적?", 1)]),
    ],
)

# ---------------------------------------------------------------- EP2 동향 시대순·새마을운동 (53,54번)
EPS[2] = dict(
    music=(98, 2, 72),
    lines=[
        dict(say="지역사회복지 동향의 순서와 새마을운동, 정리해 볼까요?"),
        dict(say="이천오 년 자원봉사활동 기본법, 이천팔 년 노인장기요양보험이 시행됐어요.",
             cap="2005년 자원봉사활동 기본법, 2008년 노인장기요양보험이 시행됐어요."),
        dict(say="그다음 동주민센터가 행정복지센터로 바뀌었고, 이천십팔 년에 통합돌봄 기본계획이 발표됐어요.",
             cap="그다음 동주민센터가 행정복지센터로 바뀌었고, 2018년에 통합돌봄 기본계획이 발표됐어요."),
        dict(say="그래서 노인장기요양보험이 자원봉사활동 기본법보다 먼저라는 순서는 틀려요."),
        dict(say="새마을운동의 기본정신은 근면, 자조, 협동이고, 새마을의 날은 매년 사월 이십이일이에요.",
             cap="새마을운동의 기본정신은 근면, 자조, 협동이고, 새마을의 날은 매년 4월 22일이에요."),
        dict(say="중앙본부 창립으로 민간주도로 바뀌었고, 칠십 년대 기록물은 세계기록유산이에요.",
             cap="중앙본부 창립으로 민간주도로 바뀌었고, 70년대 기록물은 세계기록유산이에요."),
        dict(say="그래서 새마을운동이 소득증대운동으로 발전하지 못했다는 설명은 틀려요."),
        dict(say="그럼 새마을의 날은, 사월 이십이일일까요 오월 이십이일일까요?", cap="그럼 새마을의 날은, 4월 22일일까요 5월 22일일까요?"),
    ],
    scenes=[
        dict(type="hook", lines=[0], headline="지역사회복지<br>[[동향과 새마을운동]]"),
        dict(type="cards", lines=[1, 2], headline="동향,<br>[[시대순으로]]", rows=[
            dict(line=1, title="자원봉사활동 기본법 시행", desc="2005년"),
            dict(line=1, title="노인장기요양보험 시행", desc="2008년"),
            dict(line=2, title="행정복지센터로 변경", desc="동주민센터에서 바뀜"),
            dict(line=2, title="통합돌봄 기본계획 발표", desc="2018년"),
        ]),
        dict(type="exam", lines=[3], headline="이 순서,<br>[[맞을까요?]]", tag="제24회 기출 응용 · 지역사회복지론 · 53번",
             html="[[노인장기요양보험]] 시행이<br>자원봉사활동 기본법보다<br>먼저이다", stamp="틀림!", stamp_color=RED, stamp_line=3, stamp_frac=0.7),
        dict(type="cards", lines=[4, 5], headline="[[새마을운동]]<br>핵심 정리", rows=[
            dict(line=4, title="기본정신", desc="근면 · 자조 · 협동"),
            dict(line=4, title="새마을의 날", desc="매년 4월 22일"),
            dict(line=5, title="민간주도 전환", desc="새마을운동중앙본부 창립"),
            dict(line=5, title="세계기록유산", desc="1970년대 기록물 등재"),
        ]),
        dict(type="exam", lines=[6], headline="이 설명,<br>[[맞을까요?]]", tag="제24회 기출 응용 · 지역사회복지론 · 54번",
             html="농촌 환경 개선으로 시작해<br>[[소득증대운동으로는<br>발전하지 못했다]]", stamp="틀림!", stamp_color=RED, stamp_line=6, stamp_frac=0.6),
        dict(type="cta", lines=[7], headline=CTA_HEAD, q="새마을의 날은?", buttons=[("4월 22일?", 0), ("5월 22일?", 1)]),
    ],
)

# ---------------------------------------------------------------- EP3 지역사회복지 이론 (55,56번)
EPS[3] = dict(
    music=(92, 3, 73),
    lines=[
        dict(say="지역사회복지 이론, 사례를 보고 이름을 맞혀 볼까요?"),
        dict(say="자원의존이론은 자원 교환의 불균형을 경쟁이나 재평가 같은 전략으로 고쳐요."),
        dict(say="사회체계이론은 하위체계들이 서로 어떻게 연관돼 상호작용하는지 봐요."),
        dict(say="자원동원이론은 사회운동의 성패가 충원과 자금조달, 조직구조에 달렸다고 봐요."),
        dict(say="기출 사례는 보조금 지도점검과 중앙정부 예산지원에 영향을 받는 지자체라서, 자원의존이론이에요."),
        dict(say="또 장애인 학대 문제를 가족, 이웃, 공공기관 등 하위체계의 연관으로 보면 사회체계이론이에요."),
        dict(say="그럼 자원 교환의 불균형을 고치는 이론은, 자원의존이론일까요 자원동원이론일까요?"),
    ],
    scenes=[
        dict(type="hook", lines=[0], headline="지역사회복지 이론,<br>[[사례로 맞히기]]"),
        dict(type="cards", lines=[1, 2, 3], headline="이론과<br>[[핵심 설명]]", rows=[
            dict(line=1, title="자원의존이론", desc="자원 교환의 불균형을<br>경쟁 · 재평가로 수정"),
            dict(line=2, title="사회체계이론", desc="하위체계들이 서로 연관되어<br>상호작용하는 것을 봐요"),
            dict(line=3, title="자원동원이론", desc="사회운동의 성패는 충원 · 자금<br>조직구조 능력에 달렸어요"),
        ]),
        dict(type="exam", lines=[4], headline="이 사례,<br>[[어떤 이론일까요?]]", tag="제24회 기출 응용 · 지역사회복지론 · 55번",
             html="보조금 지도점검을 받은<br>사회복지관, 중앙 예산에<br>영향받는 지자체", stamp="자원의존이론!", stamp_color=GRN, stamp_line=4, stamp_frac=0.85),
        dict(type="exam", lines=[5], headline="이 사례,<br>[[어떤 이론일까요?]]", tag="제24회 기출 응용 · 지역사회복지론 · 56번",
             html="장애인 학대 문제를<br>가족 · 이웃 · 공공기관 등<br>하위체계의 연관으로 파악", stamp="사회체계이론!", stamp_color=GRN, stamp_line=5, stamp_frac=0.85),
        dict(type="cta", lines=[6], headline=CTA_HEAD, q="교환의 불균형 수정은?", buttons=[("자원의존?", 0), ("자원동원?", 1)]),
    ],
)

# ---------------------------------------------------------------- EP4 실천 원칙·기술 (57,63,64,65번)
EPS[4] = dict(
    music=(96, 0, 74),
    lines=[
        dict(say="지역사회복지실천의 원칙과 기술, 틀린 보기만 골라 볼게요!"),
        dict(say="원칙에는 기관간 협력관계 구축, 변화에 초점, 자기결정권 강조가 있어요."),
        dict(say="하지만 지역사회 특성의 일반화는 원칙이 아니에요. 지역마다 특성이 달라요."),
        dict(say="신뢰와 호혜성이 있으면 네트워크가 지속되고, 개인적 이익에 대한 관심은 조직화에 쓰여요."),
        dict(say="임파워먼트는 문제와 권력관계의 연관성을, 사회자본은 서로에 대한 책임감을 깨닫게 해요."),
        dict(say="하지만 연계체계가 느슨해지니 기존의 회의 방식을 고수해야 한다는 말은 틀려요."),
        dict(say="또 네트워크 기술의 이유가 사회적 자본의 감소를 추구하는 거라는 말도 틀려요. 증진을 추구해요."),
        dict(say="그럼 주민이 문제를 함께 풀어 가며 권력구조를 바꾸는 기술은, 주민 조직화일까요 연계일까요?"),
    ],
    scenes=[
        dict(type="hook", lines=[0], headline="지역사회복지 실천<br>[[원칙과 기술]]"),
        dict(type="cards", lines=[1, 2], headline="실천 [[원칙]],<br>맞는 말 · 틀린 말", rows=[
            dict(line=1, title="기관간 협력관계", desc="협력관계를 구축해요", mark="o"),
            dict(line=1, title="변화에 초점", desc="지역사회 변화를 목표로", mark="o"),
            dict(line=1, title="자기결정권 강조", desc="주민이 스스로 결정해요", mark="o"),
            dict(line=2, title="지역 특성의 일반화", desc="지역마다 특성이 달라요", mark="x"),
        ]),
        dict(type="cards", lines=[3, 4], headline="실천 [[기술]],<br>이건 맞아요", rows=[
            dict(line=3, title="네트워크", desc="신뢰와 호혜성이 있으면 지속", mark="o"),
            dict(line=3, title="주민 조직화", desc="개인적 이익 관심을 활용", mark="o"),
            dict(line=4, title="임파워먼트", desc="개인 문제와 권력관계 연결", mark="o"),
            dict(line=4, title="사회자본", desc="서로에 대한 책임감 인식", mark="o"),
        ]),
        dict(type="exam", lines=[5], headline="이 설명,<br>[[맞을까요?]]", tag="제24회 기출 응용 · 지역사회복지론 · 63번",
             html="연계체계가 느슨해지므로<br>[[기존의 회의 방식을<br>고수]]해야 한다", stamp="틀림!", stamp_color=RED, stamp_line=5, stamp_frac=0.7),
        dict(type="exam", lines=[6], headline="이 이유,<br>[[맞을까요?]]", tag="제24회 기출 응용 · 지역사회복지론 · 65번",
             html="네트워크 기술의 이유:<br>[[사회적 자본 감소]] 추구", stamp="틀림!", stamp_color=RED, stamp_line=6, stamp_frac=0.55),
        dict(type="cta", lines=[7], headline=CTA_HEAD, q="함께 푸는 기술은?", buttons=[("주민 조직화?", 0), ("연계?", 1)]),
    ],
)

# ---------------------------------------------------------------- EP5 로스만 모델 (58번)
EPS[5] = dict(
    music=(100, 1, 75),
    lines=[
        dict(say="로스만의 세 가지 지역사회복지 실천모델, 특징을 비교해요!"),
        dict(say="지역사회개발모델은 과정지향적 목표로 지역사회 역량 개발과 통합을 강조해요."),
        dict(say="사회계획모델에서 사회복지사는 분석가, 행정가 역할을 해요."),
        dict(say="사회행동모델은 갈등, 대결, 협상 기법으로 권리를 박탈당한 사람의 이익을 대변해요."),
        dict(say="그래서 개발모델이 과업지향적 목표를 강조한다는 말은 틀려요. 과정지향적 목표예요."),
        dict(say="그럼 갈등과 대결, 협상 기법을 쓰는 모델은, 사회행동일까요 사회계획일까요?"),
    ],
    scenes=[
        dict(type="hook", lines=[0], headline="로스만 모델<br>[[3가지 비교]]"),
        dict(type="cards", lines=[1, 2, 3], headline="로스만<br>[[3가지 모델]]", rows=[
            dict(line=1, title="지역사회개발모델", desc="과정지향적 목표 · 역량과 통합<br>변화 매개체는 과업지향적 소집단"),
            dict(line=2, title="사회계획모델", desc="문제 해결 중심<br>사회복지사는 분석가 · 행정가"),
            dict(line=3, title="사회행동모델", desc="갈등 · 대결 · 협상 기법<br>권리 박탈된 사람의 이익 대변"),
        ]),
        dict(type="exam", lines=[4], headline="이 설명,<br>[[맞을까요?]]", tag="제24회 기출 응용 · 지역사회복지론 · 58번",
             html="지역사회개발모델은<br>[[과업지향적 목표]]를<br>강조한다", stamp="틀림!", stamp_color=RED, stamp_line=4, stamp_frac=0.55),
        dict(type="cta", lines=[5], headline=CTA_HEAD, q="갈등 · 대결 · 협상은?", buttons=[("사회행동?", 0), ("사회계획?", 1)]),
    ],
)

# ---------------------------------------------------------------- EP6 지역사회보장계획 (68번 + 협의체 명칭)
EPS[6] = dict(
    music=(94, 2, 76),
    lines=[
        dict(say="지역사회보장계획, 숫자와 근거법을 정리해요!"),
        dict(say="근거법은 사회복지사업법이 아니라 사회보장급여법이고, 사 년마다 수립해요.",
             cap="근거법은 사회복지사업법이 아니라 사회보장급여법이고, 4년마다 수립해요."),
        dict(say="현재 제삼 기 계획은 이천이십삼 년부터 이천이십육 년까지예요. 협의체 심의 후 지방의회에 보고해요.",
             cap="현재 제3기 계획은 2023년부터 2026년까지예요. 협의체 심의 후 지방의회에 보고해요."),
        dict(say="그래서 오 년마다 수립한다는 설명은 틀려요. 사 년마다 수립해요.", cap="그래서 5년마다 수립한다는 설명은 틀려요. 4년마다 수립해요."),
        dict(say="또 제삼 기 계획이 이천이십칠 년까지라는 설명도 틀려요. 이천이십육 년까지예요.", cap="또 제3기 계획이 2027년까지라는 설명도 틀려요. 2026년까지예요."),
        dict(say="지역사회보장협의체는 이천십오 년 지역사회복지협의체에서 이름이 바뀌었고, 심의와 자문 역할을 해요.",
             cap="지역사회보장협의체는 2015년 지역사회복지협의체에서 바뀌었고, 심의와 자문 역할을 해요."),
        dict(say="그럼 지역사회보장계획의 수립 주기는, 사 년일까요 오 년일까요?", cap="그럼 지역사회보장계획의 수립 주기는, 4년일까요 5년일까요?"),
    ],
    scenes=[
        dict(type="hook", lines=[0], headline="지역사회보장계획<br>[[숫자 정리]]"),
        dict(type="cards", lines=[1, 2], headline="지역사회보장계획<br>[[핵심 정리]]", rows=[
            dict(line=1, title="근거법", desc="사회보장급여법"),
            dict(line=1, title="수립 주기", desc="4년마다 수립"),
            dict(line=2, title="제3기 계획", desc="2023년부터 2026년까지"),
            dict(line=2, title="보고 절차", desc="협의체 심의 후 지방의회 보고"),
        ]),
        dict(type="exam", lines=[3], headline="이 주기,<br>[[맞을까요?]]", tag="제24회 기출 응용 · 지역사회복지론 · 68번",
             html="시 · 군 · 구는 [[5년마다]]<br>지역사회보장계획을<br>수립한다", stamp="틀림!", stamp_color=RED, stamp_line=3, stamp_frac=0.55),
        dict(type="exam", lines=[4], headline="이 기간,<br>[[맞을까요?]]", tag="제24회 기출 응용 · 지역사회복지론 · 68번",
             html="제3기 지역사회보장계획은<br>2023년부터 [[2027년]]까지", stamp="틀림!", stamp_color=RED, stamp_line=4, stamp_frac=0.6),
        dict(type="cards", lines=[5], headline="지역사회보장<br>[[협의체]]", rows=[
            dict(line=5, title="명칭 변경", desc="2015년, 지역사회복지협의체에서<br>지역사회보장협의체로"),
            dict(line=5, title="역할", desc="지역사회보장계획 심의 ·<br>자문 역할을 수행해요"),
        ]),
        dict(type="cta", lines=[6], headline=CTA_HEAD, q="계획 수립 주기는?", buttons=[("4년?", 0), ("5년?", 1)]),
    ],
)

# ---------------------------------------------------------------- EP7 공동모금회·사회적 경제 (70,73번)
EPS[7] = dict(
    music=(98, 3, 77),
    lines=[
        dict(say="사회복지공동모금회와 사회적 경제, 틀린 보기를 찾아요!"),
        dict(say="공동모금회는 사회복지법인이고, 시도 단위로 지회를 둬요."),
        dict(say="모금은 시기에 따라 연중모금과 집중모금으로 나눠요."),
        dict(say="그래서 공동모금회가 관 중심으로 활동한다는 설명은 틀려요. 민간 중심이에요."),
        dict(say="마을기업은 공동체성, 공공성, 지역성, 기업성을 원칙으로 하고, 사회적기업은 취약계층을 도와요."),
        dict(say="협동조합은 조합원 권익옹호와 지역사회 공헌을, 자활기업은 자활공동체에서 바뀐 이름이에요."),
        dict(say="그래서 자활기업의 명칭 변경 근거가 협동조합 기본법이라는 말은 틀려요. 국민기초생활보장법이에요."),
        dict(say="그럼 자활기업의 근거법은, 협동조합 기본법일까요 국민기초생활보장법일까요?"),
    ],
    scenes=[
        dict(type="hook", lines=[0], headline="공동모금회와<br>[[사회적 경제]]"),
        dict(type="cards", lines=[1, 2], headline="사회복지<br>[[공동모금회]]", rows=[
            dict(line=1, title="법적 성격", desc="사회복지법인"),
            dict(line=1, title="조직", desc="시 · 도 단위로 지회를 둬요"),
            dict(line=2, title="모금 방식", desc="연중모금과 집중모금"),
        ]),
        dict(type="exam", lines=[3], headline="이 설명,<br>[[맞을까요?]]", tag="제24회 기출 응용 · 지역사회복지론 · 70번",
             html="공동모금회는<br>중앙회와 시 · 도 지회로 구성된<br>[[관 중심]]의 활동이다", stamp="틀림!", stamp_color=RED, stamp_line=3, stamp_frac=0.55),
        dict(type="cards", lines=[4, 5], headline="[[사회적 경제]]<br>조직", rows=[
            dict(line=4, title="마을기업", desc="공동체성 · 공공성 · 지역성 · 기업성"),
            dict(line=4, title="사회적기업", desc="취약계층에 서비스나 일자리 제공"),
            dict(line=5, title="협동조합", desc="조합원 권익옹호 · 지역사회 공헌"),
            dict(line=5, title="자활기업", desc="자활공동체에서 명칭이 바뀜"),
        ]),
        dict(type="exam", lines=[6], headline="이 근거,<br>[[맞을까요?]]", tag="제24회 기출 응용 · 지역사회복지론 · 73번",
             html="자활기업은<br>[[협동조합 기본법]]에 따라<br>자활공동체에서 명칭 변경", stamp="틀림!", stamp_color=RED, stamp_line=6, stamp_frac=0.6),
        dict(type="cta", lines=[7], headline=CTA_HEAD, q="자활기업의 근거법은?", buttons=[("협동조합법?", 0), ("기초생활법?", 1)]),
    ],
)

# ---------------------------------------------------------------- EP8 아른스테인 주민참여 8단계 (74번)
EPS[8] = dict(
    music=(102, 0, 78),
    lines=[
        dict(say="아른스테인의 주민참여 여덟 단계, 사다리로 정리해요!", cap="아른스테인의 주민참여 8단계, 사다리로 정리해요!"),
        dict(say="위쪽에는 팔 단계 시민통제, 칠 단계 권한위임, 육 단계 협동관계, 오 단계 회유가 있어요.",
             cap="위쪽에는 8단계 시민통제, 7단계 권한위임, 6단계 협동관계, 5단계 회유가 있어요."),
        dict(say="아래쪽은 사 단계 상담과 자문, 삼 단계 정보제공, 그리고 치료와 조작이에요.",
             cap="아래쪽은 4단계 상담과 자문, 3단계 정보제공, 그리고 치료와 조작이에요."),
        dict(say="기출 사례는 결정권은 A시에 있지만 협상이 가능하고 책임을 공유하려 하니, 협동관계예요.",
             cap="기출 사례는 결정권은 A시에 있지만 협상이 가능하고 책임을 공유하려 하니, 협동관계예요."),
        dict(say="그럼 주민이 최종 결정권을 가지는 최고 단계는, 시민통제일까요 권한위임일까요?"),
    ],
    scenes=[
        dict(type="hook", lines=[0], headline="주민참여 8단계,<br>[[아른스테인]]"),
        dict(type="cards", lines=[1], headline="주민참여<br>[[위쪽 4단계]]", rows=[
            dict(line=1, title="시민통제", desc="주민이 최종 결정권을 가져요", badge="8"),
            dict(line=1, title="권한위임", desc="주민이 권한을 위임받아요", badge="7"),
            dict(line=1, title="협동관계", desc="협상하고 책임을 함께 져요", badge="6"),
            dict(line=1, title="회유", desc="의견은 들어도 결정은 행정이", badge="5"),
        ]),
        dict(type="cards", lines=[2], headline="주민참여<br>[[아래쪽 4단계]]", rows=[
            dict(line=2, title="상담 · 자문", desc="의견을 묻지만 반영은 불확실", badge="4"),
            dict(line=2, title="정보제공", desc="일방적으로 알려 줘요", badge="3"),
            dict(line=2, title="치료", desc="불만을 달래는 수준", badge="2"),
            dict(line=2, title="조작", desc="참여처럼 보이게만 해요", badge="1"),
        ]),
        dict(type="exam", lines=[3], headline="이 사례,<br>[[몇 단계일까요?]]", tag="제24회 기출 응용 · 지역사회복지론 · 74번",
             html="A시가 결정권을 가지지만<br>협상이 가능하고<br>책임까지 공유하려 한다", stamp="협동관계!", stamp_color=GRN, stamp_line=3, stamp_frac=0.85),
        dict(type="cta", lines=[4], headline=CTA_HEAD, q="최고 단계는?", buttons=[("시민통제?", 0), ("권한위임?", 1)]),
    ],
)

# ---------------------------------------------------------------- EP9 지방분권·활성화 과제 (67,75번)
EPS[9] = dict(
    music=(96, 1, 79),
    lines=[
        dict(say="지방분권의 중요성과 지역사회복지 활성화 과제를 정리해요!"),
        dict(say="지방분권은 지방정부의 권한과 책임성을 강화하고, 주민 욕구 중심의 맞춤형 서비스를 줘요."),
        dict(say="또 주민 참여로 연대를 강화하고, 지역 실정에 맞는 복지 집행체계를 만들어요."),
        dict(say="과제는 민간영역의 자율적 발전, 통합돌봄 기반 구축, 조직 간 협력이에요."),
        dict(say="하지만 특정 계층 중심의 수단적 운동을 활성화하는 건 과제가 아니에요."),
        dict(say="그럼 지역사회 중심의 통합돌봄과 사회서비스 기반 구축은, 활성화 과제일까요 아닐까요?"),
    ],
    scenes=[
        dict(type="hook", lines=[0], headline="지방분권과<br>[[활성화 과제]]"),
        dict(type="cards", lines=[1, 2], headline="지방분권이<br>[[중요한 이유]]", rows=[
            dict(line=1, title="권한과 책임성 강화", desc="지방정부가 책임을 져요", mark="o"),
            dict(line=1, title="맞춤형 복지서비스", desc="주민 욕구 중심으로 제공", mark="o"),
            dict(line=2, title="주민 참여와 연대", desc="참여로 연대를 강화해요", mark="o"),
            dict(line=2, title="효율적인 집행체계", desc="지역 실정에 맞게 구축", mark="o"),
        ]),
        dict(type="cards", lines=[3, 4], headline="활성화 과제,<br>[[맞는 말 · 틀린 말]]", rows=[
            dict(line=3, title="민간영역 자율 발전", desc="자율적으로 발전해요", mark="o"),
            dict(line=4, title="특정 계층 중심 운동", desc="수단적 운동은 과제가 아니에요", mark="x"),
            dict(line=3, title="통합돌봄 기반 구축", desc="지역사회 중심 사회서비스", mark="o"),
            dict(line=3, title="자원 활용과 협력", desc="조직 간 유기적 협력", mark="o"),
        ]),
        dict(type="cta", lines=[5], headline=CTA_HEAD, q="통합돌봄 기반 구축은?", buttons=[("과제?", 0), ("아님?", 1)]),
    ],
)
