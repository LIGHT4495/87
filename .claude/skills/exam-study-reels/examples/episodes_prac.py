# -*- coding: utf-8 -*-
# 사회복지실천론 (제24회 2교시 1~25번) - paper/orange motion style
# scene types: hook / cards / exam / cta ; markup [[accent]] in headline and exam html
EPS = {}
RED = "#e8431a"; GRN = "#12a37f"

# ---------------------------------------------------------------- EP1 목적·이념 (1,2번)
EPS[1] = dict(
    music=(92, 0, 41),
    lines=[
        dict(say="사회복지실천의 목적과 이념, 헷갈리지 않는 방법이 있어요!"),
        dict(say="개인과 가족의 문제해결과 대처 능력 향상을 돕고, 사회정책 발전에도 기여해요."),
        dict(say="또 개인과 사회 사이의 유익한 상호작용을 촉진하죠."),
        dict(say="하지만 클라이언트에게 무조건적인 원조를 제공하는 건, 목적이 아니에요."),
        dict(say="다원주의는 임파워먼트 논의에, 인도주의는 타인을 위한 봉사정신에 영향을 줬어요."),
        dict(say="민주주의는 자기결정권 강조에, 사회진화론은 사회통제적 성격이 강해요."),
        dict(say="그럼 자기결정권 강조에 영향을 준 이념은, 민주주의일까요 인도주의일까요?"),
    ],
    scenes=[
        dict(type="hook", lines=[0], headline="사회복지실천의<br>[[목적과 이념]]"),
        dict(type="cards", lines=[1, 2], headline="실천의 목적,<br>[[이건 맞아요]]", rows=[
            dict(line=1, title="문제해결 · 대처 능력", desc="개인 · 집단 · 가족의 능력 향상", mark="o"),
            dict(line=1, title="사회정책 발전", desc="사회정책의 개발과 발전에 기여", mark="o"),
            dict(line=2, title="상호작용 촉진", desc="개인과 사회 간 유익한 상호작용", mark="o"),
        ]),
        dict(type="exam", lines=[3], headline="이 목적,<br>[[맞을까요?]]", tag="제24회 기출 응용 · 실천론 · 1번",
             html="클라이언트에게<br>[[무조건적인 원조]]를 제공한다", stamp="틀림!", stamp_color=RED, stamp_line=3, stamp_frac=0.7),
        dict(type="cards", lines=[4, 5], headline="사회복지실천의<br>[[이념]]", rows=[
            dict(line=4, title="다원주의", desc="임파워먼트 논의에 영향"),
            dict(line=4, title="인도주의", desc="타인을 위한 봉사정신"),
            dict(line=5, title="민주주의", desc="자기결정권 강조에 영향"),
            dict(line=5, title="사회진화론", desc="사회통제적 성격이 강함"),
        ]),
        dict(type="cta", lines=[6], headline="[[댓글]]로 정답을<br>알려 주세요!", q="자기결정권 이념은?", buttons=[("민주주의?", 0), ("인도주의?", 1)]),
    ],
)

