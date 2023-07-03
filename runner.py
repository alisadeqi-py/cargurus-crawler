import requests
import time 
import traceback
import json
from bs4 import BeautifulSoup 
import pandas as pd  
from loader import loader
from parse import parser
import random
def get(link):
    try:
        sess = requests.Session()
        adapter = requests.adapters.HTTPAdapter(max_retries = 15)
        sess.mount('http://', adapter)
        headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36",
        }
        url = 'https://www.cargurus.com/'
        url += link
        #print(url)
        response = sess.get( url  , verify=True ,headers = headers ,timeout= 15)
        #time.sleep(random.randint(3,10))
       #doc_text = response.text
        #with open ('doc.txt' , 'w' , encoding="utf-8") as f:
        #    f.write(response.text)
        #print(response.text)
        #print(response)
    except Exception:
        traceback.print_exc()
        return None
    return response.text
#pageNavShowing
dealer_list = []
page = 0
links = loader()[:]
for link in links:
    print(link)
    out_put = parser(get(link))
    #print(out_put)
    dealer_list.append(out_put)
    df = pd.DataFrame(dealer_list)
    writer = pd.ExcelWriter('Boston.xlsx', engine='xlsxwriter')
    df.to_excel(writer, sheet_name='welcome', index=False)
    writer.close()
    print( f'page {page} was crawled')
    page += 1
