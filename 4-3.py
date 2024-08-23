#평균값 구하기(행)
import pandas as pd

df = pd.DataFrame({'x':[1,2,None,3],
                   'y':[4,3,8,4]})

df_m=df.mean(axis=1)
print(df_m)