# ---------------------------------------------------------------- EP2 인보관 vs COS (3번)
EPS[2] = dict(
    music=(88, 1, 42),
    lines=[
        dict(say="인보관운동과 자선조직협회, 뭐가 다를까요?"),
        dict(say="인보관운동은 빈곤을 산업화로 인한 착취의 결과로 보고, 빈민과 함께 살며 지역사회를 개선했어요. 집단사회사업에 영향을 줬죠."),
        dict(say="자선조직협회는 우애방문으로 빈민을 돕고 중복 구제를 막았어요. 개별사회사업에 영향을 줬죠."),
        dict(say="그래서 인보관운동이 사회진화론에 근거했다는 설명은 틀려요. 사회진화론은 자선조직협회 쪽이에요."),
        dict(say="그럼 집단사회사업에 영향을 준 운동은, 인보관일까요 자선조직협회일까요?"),
    ],
    scenes=[
        dict(type="hook", lines=[0], headline="[[인보관운동]] vs<br>[[자선조직협회]]"),
        dict(type="cards", lines=[1, 2], headline="두 운동,<br>[[이렇게 달라요]]", rows=[
            dict(line=1, title="인보관운동", desc="빈민과 함께 거주 · 사회환경 개선<br>집단사회사업에 영향"),
            dict(line=2, title="자선조직협회", desc="우애방문 · 중복 구제 방지<br>개별사회사업에 영향"),
        ]),
        dict(type="exam", lines=[3], headline="이 설명,<br>[[맞을까요?]]", tag="제24회 기출 응용 · 실천론 · 3번",
             html="[[인보관운동]]은<br>사회진화론에 근거했다", stamp="틀림!", stamp_color=RED, stamp_line=3, stamp_frac=0.55),
        dict(type="cta", lines=[4], headline="[[댓글]]로 정답을<br>알려 주세요!", q="집단사회사업에 영향은?", buttons=[("인보관?", 0), ("자선조직?", 1)]),
    ],
)

# ---------------------------------------------------------------- EP3 전문직·가치 (4,5번)
EPS[3] = dict(
    music=(90, 2, 43),
    lines=[
        dict(say="전문직의 조건과 가치, 한 번에 정리해요!"),
        dict(say="그린우드는 전문직 속성으로 체계적 이론, 전문적 권위, 사회적 승인을 꼽았어요."),
        dict(say="여기에 윤리강령과 전문직 문화까지, 모두 다섯 가지예요."),
        dict(say="레비는 가치를 사람우선, 결과우선, 수단우선으로 나눴어요. 사람우선은 개별성과 소속의 욕구예요."),
        dict(say="결과우선은 동등한 기회와 차별 금지, 수단우선은 비밀보장과 비심판적 태도예요."),
        dict(say="그래서 차별 금지를 수단우선 가치로 묶으면 틀려요. 차별 금지는 결과우선 가치예요."),
        dict(say="그럼 소속의 욕구는, 사람우선 가치일까요 결과우선 가치일까요?"),
    ],
    scenes=[
        dict(type="hook", lines=[0], headline="전문직의 조건과<br>[[가치]] 정리!"),
        dict(type="cards", lines=[1], headline="그린우드의<br>[[전문직 속성]] ①", rows=[
            dict(line=1, title="체계적 이론", desc="전문직만의 지식 체계"),
            dict(line=1, title="전문적 권위", desc="전문성에 바탕을 둔 권위"),
            dict(line=1, title="사회적 승인", desc="사회가 전문성을 인정"),
        ]),
        dict(type="cards", lines=[2], headline="그린우드의<br>[[전문직 속성]] ②", rows=[
            dict(line=2, title="윤리강령", desc="전문직의 행동 기준", badge="04"),
            dict(line=2, title="전문직 문화", desc="고유의 가치 · 규범 · 상징", badge="05"),
        ]),
        dict(type="cards", lines=[3, 4], headline="레비의<br>[[3가지 가치]]", rows=[
            dict(line=3, title="사람우선", desc="개별성 · 소속의 욕구"),
            dict(line=4, title="결과우선", desc="동등한 기회 · 차별 금지"),
            dict(line=4, title="수단우선", desc="비밀보장 · 비심판적 태도"),
        ]),
        dict(type="exam", lines=[5], headline="이 연결,<br>[[맞을까요?]]", tag="제24회 기출 응용 · 실천론 · 5번",
             html="[[수단우선]] 가치 -<br>차별 금지", stamp="틀림!", stamp_color=RED, stamp_line=5, stamp_frac=0.5),
        dict(type="cta", lines=[6], headline="[[댓글]]로 정답을<br>알려 주세요!", q="소속의 욕구는?", buttons=[("사람우선?", 0), ("결과우선?", 1)]),
    ],
)

