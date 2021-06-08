
import pandas as pd
import numpy as np

print()
np_array = np.random.rand(3)
print(f"{np_array}")
print()

np_2darray = np.random.rand(3, 2)
print(f"{np_2darray}")
print()

pd_series = pd.Series(np_array)
print(f"{pd_series}")
print(f"{pd_series[1] = }")
print()

pd_series = pd.Series(np_array, index=['F', 'S', 'T'])
print(f"{pd_series}")
print(f"{pd_series['S'] = }")
print(f"{pd_series[2] = }")
print()

pd_df = pd.DataFrame(np_2darray)
print(f"{pd_df}")
print(f"{pd_df.index = }")
print(f"{pd_df.columns = }")
print(f"{pd_df.shape = }")
print(f"{pd_df[0][0] = }")
print(f"pd_df[0] =\n{pd_df[0]}")
print(f"{type(pd_df[0]) = }")
print()

pd_df = pd.DataFrame(np_2darray, index=['1st', '2nd', '3rd'])
print(f"{pd_df}")
print(f"{pd_df.index = }")
print(f"{pd_df[0]['1st'] = }")
print()

pd_df = pd.DataFrame(np_2darray, index=['1st', '2nd', '3rd'], columns=['I', 'II'])
print(f"{pd_df}")
print(f"{pd_df.columns = }")
print(f"{pd_df.index = }")
print(f"pd_df['II'] =\n{pd_df['II']}")
print(f"{type(pd_df['II']) = }")
print(f"{pd_df['I']['1st'] = }")
print()

try:
    print(f"{pd_df[0]['1st'] = }")
except KeyError:
    print(f"pd_df[0]['1st'] : This doesn't work in DataFrames... as the column labels have been changed")
print()

pd_df.index = ['A', 'B', 'C']
print("Changing index of 'pd_df' after creating it...")
print(f"{pd_df}")
print(f"{pd_df.index = }")
print()
