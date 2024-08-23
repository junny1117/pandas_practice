#표준편차 구하기

import pandas as pd

df = pd.DataFrame({'x':[1,2,None,3],
                   'y':[4,3,8,4]})

df_s = df.std()

print(df_s)