#인덱스 재배열

import pandas as pd
df=pd.DataFrame(data = [["홍길동", 80,90,85],
                        ["이기자", 70,75,85],
                        ["최신", 100, 90, 95]],
                        index=[1,2,3], columns=["name", "kor", "eng", "mat"])

df2 = df.reindex([2,1,3])
print(df2)

df3=df.reindex([2,3,4,5], fill_value=0)
print(df3)