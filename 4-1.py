#평균값 구하기(열)
import pandas as pd

df = pd.DataFrame({'X':[1,2,None,3],'Y':[4,3,8,4]})

df_mean =  df.mean()

df_m = df.mean(skipna=False)

print(df)
print(df_mean)
print(df_m)