#그룹(분할) 객체 연산하기 (1) 데이터 집계
import pandas as pd
import seaborn as sns
titan = sns.load_dataset('titanic')
df=titan.loc[7:16,['survived','sex','age','fare']]
group_res=df.groupby(['survived', 'sex'])
res=group_res.mean()
print(res)
res2=group_res.mean()['age']
print(res2)