# ---------------------------------------------------------------- EP4 윤리적 원칙 우선순위 (7번)
EPS[4] = dict(
    music=(94, 3, 44),
    lines=[
        dict(say="윤리적 원칙의 우선순위, 순서가 늘 헷갈리죠?"),
        dict(say="가장 먼저 생명 보호, 그다음이 평등과 불평등 원칙이에요."),
        dict(say="세 번째는 자율성과 자유, 네 번째는 최소 손실이에요."),
        dict(say="그다음 삶의 질, 사생활과 비밀보장, 마지막이 진실성과 완전한 공개예요."),
        dict(say="기출은 이 네 개를 순서대로 고르는 문제였어요. 평등과 불평등, 자율성과 자유, 최소 손실, 삶의 질 순서가 정답이에요."),
        dict(say="그럼 최소 손실 원칙과 삶의 질 원칙 중, 더 먼저인 건 무엇일까요?"),
    ],
    scenes=[
        dict(type="hook", lines=[0], headline="윤리적 원칙의<br>[[우선순위]]는?"),
        dict(type="cards", lines=[1, 2], headline="우선순위<br>[[1위 ~ 4위]]", rows=[
            dict(line=1, title="생명 보호", desc="가장 먼저 지켜요"),
            dict(line=1, title="평등과 불평등", desc="같은 사람은 같게 대우"),
            dict(line=2, title="자율성과 자유", desc="스스로 결정할 권리"),
            dict(line=2, title="최소 손실", desc="해악이 가장 적은 선택"),
        ]),
        dict(type="cards", lines=[3], headline="우선순위<br>[[5위 ~ 7위]]", rows=[
            dict(line=3, title="삶의 질", desc="삶의 질을 높이는 선택", badge="05"),
            dict(line=3, title="사생활과 비밀보장", desc="사생활과 비밀 지키기", badge="06"),
            dict(line=3, title="진실성과 완전한 공개", desc="정보를 숨김없이 공개", badge="07"),
        ]),
        dict(type="exam", lines=[4], headline="기출의<br>[[정답 순서]]", tag="제24회 기출 응용 · 실천론 · 7번",
             html="[[평등과 불평등]]<br>→ 자율성과 자유<br>→ 최소 손실 → 삶의 질", stamp="정답 순서!", stamp_color=GRN, stamp_line=4, stamp_frac=0.85),
        dict(type="cta", lines=[5], headline="[[댓글]]로 정답을<br>알려 주세요!", q="더 먼저인 원칙은?", buttons=[("최소 손실?", 0), ("삶의 질?", 1)]),
    ],
)

# ---------------------------------------------------------------- EP5 실천현장 (10번)
EPS[5] = dict(
    music=(90, 0, 45),
    lines=[
        dict(say="실천현장 분류, 1차와 2차가 헷갈리죠?"),
        dict(say="1차 현장은 사회복지가 주된 기능인 곳이에요. 사회복지관이나 복지시설이 대표적이죠."),
        dict(say="2차 현장은 사회복지가 부차적인 기능인 곳이에요. 학교, 병원, 기업, 교정시설이 있어요."),
        dict(say="재가노인복지시설은, 집에서 다니며 이용하는 이용시설이고,"),
        dict(say="청소년자립지원관은, 입소해서 지내는 생활시설이에요."),
        dict(say="그리고 사회복지협의회와 공동모금회를 공공 실천현장이라고 하면 틀려요. 이곳들은 민간 현장이에요."),
        dict(say="그럼 학교와 병원은, 1차 현장일까요 2차 현장일까요?"),
    ],
    scenes=[
        dict(type="hook", lines=[0], headline="실천현장,<br>[[1차 vs 2차]]"),
        dict(type="cards", lines=[1, 2], headline="[[1차 현장]]과<br>[[2차 현장]]", rows=[
            dict(line=1, title="1차 현장", desc="사회복지가 주된 기능<br>사회복지관 · 복지시설"),
            dict(line=2, title="2차 현장", desc="사회복지가 부차적 기능<br>학교 · 병원 · 기업 · 교정"),
        ]),
        dict(type="cards", lines=[3, 4], headline="[[이용시설]] vs<br>[[생활시설]]", rows=[
            dict(line=3, title="재가노인복지시설", desc="집에서 다니며 이용하는<br>이용시설"),
            dict(line=4, title="청소년자립지원관", desc="입소해서 지내는<br>생활시설"),
        ]),
        dict(type="exam", lines=[5], headline="이 분류,<br>[[맞을까요?]]", tag="제24회 기출 응용 · 실천론 · 10번",
             html="사회복지협의회, 공동모금회는<br>[[공공 실천현장]]이다", stamp="틀림!", stamp_color=RED, stamp_line=5, stamp_frac=0.6),
        dict(type="cta", lines=[6], headline="[[댓글]]로 정답을<br>알려 주세요!", q="학교와 병원은?", buttons=[("1차?", 0), ("2차?", 1)]),
    ],
)

