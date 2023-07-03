import requests
from bs4 import BeautifulSoup   
import pandas as pd 
import time 
import random 
import csv


def get(start):
    sess = requests.Session()
    adapter = requests.adapters.HTTPAdapter(max_retries = 20)
    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36",
        }
    url = f'https://www.cargurus.com/Cars/dl.action?entityId=&address=Boston%2C+MA&latitude=42.36008&longitude=-71.05888&distance=100&page={start}'
    response = sess.get( url ,headers = headers ,timeout=10)
    time.sleep(random.randint(7,12))
    print(f'page {start} was crawled')
    return response

dealer_list = []
def parser(html_doc):
    failed = []
    try:
        soup = BeautifulSoup(html_doc.text)
        try:
            dealer_name = soup.find_all('div', attrs = {'class':'details'})  
        except Exception as e:
            print(e)
        try:
            dealer_address_span = soup.find_all('span' , attrs = {'class' : 'dealerDetail'})
            dealer_address = []
            for address in dealer_address_span:
                if address['class'][0] == 'dealerDetail':
                    dealer_address.append(address.text)
        except Exception as e:
            print(e)

        try:   
            dealer_page = soup.find_all('a' , attrs = {'class' : 'viewInventory'})
            for (i , j , k ) in zip(dealer_page , dealer_address , dealer_name):
                j = ' '.join(j.split())
                dealer_list.append([k.strong.text , j , i['href']])
            print(len(dealer_list))
            df = pd.DataFrame(dealer_list)
            writer = pd.ExcelWriter('data/Boston.xlsx', engine='xlsxwriter')
            df.to_excel(writer, sheet_name='welcome', index=False)
            writer.close()
        except Exception as e:
            print(e)
            failed.append()
            with open('failed.csv', 'w' , newline='') as f:
                writer = csv.writer(f)
                for item in failed:
                    writer.writerow([item])
    except Exception as e:
        print(e)

for i in range(279):
    print(parser(get(start = i)))
    print(i)