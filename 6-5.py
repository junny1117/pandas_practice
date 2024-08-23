#Series와 DataFrame 간 연산하기

import pandas as pd
obj1=pd.Series([1,2,3,4], index=['a','b','c','d'])
obj2=pd.DataFrame([[1,2],[3,4]], columns=['a','b'])
res=obj1.add(obj2)
print(res)