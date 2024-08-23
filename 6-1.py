#Series 숫자간 연산
import pandas as pd
score = pd.Series({'kor':90, 'eng':100, 'math':85,'sec':96})
print(score)
Conversion_score = score*0.2
print('\n')
print(Conversion_score)