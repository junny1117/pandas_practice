#행 추가/삭제

import pandas as pd

df=pd.DataFrame({'name':['hong','kim','heo'], 'kor':[80,90,75],'eng':[80,95,100]})

print(df)

df.loc[3] = ['song', 95, 80]

print(df)

df.drop([3], axis =0, inplace=True)

print (df)
