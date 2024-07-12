#Serirs 데이터 생성

import pandas as pd
dic = {'name':['hong', 'kim', 'heo',], 'kor':[80, 90, 75], 'eng':[60, 70, 90]}
ser_data = pd.Series(dic)
print(ser_data)