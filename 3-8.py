#행과 열 위치 변경하기
import pandas as pd
df=pd.DataFrame({'name':['hong', 'kim', 'heo'],
'kor' : [80, 90, 75], 'eng' : [80, 95, 100]})

print (df)

df_tran=df.transpose( )
print(df_tran)