
import pandas as pd


def loader(path):
    data = pd.read_excel(path)
    links = data.iloc[: , -1]
    return links

