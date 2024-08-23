#DataFrame과 숫자 간 연산하기

import pandas as pd
import seaborn as sns
titan=sns.load_dataset('titanic')
df=titan.loc[10:16,['age']]
res=df.div(2)
print(res)