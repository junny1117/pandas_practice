#열 선택
import pandas as pd

df=pd.DataFrame({'name':['hong', 'kim', 'heo'], 'kor' : [80, 90, 75], 'eng' : [80, 95, 100]})

print (df)


#한개의 열 선택
eng_data=df['eng']
print(eng_data)
#여러개의 열 선택
name_eng_data=df[['name', 'eng']]
print(name_eng_data)

