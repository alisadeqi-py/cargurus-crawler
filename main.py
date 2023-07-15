from loader import loader
from link_crawler import luncher
from  crawler import parser
import requests
import time 
from threading import Lock
import traceback
import json
from bs4 import BeautifulSoup 
import pandas as pd  
import random
from geopy import geocoders  
import concurrent.futures
from geopy.geocoders import Nominatim
from concurrent import futures
import threading

data = pd.read_excel('urls.xlsx')
urls = data.iloc[: , 0]

# geolocator = Nominatim(user_agent='myapplication')

""" for city in cities:
    city = city.replace(' ', '-')
    location = geolocator.geocode(city)
    lat = location.latitude
    long = location.longitude
    urls.append(f'https://www.cargurus.com/Cars/dl.action?entityId=&address={city}&latitude={lat}&longitude={long}&distance=100&page=')
    print(urls)
print(len(urls))

df = pd.DataFrame(urls)
writer = pd.ExcelWriter('urls.xlsx', engine='xlsxwriter')
df.to_excel(writer , index=False)
writer.close()
 """
# print((len(urls)//8))
first_url = urls[0:63]
second_url = urls[64:125]
third_url = urls[126:187]


def get(link):
    try:
        sess = requests.Session()
        adapter = requests.adapters.HTTPAdapter(max_retries = 40)
        sess.mount('http://', adapter)
        headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36",
        }
        url = 'https://www.cargurus.com/'
        url += link
        #print(url)
        response = sess.get( url  , verify=True ,headers = headers ,timeout= 40)
        #time.sleep(random.randint(3,10))
    #doc_text = response.text
        #with open ('doc.txt' , 'w' , encoding="utf-8") as f:
        #    f.write(response.text)
        #print(response.text)
        #print(response)
        return response.text
    except Exception:
        traceback.print_exc()
        return None
        




dealer_list = []
failed = []

lock = Lock()

def runner(urls):
    for url in urls:
        print(url)
        path , name = luncher(url)
        print(path)
        if path != 0 :
            links = loader(path)
            print(len(links))
            for link in links:
                try:
                    print(link)
                    out_put = parser(get(link))
                    lock.acquire()
                    dealer_list.append(out_put)
                    df = pd.DataFrame(dealer_list)
                    writer = pd.ExcelWriter(f'primary_result/{name}.xlsx', engine='xlsxwriter')
                    df.to_excel(writer , index=False)
                    writer.close()
                    lock.release()
                    print((len(dealer_list)/len(links))*100,'%' )
                except Exception as e:
                    print(e)
                    time.sleep(18)
                    with open('failes.txt' , 'w') as f:
                        f.write(url)
                    
            dealer_list = []
        else:
            print('unvalid url')
print(runner(first_url))



 
""" t1 = threading.Thread(target = runner, args=(first_url,))
t2 = threading.Thread(target = runner, args = (second_url,))


t1.start()
t2.start()

t1.join()
t2.join() """
