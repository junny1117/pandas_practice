#DataFrame 생성(딕셔너리 활용)

import pandas as pd
dic = {'name':['hong', 'kim','heo'],
       'kor':[80, 90, 75],
       'eng':[80,95,100]}
df = pd.DataFrame(dic)
print(df)