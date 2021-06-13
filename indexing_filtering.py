"""
    Using the previous dataset, we will try to answer following questions:
    1. Number of distinct artists
    2. How many artworks by 'Robert Blake'
    3. Artwork with biggest area
    ----
    4. Oldest Acquired Artwork
    5. Total number of artworks created using Acrylic or Oil paints.
    6. Total artworks acquired on any given year
    7. Number of Artworks with unknown titles

    While doing this, we will learn indexing and filtering tools available in Pandas
"""
import pandas as pd


def read_tate_dataset() -> pd.DataFrame:
    dataset_path = '../datasets/tate_dataset_full_df.gz'

    dataset = pd.read_pickle(dataset_path, compression='infer')

    return dataset


def task1(df: pd.DataFrame):
    print("Task 1: Read distinct artists count")
    distinct_artists = pd.unique(df.loc[:, 'artist'])
    count_distinct_artists = len(distinct_artists)
    print(f"Value: {count_distinct_artists}")


def task2(df: pd.DataFrame):
    print("Task 2: Number of artworks by 'Robert Blake'")
    artworks_per_artist = df['artist'].value_counts()
    artworks_by_robert = artworks_per_artist['Blake, Robert']
    print(f"Value: {artworks_by_robert}")


def task3(df: pd.DataFrame):
    print("Task 3: Artwork with largest area")
    widths = df.loc[:, 'width']
    heights = df.loc[:, 'height']

    # Convert the values in 'width' or 'height' column to float and convert non-numeric values to Nan
    widths = pd.to_numeric(widths, errors='coerce')     # type: pd.Series
    heights = pd.to_numeric(heights, errors='coerce')   # type: pd.Series

    # Calculate
    area = widths * heights
    df = df.assign(area=area)

    max_area = df.loc[:, 'area'].max()
    idx_max_area = df.loc[:, 'area'].idxmax()

    print(f"Area: {max_area}\nArtwork:\n{df.loc[idx_max_area, :]}")


def task4(df: pd.DataFrame):
    print("Task 4: Oldest Acquired Artwork")
    acquired_year = df.loc[:, 'acquisitionYear']   # type: pd.DataFrame

    acquired_year = pd.to_numeric(acquired_year, errors='coerce')

    oldest_year = acquired_year.min()
    oldest = df.loc[acquired_year.idxmin(), :]
    print(f"Year: {int(oldest_year)}\nArtwork:\n{oldest}")


def task5(df: pd.DataFrame):
    print("Task 5: Total number of artworks created using Oil or Acrylic Paints")
    mediums = df.loc[:, 'medium']    # type: pd.Series

    # pd.Series.str provides access to all String operations on each member of Series.
    oil_paint_artworks = mediums.str.lower().str.startswith('oil')
    acrylic_paint_artworks = mediums.str.lower().str.startswith('acrylic')

    # The biwise OR does elemnt-wise OR or each element in Series
    row_filter = oil_paint_artworks | acrylic_paint_artworks

    # Filter all oil and acrylic artworks
    oil_or_acrylic_artworks = df.loc[row_filter, :]     # type: pd.DataFrame
    cnt_oil_or_acrylic_artworks = len(oil_or_acrylic_artworks)
    print(f"Value: {cnt_oil_or_acrylic_artworks}")


def task6(df: pd.DataFrame, year):
    print(f"Task 6: Total artworks acquired in the year {year}")
    acquisitionYear = df.loc[:, 'acquisitionYear']      # type: pd.Series
    acquisitionYear = pd.to_numeric(acquisitionYear, errors='coerce')
    row_filter = (acquisitionYear == year)
    artworks_for_given_year = df.loc[row_filter, :]
    cnt_artworks = len(artworks_for_given_year)

    print(f"Value: {cnt_artworks}")


def task7(df: pd.DataFrame):
    print("Task 7: Number of artworks with unknown titles")
    titles = df.loc[:, 'title']     # type: pd.Series
    title_counts = titles.value_counts()    # type: pd.Series
    title_counts.sort_values(inplace=True)
    probable_unknown_titles = title_counts.tail(10)

    # As observed manually from the value of probable_unknown_titles, bottom 5 are the unknown ones
    unknown_titles = probable_unknown_titles.tail(5)
    cnt_unknown_titles = unknown_titles.sum()
    print(f"Value: {cnt_unknown_titles}")


if __name__ == '__main__':
    tate_dataset_df = read_tate_dataset()

    task1(tate_dataset_df)
    print()
    task2(tate_dataset_df)
    print()
    task3(tate_dataset_df)
    print()
    task4(tate_dataset_df)
    print()
    task5(tate_dataset_df)
    print()
    year = input("Enter Acquisition Year for which total artworks are needed: ")
    task6(tate_dataset_df, int(year))
    print()
    task7(tate_dataset_df)
    print()

