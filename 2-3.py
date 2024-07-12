#DataFrame 생성(numpy 활용)

import pandas as pd
import numpy as np
arr = np.array([80,90,75])
df = pd.DataFrame(arr)
print(df)