from pathlib import Path
import pandas as pd
from typing import List


def concat_many_csvs(paths: List[Path]) -> pd.DataFrame:
    """
    Concatenate many csv files into one dataframe.
    :param paths:
    :return:
    """
    data = []
    for path in paths:
        df = pd.read_csv(path, index_col=None, header=0)
        data.append(df)
    return pd.concat(data, axis=0, ignore_index=True)
