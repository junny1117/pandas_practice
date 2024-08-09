#원소 선택

import pandas as pd

df=pd.DataFrame({'name':['hong', 'kim', 'heo'], 'kor' : [80, 90, 75], 'eng' : [80, 95, 100]})

print (df)


#loc 이용
kim_kor=df.loc[1,'kor']
print(kim_kor)

#iloc 이용
kim_kor2=df.iloc[1,1]
print(kim_kor2)