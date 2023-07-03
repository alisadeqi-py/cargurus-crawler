import requests
import traceback
from bs4 import BeautifulSoup
import time 
import json
import re
import random
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

adv_links_set = []
def get_page(start):
    try:
        sess = requests.Session()
        adapter = requests.adapters.HTTPAdapter(max_retries = 20)
        sess.mount('http://', adapter)
        headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36",
        }
        link = f'https://www.cargurus.com/Cars/dl.action?entityId=&dealerType=USED&sortType=PROXIMITY_ASC&distance=100&address=Connecticut&latitude=41.603&longitude=-73.088&page={start}'
        #url = link + page
        response = sess.get( link  , verify=False ,headers = headers ,timeout=10) 
        time.sleep(5)
        print(response)
    except Exception:
        traceback.print_exc()
        return None
    return response.text

def find_links(html_doc):
    soup = BeautifulSoup(html_doc)
    res = soup.find_all('a', attrs = {'class':'viewInventory'})
    links = []
    for a in res:
        print(a["href"])
        links.append(a["href"])
    return links
    
adv_link = []
for i in range(28,436):

    links = find_links(get_page(i))
    adv_link.append(links)

    print( 'page:', i)
    time.sleep(random.randint(2,5))

    with open('data/Connecticut.json' , 'w') as f:
        print(len(adv_link))
        for item in adv_link:
            if item not in adv_links_set:
                adv_links_set.append(item)
        print(len(adv_links_set))
        f.write(json.dumps(list(adv_links_set)))



