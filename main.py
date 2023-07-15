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
#from geopy import geocoders  
import concurrent.futures
#from geopy.geocoders import Nominatim
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
#third_url = urls[126:187]

""" urls = [
    'https://www.cargurus.com/Cars/dl.action?entityId=&address=Ashland%2C+OR+97520&latitude=42.194576&longitude=-122.70948&distance=100&page=',
    'https://www.cargurus.com/Cars/dl.action?entityId=&address=Charleston%2C+SC&latitude=32.776474&longitude=-79.93105&distance=100&page='
]
 """
#first_url = urls[0]
#second_url = urls[1]


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
        response = sess.get( url  , verify=True ,headers = headers ,timeout= 40)
        return response.text
    except Exception:
        traceback.print_exc()
        return None
        





failed = []

lock = Lock()



def runner(urls , thread_name):
    #with lock:
    for url in urls:
        print(url)
        path_thread , name = luncher(url , thread_name)
        print(path_thread, name)
        links = loader(path_thread)
        print('ali')
        return links , name  

def crawler(links , name , thread_name):
        thread_name = []
        for link in links:
            try:
                print(link)
                out_put = parser(get(link))
                thread_name.append(out_put)
                df = pd.DataFrame(thread_name)
                writer = pd.ExcelWriter(f'primary_result/{name}.xlsx', engine='xlsxwriter')
                df.to_excel(writer , index=False)
                writer.close()
                print((len(thread_name)/len(links))*100,'%' , thread_name )
            except Exception as e:
                print(e)
                time.sleep(3)


def main(thread_name , urls):
    print(thread_name)
    links , name = runner(urls , thread_name)
    crawler(links, name , thread_name)




class showThread(threading.Thread):
    def __init__(self , thread_name , urls):
        super().__init__()
        self.thread_name = thread_name
        self.urls = urls
    
    def run(self):
        main(self.thread_name, self.urls)

t1 = showThread(thread_name = 'one' ,  urls = first_url)
t2 = showThread(thread_name = 'two',  urls = second_url)


t1.start()
t2.start()

t1.join()
t2.join()