# ---------------------------------------------------------------- EP6 강점·역량강화·통합적 접근 (11,13,14번)
EPS[6] = dict(
    music=(96, 1, 46),
    lines=[
        dict(say="강점관점, 역량강화, 통합적 접근, 한 번에 정리해요!"),
        dict(say="병리관점은, 전문가의 판단을 중심으로 문제를 해결해요."),
        dict(say="강점관점은, 모든 클라이언트에게 강점이 있고 환경에도 자원이 있다고 봐요."),
        dict(say="그래서 전문가의 판단 중심 해결은, 강점관점이 아니라 병리관점이에요."),
        dict(say="역량강화는 능력과 영향을 강조하고, 협력관계를 만들고, 참여를 중시해요."),
        dict(say="병리학적 관점에 기반했다는 말은 틀려요. 강점관점에 가깝죠."),
        dict(say="통합적 접근은 다양한 이론을 쓰고, 개인과 환경, 여러 수준의 체계에 개입해요."),
        dict(say="일반주의를 지양한다는 말은 틀려요. 통합적 접근은 일반주의를 지향해요."),
        dict(say="그럼 클라이언트를 선택과 결정의 주체로 보는 관점은, 강점일까요 병리일까요?"),
    ],
    scenes=[
        dict(type="hook", lines=[0], headline="강점관점 · 역량강화<br>[[통합적 접근]]"),
        dict(type="cards", lines=[1, 2], headline="[[병리관점]] vs<br>[[강점관점]]", rows=[
            dict(line=1, title="병리관점", desc="전문가의 판단 중심으로<br>문제를 해결"),
            dict(line=2, title="강점관점", desc="누구나 강점이 있고 환경엔 자원이<br>클라이언트가 결정의 주체"),
        ]),
        dict(type="exam", lines=[3], headline="이 설명,<br>[[맞을까요?]]", tag="제24회 기출 응용 · 실천론 · 11번",
             html="강점관점은<br>[[전문가의 판단]] 중심으로<br>문제를 해결한다", stamp="틀림!", stamp_color=RED, stamp_line=3, stamp_frac=0.45),
        dict(type="cards", lines=[4, 5], headline="[[역량강화]]<br>실천", rows=[
            dict(line=4, title="능력과 영향 강조", desc="클라이언트의 힘을 믿어요", mark="o"),
            dict(line=4, title="협력관계 형성", desc="사회복지사와 함께 가요", mark="o"),
            dict(line=4, title="참여 중시", desc="클라이언트가 직접 참여", mark="o"),
            dict(line=5, title="병리학적 관점 기반", desc="강점관점에 가까워요", mark="x"),
        ]),
        dict(type="cards", lines=[6, 7], headline="[[통합적 접근]]", rows=[
            dict(line=6, title="다양한 이론 사용", desc="특정 이론에 얽매이지 않아요", mark="o"),
            dict(line=6, title="개인 · 환경 함께 고려", desc="복합적으로 살펴봐요", mark="o"),
            dict(line=6, title="여러 수준의 체계 개입", desc="개인 · 가족 · 집단 · 지역사회", mark="o"),
            dict(line=7, title="일반주의 지양", desc="일반주의를 지향해요", mark="x"),
        ]),
        dict(type="cta", lines=[8], headline="[[댓글]]로 정답을<br>알려 주세요!", q="결정의 주체로 보는 건?", buttons=[("강점?", 0), ("병리?", 1)]),
    ],
)

