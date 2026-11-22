# -*- coding: utf-8 -*-
EPS = {}
EPS[1] = dict(music=(96, 0, 5), lines=[dict(say="새 캐릭터 미리보기예요!"), dict(say="귀엽게 인사해요."), dict(say="정답은 하나예요!", pause=2.3)],
    scenes=[dict(type="hook", lines=[0], headline="새 캐릭터<br>[[미리보기]]"),
            dict(type="cta", lines=[1, 2], headline="[[댓글]]로 정답을<br>맞혀 보세요!", q="테스트 질문?", buttons=[("하나", 0), ("둘", 1)], reveal=dict(line=2, answer=0))])
