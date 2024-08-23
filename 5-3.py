#불리언 인덱싱

import pandas as pd
df=pd.DataFrame(data = [["홍길동", 80,90,85],
                        ["이기자", 70,75,85],
                        ["최신", 100, 90, 95]],
                        index=[1,2,3], columns=["name", "kor", "eng", "mat"])

print(df.eng>=90)
print(df[df.eng>=90])
print([df.eng>=90,["name","eng"]])