# ---------------------------------------------------------------- EP7 체계이론·4체계 (12,15번)
EPS[7] = dict(
    music=(92, 2, 47),
    lines=[
        dict(say="체계이론과 4체계 모델, 용어가 자꾸 꼬이죠?"),
        dict(say="순환적 인과성은 행동을 서로에 대한 반응으로 보고, 홀론은 상위이면서 동시에 하위체계예요."),
        dict(say="환경과 자유롭게 교환하는 체계는 개방체계, 밖에서 들어오는 에너지와 정보는 투입이에요."),
        dict(say="그래서 자유롭게 교환하는 체계를 폐쇄체계라고 하면 틀려요."),
        dict(say="핀커스와 미나한의 4체계는, 변화매개체계, 클라이언트체계, 표적체계, 행동체계예요."),
        dict(say="그래서 클라이언트가 변화의 대상이면 행동체계가 된다는 말은 틀려요. 그땐 표적체계가 돼요."),
        dict(say="그럼 변화가 필요한 대상은, 표적체계일까요 행동체계일까요?"),
    ],
    scenes=[
        dict(type="hook", lines=[0], headline="체계이론과<br>[[4체계 모델]]"),
        dict(type="cards", lines=[1, 2], headline="체계이론<br>[[핵심 용어]]", rows=[
            dict(line=1, title="순환적 인과성", desc="행동은 서로에 대한 반응"),
            dict(line=1, title="홀론", desc="상위이면서 동시에 하위체계"),
            dict(line=2, title="개방체계", desc="환경과 자유롭게 교환"),
            dict(line=2, title="투입", desc="밖에서 들어오는 에너지 · 정보"),
        ]),
        dict(type="exam", lines=[3], headline="이 설명,<br>[[맞을까요?]]", tag="제24회 기출 응용 · 실천론 · 12번",
             html="환경과 자유롭게 교환하는<br>체계를 [[폐쇄체계]]라고 한다", stamp="틀림!", stamp_color=RED, stamp_line=3, stamp_frac=0.7),
        dict(type="cards", lines=[4], headline="핀커스 · 미나한<br>[[4체계]]", rows=[
            dict(line=4, title="변화매개체계", desc="사회복지사와 사회복지기관"),
            dict(line=4, title="클라이언트체계", desc="서비스를 요청하고 계약한 사람"),
            dict(line=4, title="표적체계", desc="변화가 필요한 대상"),
            dict(line=4, title="행동체계", desc="변화를 위해 함께 노력"),
        ]),
        dict(type="exam", lines=[5], headline="이 설명,<br>[[맞을까요?]]", tag="제24회 기출 응용 · 실천론 · 15번",
             html="클라이언트가 변화의 대상이면<br>[[행동체계]]가 된다", stamp="틀림!", stamp_color=RED, stamp_line=5, stamp_frac=0.5),
        dict(type="cta", lines=[6], headline="[[댓글]]로 정답을<br>알려 주세요!", q="변화가 필요한 대상은?", buttons=[("표적?", 0), ("행동?", 1)]),
    ],
)

