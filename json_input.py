"""
    Demo of reading JSON data using Pandas
"""
import json
import os
from typing import Tuple, Any

import pandas as pd

# The tate Collection's JSON dataset is arranged such that each JSONfile contains details of a single artwork.
# These JSONfiles are arranged in a folder structure defined by there acquisition ID (prefixes).

JSON_DATASET_ROOT_PATH = '../datasets/the-tate-collection-json/artworks'
INDEX_COL = 'id'
KEYS_TO_USE = [INDEX_COL, 'all_artists', 'title', 'acquisitionYear', 'medium', 'dateText', 'height', 'width', 'units']


def read_fields_from_json(file_path) -> Tuple[Any]:
    record = []
    with open(file_path, "r") as fp:
        try:
            data = json.load(fp)
        except json.JSONDecodeError:
            print(f"Invalid JSON file '{file_path}'")
        else:
            # Read the values
            for key in KEYS_TO_USE:
                record.append(data[key])

    return tuple(record)


def read_dataset(json_root_path) -> pd.DataFrame:
    """
    Try to find the JSON files in all the subfolders of the given folder.
    Read the JSON files and add the record to the dataframe.
    Owing to large number of files, only read first JSON file in each folder.

    :param json_root_path: Parent Directory containing the tree for JSON files.
    :return: DataFrame containing the data arranged in pre-defined columns.
    """
    artworks = []
    for _dirname, _dirs, files in os.walk(json_root_path):
        for file in files:  # type: str
            if file.endswith('json'):
                record = read_fields_from_json(os.path.join(_dirname, file))
                artworks.append(record)
            # Read one file per directory and then break
            break

    df = pd.DataFrame.from_records(artworks, index=INDEX_COL, columns=KEYS_TO_USE)

    return df

