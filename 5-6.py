#인덱스 정렬
#행 기준
import pandas as pd
df=pd.DataFrame(data = [["홍길동", 80,90,85],
                        ["이기자", 70,75,85],
                        ["최신", 100, 90, 95]],
                        index=[1,2,3], columns=["name", "kor", "eng", "mat"])

df2=df.sort_index(ascending=True)
print(df2)

#열 기준

df3=df.sort_values("eng")
print(df3)

df4=df.sort_values(["eng", "mat"], ascending=False)
print(df4)