# ---------------------------------------------------------------- EP8 전문적 관계 (16~19번)
EPS[8] = dict(
    music=(88, 3, 48),
    lines=[
        dict(say="전문적 관계에서 헷갈리는 개념, 전이와 역전이!"),
        dict(say="비스텍의 통제된 정서적 관여는, 감정을 민감하게 이해하되 내 반응은 목적에 맞게 조절하는 거예요."),
        dict(say="의도적 감정표현과 수용도 관계 원칙에 포함돼요."),
        dict(say="하지만 펄만의 전문적 관계에서, 사회복지사가 감정과 반응을 통제하지 않는다는 설명은 틀려요."),
        dict(say="전이는, 클라이언트가 과거 관계의 감정을 사회복지사에게 옮기는 거예요. 아버지에게 폭력을 겪은 클라이언트가 남성 사회복지사를 두려워하는 경우죠."),
        dict(say="역전이는 반대로, 사회복지사가 자신의 감정을 클라이언트에게 옮기는 거예요."),
        dict(say="그럼 친구들이 너를 따돌린다고 생각해서 속상했구나, 라는 말은 반영일까요 직면일까요?"),
    ],
    scenes=[
        dict(type="hook", lines=[0], headline="전문적 관계,<br>[[전이 vs 역전이]]"),
        dict(type="cards", lines=[1, 2], headline="비스텍의<br>[[관계 원칙]]", rows=[
            dict(line=1, title="통제된 정서적 관여", desc="민감하게 이해 · 목적에 맞게 조절"),
            dict(line=2, title="의도적 감정표현", desc="감정을 자유롭게 표현하게 해요"),
            dict(line=2, title="수용", desc="있는 그대로 받아들여요"),
        ]),
        dict(type="exam", lines=[3], headline="이 설명,<br>[[맞을까요?]]", tag="제24회 기출 응용 · 실천론 · 18번",
             html="사회복지사는 자신의<br>[[감정과 반응]]을 통제하지 않는다", stamp="틀림!", stamp_color=RED, stamp_line=3, stamp_frac=0.75),
        dict(type="cards", lines=[4, 5], headline="[[전이]]와<br>[[역전이]]", rows=[
            dict(line=4, title="전이", desc="클라이언트가 과거 관계의 감정을<br>사회복지사에게 투사"),
            dict(line=5, title="역전이", desc="사회복지사가 자신의 감정을<br>클라이언트에게 투사"),
        ]),
        dict(type="cta", lines=[6], headline="[[댓글]]로 정답을<br>알려 주세요!", q="'속상했구나'는?", buttons=[("반영?", 0), ("직면?", 1)]),
    ],
)

# ---------------------------------------------------------------- EP9 실천과정 (20,22,23번)
EPS[9] = dict(
    music=(94, 0, 49),
    lines=[
        dict(say="실천과정, 사정부터 평가까지 한 번에 정리해요!"),
        dict(say="사정은 개입 전에 모은 자료를 분석해, 문제와 욕구, 자원과 강점을 이해하는 단계예요."),
        dict(say="계획과 계약에서는 목표를 정하고, 역할과 기간, 빈도를 약속해요."),
        dict(say="개입으로 서비스를 실행하고, 평가로 효과를 확인해요."),
        dict(say="기출에서 계약 내용으로 제시한 다섯 가지는, 모두 맞아요."),
        dict(say="평가에는 형성평가와 총괄평가가 있어요. 형성평가는 수행 중 문제를 찾아 고치고, 총괄평가는 끝난 뒤 효과를 판단해요."),
        dict(say="그럼 프로그램 수행 중 문제점을 고쳐 가는 평가는, 형성평가일까요 총괄평가일까요?"),
    ],
    scenes=[
        dict(type="hook", lines=[0], headline="실천과정,<br>[[사정]]부터 [[평가]]까지"),
        dict(type="cards", lines=[1, 2, 3], headline="실천과정<br>[[핵심 단계]]", rows=[
            dict(line=1, title="사정", desc="문제 · 욕구 · 자원 · 강점 이해"),
            dict(line=2, title="계획 · 계약", desc="목표 · 역할 · 기간과 빈도 약속"),
            dict(line=3, title="개입", desc="계획에 따라 서비스 실행"),
            dict(line=3, title="평가", desc="개입의 효과를 확인"),
        ]),
        dict(type="exam", lines=[4], headline="계약에<br>[[포함될까요?]]", tag="제24회 기출 응용 · 실천론 · 22번",
             html="개입방법 · 두 사람의 역할<br>개입기간과 빈도<br>구체적 서비스 목표", stamp="5개 모두!", stamp_color=GRN, stamp_line=4, stamp_frac=0.8),
        dict(type="cards", lines=[5], headline="[[형성평가]] vs<br>[[총괄평가]]", rows=[
            dict(line=5, title="형성평가", desc="수행 중 문제점을 찾아<br>수정 · 보완"),
            dict(line=5, title="총괄평가", desc="종료 후 효과와<br>목표 달성 판단"),
        ]),
        dict(type="cta", lines=[6], headline="[[댓글]]로 정답을<br>알려 주세요!", q="수행 중 개선하는 평가는?", buttons=[("형성?", 0), ("총괄?", 1)]),
    ],
)

