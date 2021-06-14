"""
    We shall do following tasks using group operations:
    1. Aggregation: Count number of titles acquired each year, OR
                    Find oldest artwork for each artist
    2. Transformation: Replacing unknown 'medium' with the most used 'medium' by that artist
    3. Filtering: Removing rows with unknown 'title' OR
                  Dropping the rows with unique titles (i.e. keeping only duplicated titles)
"""
import pandas as pd
from indexing_filtering import read_tate_dataset


def titles_per_acq_year(df: pd.DataFrame):
    df_groupby_acq_year = df.groupby(['acquisitionYear'])

    # Method 1: Using Generics
    for name, group_df in df_groupby_acq_year:
        print(f"Titles acquired in year {int(name)}: {len(group_df)}")

    print()
    # Method 2A: Using pandas Builtin 'agg' method
    df = df_groupby_acq_year.agg('count').loc[:, 'title']
    print(df)

    print()
    # Method 2B: Using pandas Builtin 'agg' method's alternate
    df = df_groupby_acq_year.count().loc[:, 'title']
    print(df)


def oldest_artwork_per_artist(df: pd.DataFrame):
    df_groupby_artist = df.groupby(['artist'])

    for name, group_df in df_groupby_artist:
        print(f"The first artwork from {name} was acquired in {int(group_df.loc[:, 'acquisitionYear'].min())}")


if __name__ == '__main__':
    tate_dataset_df = read_tate_dataset()
    tate_dataset_df_subset = tate_dataset_df.iloc[30000:32000, :]

    print("Task 1: Total Titles acquired per year")
    titles_per_acq_year(tate_dataset_df_subset)
    print()

    print("Task 2: Total Titles acquired per year")
    oldest_artwork_per_artist(tate_dataset_df_subset)
    print()
