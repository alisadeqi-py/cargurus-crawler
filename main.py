from loader import loader
from link_crawler import luncher
from  crawler import parser
import requests
import time 
import traceback
import json
from bs4 import BeautifulSoup 
import pandas as pd  
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

 
 
urls =[
      #'https://www.cargurus.com/Cars/dl.action?entityId=&address=Omaha%2C+NE&latitude=41.25654&longitude=-95.9345&distance=100&page=',
      'https://www.cargurus.com/Cars/dl.action?entityId=&address=Carson+City%2C+NV&latitude=39.1638&longitude=-119.7674&distance=100&page=' , 
      'https://www.cargurus.com/Cars/dl.action?entityId=&address=Las+Vegas%2C+NV&latitude=36.171562&longitude=-115.1391&distance=100&page=' ,
      'https://www.cargurus.com/Cars/dl.action?entityId=&address=Concord%2C+NH&latitude=43.208138&longitude=-71.537575&distance=1000&page=' ,
      'https://www.cargurus.com/Cars/dl.action?entityId=&address=Trenton%2C+NJ&latitude=40.22058&longitude=-74.75972&distance=100&page=' , 
      'https://www.cargurus.com/Cars/dl.action?entityId=&address=Newark%2C+NJ&latitude=40.735657&longitude=-74.17236&distance=100&page=',
      'https://www.cargurus.com/Cars/dl.action?entityId=&address=Santa+Fe%2C+NM&latitude=35.686974&longitude=-105.9378&distance=100',
      'https://www.cargurus.com/Cars/dl.action?entityId=&address=Albuquerque%2C+NM&latitude=35.084385&longitude=-106.65042&distance=100',
      'https://www.cargurus.com/Cars/dl.action?entityId=&address=Albany%2C+NY&latitude=42.65258&longitude=-73.75623&distance=100',
      'https://www.cargurus.com/Cars/dl.action?entityId=&address=New+York%2C+NY&latitude=40.712776&longitude=-74.005974&distance=100',
      'https://www.cargurus.com/Cars/dl.action?entityId=&address=Raleigh%2C+NC&latitude=35.77959&longitude=-78.638176&distance=100',
      'https://www.cargurus.com/Cars/dl.action?entityId=&address=Charlotte%2C+NC&latitude=35.227085&longitude=-80.843124&distance=100',
      'https://www.cargurus.com/Cars/dl.action?entityId=&address=Columbus%2C+OH&latitude=39.961174&longitude=-82.998795&distance=100',
      'https://www.cargurus.com/Cars/dl.action?entityId=&address=Oklahoma+City%2C+OK&latitude=35.46756&longitude=-97.516426&distance=100',
      'https://www.cargurus.com/Cars/dl.action?entityId=&address=Portland%2C+OR&latitude=45.515232&longitude=-122.67838&distance=100',
      'https://www.cargurus.com/Cars/dl.action?entityId=&address=Harrisburg%2C+PA&latitude=40.27319&longitude=-76.8867&distance=100',
      'https://www.cargurus.com/Cars/dl.action?entityId=&address=Philadelphia%2C+PA&latitude=39.952583&longitude=-75.16522&distance=100',
      'https://www.cargurus.com/Cars/dl.action?entityId=&address=Providence%2C+RI&latitude=41.82399&longitude=-71.412834&distance=100',
      'https://www.cargurus.com/Cars/dl.action?entityId=&address=Charleston%2C+SC&latitude=32.776474&longitude=-79.93105&distance=100',
      'https://www.cargurus.com/Cars/dl.action?entityId=&address=Sioux+Falls%2C+SD&latitude=43.54602&longitude=-96.73126&distance=100',
      'https://www.cargurus.com/Cars/dl.action?entityId=&address=Nashville%2C+TN&latitude=36.162663&longitude=-86.7816&distance=100',
      'https://www.cargurus.com/Cars/dl.action?entityId=&address=Austin%2C+TX&latitude=30.267153&longitude=-97.74306&distance=100',
      'https://www.cargurus.com/Cars/dl.action?entityId=&address=Houston%2C+TX&latitude=29.760427&longitude=-95.369804&distance=100',
      'https://www.cargurus.com/Cars/dl.action?entityId=&address=Salt+Lake+City%2C+UT&latitude=40.76078&longitude=-111.891045&distance=100',
      'https://www.cargurus.com/Cars/dl.action?entityId=&address=Montpelier%2C+VT+05602&latitude=44.26006&longitude=-72.575386&distance=100',
      'https://www.cargurus.com/Cars/dl.action?entityId=&address=Virginia+Beach%2C+VA&latitude=36.851643&longitude=-75.97922&distance=100',
      'https://www.cargurus.com/Cars/dl.action?entityId=&address=Olympia%2C+WA&latitude=47.037872&longitude=-122.900696&distance=100',
      'https://www.cargurus.com/Cars/dl.action?entityId=&address=Seattle%2C+WA&latitude=47.60621&longitude=-122.33207&distance=100',
      'https://www.cargurus.com/Cars/dl.action?entityId=&address=Charleston%2C+SC&latitude=32.776474&longitude=-79.93105&distance=100',
      'https://www.cargurus.com/Cars/dl.action?entityId=&address=Madison%2C+WI&latitude=43.072166&longitude=-89.40075&distance=100'
      'https://www.cargurus.com/Cars/dl.action?entityId=&address=Milwaukee%2C+WI&latitude=43.038902&longitude=-87.90647&distance=100',
      'https://www.cargurus.com/Cars/dl.action?entityId=&address=Cheyenne%2C+WY&latitude=41.13998&longitude=-104.820244&distance=100',
    ]


dealer_list = []

for url in urls:
    #print(url)
    path , name = luncher(url)
    links = loader(path)
    print(path)
    time.sleep(1)
    print(len(links))
    for link in links:
        print(link)
        out_put = parser(get(link))
        dealer_list.append(out_put)
        df = pd.DataFrame(dealer_list)
        writer = pd.ExcelWriter(f'primary_result/{name}.xlsx', engine='xlsxwriter')
        df.to_excel(writer, sheet_name='welcome', index=False)
        writer.close()
        time.sleep(random.randint(2,3))
        print((len(dealer_list)/len(links))*100,'%' )
    dealer_list = []

    