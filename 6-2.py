# 두 series 객체의 덧셈 연산(동일 크기)
import pandas as pd
score1=pd.Series({'kor':80,'eng':90, 'math':85})
score2=pd.Series({'eng':70, 'kor':75, 'math':85})
res=score1+score2
print(res)
#다른크기
score3=pd.Series({'kor':80,'eng':90, 'math':85})
score4=pd.Series({'eng':70, 'kor':75})
res2=score3+score4
print(res2)