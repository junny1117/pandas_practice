#열 추가 삭제

import pandas as pd

df = pd.DataFrame({'name':['hong', 'kim', 'heo'], 'kor':[80,90,75], 'eng':[80,95,100]})

print (df)

df['math']=[70,85,90]

print(df)

df.drop('eng', axis =1, inplace=True)

print (df)