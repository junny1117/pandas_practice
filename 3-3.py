#행 선택
import pandas as pd

df=pd.DataFrame({'name':['hong', 'kim', 'heo'], 'kor' : [80, 90, 75], 'eng' : [80, 95, 100]})

print (df)


#loc를 이용한 행 선택 - 1개의 행
heo_data=df.loc[2]
print(heo_data)
##loc를 이용한 행 선택 - 여러개의 행
all_data=df.loc[0:2]
print(all_data)

##iloc를 이용한 행 선택 - 1개의 행
heo_data2=df.iloc[2]
print(heo_data2)
##iloc를 이용한 행 선택 - 여러개의 행
all_data2=df.iloc[-1]
print(all_data2)