# ---------------------------------------------------------------- EP10 개입기술·사례관리 (21,24,25번)
EPS[10] = dict(
    music=(90, 2, 50),
    lines=[
        dict(say="개입기술과 사례관리, 마지막 정리예요!"),
        dict(say="재보증은 자신감을 높이는 기술, 모델링은 바람직한 행동을 모방하게 하는 기술이에요."),
        dict(say="인지재구조화는 왜곡된 사고를 바꾸고, 소거는 강화를 주지 않아 행동을 사라지게 해요."),
        dict(say="하지만 부정적 감정을 표출하게 해 강도를 약화시키는 건, 일반화가 아니라 환기예요."),
        dict(say="사례관리자는, 클라이언트의 이익을 대변하고 권리를 보호하는 옹호자가 돼요."),
        dict(say="자원을 연결하는 중개자, 역량을 키우는 능력부여자 역할도 해요."),
        dict(say="사례관리가 등장한 배경은, 대규모 시설의 부작용을 줄이고 지역사회 복귀를 돕는 탈시설화예요."),
        dict(say="그럼 클라이언트의 이익을 대변하는 역할은, 옹호자일까요 중개자일까요?"),
    ],
    scenes=[
        dict(type="hook", lines=[0], headline="개입기술과<br>[[사례관리]]"),
        dict(type="cards", lines=[1, 2], headline="개입 기술,<br>[[이건 맞아요]]", rows=[
            dict(line=1, title="재보증", desc="신뢰를 표현해 자신감을 높여요"),
            dict(line=1, title="모델링", desc="바람직한 행동을 모방하게 해요"),
            dict(line=2, title="인지재구조화", desc="왜곡된 사고를 바꿔요"),
            dict(line=2, title="소거", desc="강화를 주지 않아 행동이 사라져요"),
        ]),
        dict(type="exam", lines=[3], headline="이 설명,<br>[[맞을까요?]]", tag="제24회 기출 응용 · 실천론 · 21번",
             html="[[일반화]]는 부정적 감정을<br>표출하게 해 강도를 약화시킨다", stamp="틀림!", stamp_color=RED, stamp_line=3, stamp_frac=0.7),
        dict(type="cards", lines=[4, 5], headline="[[사례관리자]]의<br>역할", rows=[
            dict(line=4, title="옹호자", desc="이익을 대변하고 권리를 보호"),
            dict(line=5, title="중개자", desc="필요한 자원과 서비스를 연결"),
            dict(line=5, title="능력부여자", desc="스스로 해결할 힘을 키워요"),
        ]),
        dict(type="exam", lines=[6], headline="사례관리의<br>[[등장배경]]", tag="제24회 기출 응용 · 실천론 · 25번",
             html="대규모 시설의 관료주의 해소<br>지역사회 복귀 어려움 개선", stamp="탈시설화!", stamp_color=GRN, stamp_line=6, stamp_frac=0.85),
        dict(type="cta", lines=[7], headline="[[댓글]]로 정답을<br>알려 주세요!", q="이익을 대변하는 역할은?", buttons=[("옹호자?", 0), ("중개자?", 1)]),
    ],
)
