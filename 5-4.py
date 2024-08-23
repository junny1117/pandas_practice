#인덱스 배정, 설정

import pandas as pd
df=pd.DataFrame(data = [["홍길동", 80,90,85],
                        ["이기자", 70,75,85],
                        ["최신", 100, 90, 95]],
                        columns=["name", "kor", "eng", "mat"])

print(df)

df2=df.index=[1,2,3]
print(df2)

#행 인덱스 설정
df3 = df.set_index("name")
print(df3)

#인덱스 초기화

df4= df3.reset_index(drop=True)
print(df4)