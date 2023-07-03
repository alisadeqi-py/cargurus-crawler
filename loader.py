import pandas as pd 
def loader():
    data = pd.read_excel('data/Boston.xlsx')

    links = data.iloc[: , -1]
    return links

""" links = loader()
base = 'https://www.cargurus.com/'
for i in links:
    url = base + i 
    print(url) """
