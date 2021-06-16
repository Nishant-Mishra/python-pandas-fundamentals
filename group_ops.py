"""
    We shall do following tasks using group operations:
    1. Aggregation: Count number of titles acquired each year, OR
                    Find oldest artwork for each artist
    2. Transformation: Replacing unknown 'medium' with the most used 'medium' by that artist
    3. Filtering: Removing rows with unknown 'title' OR
                  Dropping the rows with unique titles (i.e. keeping only duplicated titles)
"""
from typing import Optional

import pandas as pd
from indexing_filtering import read_tate_dataset


def titles_per_acq_year(df: pd.DataFrame):
    df_groupby_acq_year = df.groupby(['acquisitionYear'])
    titles_groupby_acq_year = df_groupby_acq_year['title']

    # Method 1: Using Generics
    records = {}
    for name, group_series in titles_groupby_acq_year:  # type: str, pd.Series[str]
        records[name] = group_series.count()
    s1 = pd.Series(records)

    # Method 2A: Using pandas Builtin 'agg' method
    s2 = titles_groupby_acq_year.agg(pd.Series.count)   # type: pd.Series[int]

    # Method 2B: Using pandas Builtin 'agg' method's alternate
    s3 = df_groupby_acq_year.count().loc[:, 'title']    # type: pd.Series[int]

    assert s1.equals(s2), "Calculating aggregation by iterating over GroupByDataFrame " \
                          "should be equal to using Python '.agg'"
    assert s2.equals(s3), "Calling aggregation func with pandas '.agg' should be equal " \
                          "to calling the aggregation directly on DataFrame object"
    s3.index = s3.index.astype('int')
    print(s3)


def oldest_artwork_per_artist(df: pd.DataFrame):
    acq_year_groupby_artist = df.groupby(['artist'])['acquisitionYear']

    # Method 1: Using Generics
    records = {}
    for name, group_series in acq_year_groupby_artist:  # type: str, pd.Series
        records[name] = group_series.min()
    s1 = pd.Series(records)

    # Method 2A: Using pandas Builtin 'agg' method
    s2 = acq_year_groupby_artist.agg(pd.Series.min)     # type: pd.Series

    # Method 2B: Using pandas Builtin 'agg' method's alternate
    s3 = acq_year_groupby_artist.min()                  # type: pd.Series

    assert s1.equals(s2), "Calculating aggregation by iterating over GroupByDataFrame " \
                          "should be equal to using Python '.agg'"
    assert s2.equals(s3), "Calling aggregation func with pandas '.agg' should be equal " \
                          "to calling the aggregation directly on DataFrame object"
    s3 = s3.astype('int')
    print(s3)


def _find_most_freq_medium(series: pd.Series) -> Optional[str]:
    counts = series.value_counts()      # type: pd.Series
    if counts.min() == counts.max():
        return None
    return counts.idxmax()


def replace_unknown_mediums(df: pd.DataFrame):
    mediums_groupby_artist = df.groupby(['artist'])['medium']

    # Method 1
    for name, group_series in mediums_groupby_artist:   # type: str, pd.Series
        cnt_mediums = len(group_series)
        if cnt_mediums > 0:
            print(group_series)
            medium = _find_most_freq_medium(group_series)
            if medium:
                df.fillna(value={'medium': medium}, inplace=True)




if __name__ == '__main__':
    tate_dataset_df = read_tate_dataset()
    tate_dataset_df_subset = tate_dataset_df.iloc[49900:50100, :]

    # print("Task 1: Total Titles acquired per year:")
    # titles_per_acq_year(tate_dataset_df_subset)
    # print()
    #
    # print("Task 2: Oldest artwork per artist")
    # oldest_artwork_per_artist(tate_dataset_df_subset)
    # print()

    print("Task 3: Unknown mediums replaced with most used by that artist")
    replace_unknown_mediums(tate_dataset_df)
    print()
