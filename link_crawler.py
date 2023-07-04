import requests
from bs4 import BeautifulSoup   
import pandas as pd 
import time 
import random 
import csv





def get(url):

    sess = requests.Session()
    adapter = requests.adapters.HTTPAdapter(max_retries = 20)
    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36",
        }
    
    try:
        html_doc = sess.get( url ,headers = headers ,timeout=10)
        return html_doc
    except Exception as e:
        return e

def page(response):

    try:
        soup = BeautifulSoup(response.text , "html.parser")
        page = soup.select('.info > strong:nth-child(2)')
        name = soup.select('.header5')
        for wraper in name:
            name = wraper.text[29:-4]
        for wraper in page:
            page = wraper.text
        return (name , page)
    except Exception as e:
        return e


def link_crawler(info , url):
    dealer_list = []
    failed = []
    page = info[1]
    page = page.replace(',' , '')
    #print(page)
    page = int(page)//10 + 1
    global name 
    name = info[0]
    name = name.replace(',' , '-')
    name = name.replace(' ' , '').split()[0]
    
    for start in range(page):
            #print(start)
            link = url + str(start)
            #print(link)
            sess = requests.Session()
            #print('ali' , url)
            adapter = requests.adapters.HTTPAdapter(max_retries = 20)
            headers = {
                "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36",
            }
    
            try:
                response = sess.get( link ,headers = headers ,timeout=10)
            except Exception as e:
                return e

            soup = BeautifulSoup(response.text)
            try:
                dealer_name = soup.find_all('div', attrs = {'class':'details'})  
                #print(dealer_name['href'])
                print(link , name)
            except Exception as e:
                print(e)
            try:
                dealer_address_span = soup.find_all('span' , attrs = {'class' : 'dealerDetail'})
                dealer_address = []
                for address in dealer_address_span:
                    if address['class'][0] == 'dealerDetail':
                        dealer_address.append(address.text)
                    else:
                        dealer_address.append('does not exist')
            except Exception as e:
                print(e)

            try:   
                dealer_page = soup.find_all('a' , attrs = {'class' : 'viewInventory'})
                for (i , j , k ) in zip(dealer_page , dealer_address , dealer_name):
                    j = ' '.join(j.split())
                    dealer_list.append([k.strong.text , j , i['href']])
            #print(len(dealer_list))
            except Exception as e:
                print(e)
                #failed.append()
                with open('failed.csv', 'w' , newline='') as f:
                    writer = csv.writer(f)
                    for item in failed:
                        writer.writerow([item])
            df = pd.DataFrame(dealer_list)
            global path
            path = f'primary/{name}.xlsx'
            writer = pd.ExcelWriter( path , engine='xlsxwriter')
            df.to_excel(writer, sheet_name='welcome', index=False)
            writer.close()

def luncher(urls):
    response = get(urls)
    info = page(response)
    link_crawler(info , urls)
    return path , name