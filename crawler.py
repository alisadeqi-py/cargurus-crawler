from config import BASE_LINK
from abc import ABC , abstractclassmethod
import requests
from bs4 import BeautifulSoup
import json




class CrawlerBase(ABC):

    @abstractclassmethod
    def start(self):
        pass
    
    @abstractclassmethod
    def start(self , data):
        pass
    
    @staticmethod
    def get(link):
        try:
            response = requests.get(link)
        except:
            return None 
        return response


class LinkCrawler(CrawlerBase):

    def __init__(self , cities , link=BASE_LINK):
        self.cities = cities
        self.link = link


    def get_page(self , link):
        try:
            response = requests.get(link) 
            print(response)
        except:
            return None
        return response

    def find_links(self , html_doc):
        soup = BeautifulSoup(html_doc)
        res = soup.find_all( 'a' , attrs = {'class' : 'lmXF4B c7jzqC A1f6zD'} )
        print(res)
        return res

    def start(self , link):
        start =  0 
        crawl = True 
        adv_link = []
        response = self.get_page(link)
        new_links = self.find_links(response.text)
        adv_link.extend(new_links)
        return adv_link

    
    def start_crawl(self):
        adv_links = []
        for city in self.cities:
            links = self.start(self.link.format(city))
            print( city , 
            len(links))
            adv_links.extend(links)
        self.store([li.get('href') for li in adv_links])
    def store(self , data):
        with open('data/data.json' , 'w') as f:
            f.write(json.dumps(data))