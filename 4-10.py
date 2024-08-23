#상관계수 구하기

import pandas as pd
df=pd.DataFrame({'name':['hong', 'kim', 'heo'],
'kor' : [80, 90, 75], 'eng' : [80, 95, 100]})

print (df)

df_c = df.corr()
df_c2 = df.corr(method = 'pearson')
df_c3 = df.corr(method = 'spearman')
df_c4 = df.corr(method = 'kendall')

print(df_c)
print(df_c2)
print(df_c3)
print(df_c4)