#그룹(분할) 객체 연산하기 (2) agg 함수
import pandas as pd 
import seaborn as sns
def mean_min(x):
    return x.mean()-x.min()
titan = sns.load_dataset("titanic")
df=titan.loc[7:16,['survived', 'sex', 'age','fare']]
group_res=df.groupby(['survived','sex'])
mean_min_res=group_res.agg(mean_min)
print(mean_min_res)
mean_min_res2=group_res.agg('mean','min')
print(mean_min_res2)
mean_min_res3=group_res.agg({'age':'mean','fare':['mean','min']})
print(mean_min_res3)