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
    print(df_groupby_acq_year)

    for name, group_df in df_groupby_acq_year:
        print(f"Titles acquired in year {name}: {len(group_df)}")


if __name__ == '__main__':
    tate_dataset_df = read_tate_dataset()

    print("Task 1: Total Titles acquired per year")
    titles_per_acq_year(tate_dataset_df)
    print()
