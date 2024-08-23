#서로 크기가 다른 두 Series 객체의 덧셈 연산 수행하기(add 함수 이용)

import pandas as pd
score1=pd.Series({'kor':80, 'eng':90, 'math':85})
score2=pd.Series({'eng':70, 'kor':75})
res=score1.add(score2, fill_value=0)
print(res)