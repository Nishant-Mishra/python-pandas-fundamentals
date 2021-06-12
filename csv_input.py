"""
    Demo of reading CSV Data using Pandas
"""
import traceback

import pandas as pd


CSV_DATASET_PATH = "../datasets/the-tate-collection.csv"

# To read data from CSV, we use pd.read_csv(...) function
tate_dataset_abridged_df = pd.read_csv(CSV_DATASET_PATH, sep=';', nrows=5)
print(tate_dataset_abridged_df)
print()

INDEX_COL = 'id'

# Specifying one of the columns in dataset as Index
tate_dataset_abridged_df = pd.read_csv(CSV_DATASET_PATH, sep=';', nrows=5, index_col=INDEX_COL)
print(tate_dataset_abridged_df)
print()

# Specifying subset of column labels to read from CSV File
tate_dataset_abridged_df = pd.read_csv(CSV_DATASET_PATH, sep=';', nrows=5, index_col=INDEX_COL,
                                       usecols=['id', 'artist', 'url'])
print(tate_dataset_abridged_df)
print()

USECOLS = [INDEX_COL, 'artist', 'title', 'medium', 'year', 'acquisitionYear', 'height', 'width', 'units']

tate_dataset_abridged_df = pd.read_csv(CSV_DATASET_PATH, sep=';', nrows=5, index_col=INDEX_COL,
                                       usecols=USECOLS)
print(tate_dataset_abridged_df)
print()

# Cannot skip Index Column from the list of columns to read
try:
    tate_dataset_abridged_df = pd.read_csv(CSV_DATASET_PATH, sep=';', nrows=5, index_col=INDEX_COL,
                                           usecols=USECOLS[1:])
except ValueError as e:
    print(f"ERROR: Cannot skip Index Column from 'usecols' param")
    print("Traceback:")
    traceback.print_tb(e.__traceback__)
else:
    print("Oh well!! It works, You can skip the Index Cloumn label from 'usecols' param")
    print(tate_dataset_abridged_df)

# Save the read dataset to disk file
tate_dataset_full_df = pd.read_csv(CSV_DATASET_PATH, sep=';', index_col=INDEX_COL, usecols=USECOLS)
pd.to_pickle(tate_dataset_full_df, '../datasets/tate_dataset_full_df.gz', compression='infer')

