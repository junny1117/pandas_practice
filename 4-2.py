import pandas as pd

df = pd.DataFrame({'x':[1,2,None,3],
                   'y':[4,3,8,4]})

df_m = df.mean(skipna=False)

print(df_m)