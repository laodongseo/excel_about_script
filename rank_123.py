import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

import pandas as pd

df = pd.DataFrame([
    ['a', 2008],
    ['a', 2008],
    ['a', 2008],
    ['b', 2008],
    ['b', 2008],
    ['b', 2008],
], columns=['A', 'B'])

df['C'] = df.groupby('A')['B'].rank(method='first').astype(int)
df['D'] = df['B'] + df['C'] - 1
print(df)

s = df['B'].rank(method='first')
print(s)
