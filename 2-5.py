#색인 객체 생성 후 Series 객체에 할당하기

import pandas as pd
#색인 객체 만들기
stud_id = pd.Index(['name', 'kor', 'eng'])
print(stud_id)

#Series 객체 만들기
stud_data=pd.Series([['hong', 'kim', 'heo'], [80,75,90], [80,90,70]])
print(stud_data)

stud_data.index=stud_id
print(stud_data)