import json 
import requests
import re
import requests
from bs4 import BeautifulSoup 
from threading import Lock

lock = Lock()


def parser(html_doc):
    #with lock:
    failed = []
    soup = BeautifulSoup(html_doc)
    def dealer_name():
        try:
            dealer_name = soup.find('h1' , attrs = {'class' : 'dealerName'})
            return dealer_name
        except Exception as e:
            print(e)
            return 'bad url'
    def dealer_web():
        try:
            dealer_web = soup.find('a' , attrs = { 'target' : "_blank" })
            #print(dealer_web.text)
            if dealer_web:
                return dealer_web.text
            else:
                return 'doees not exist'
        except Exception as e:
            print(e)
            failed.append(f'{dealer_name} web not found')
            return 'doees not exist'
    def dealer_count():
        try:
            dealer_count = soup.find('span' , attrs = { 'class' : 'pageNavShowing' }).findChildren()
            if dealer_count:
                
                for i , child in enumerate(dealer_count):
                    if i == 1:
                        dealer_count_num = child.text
                    else :
                        dealer_count_num = 0
                return dealer_count_num
            else:
                return 0
        except Exception as e:
            print(e)
            failed.append(f'{dealer_name} count not found')
            return 'doees not exist'
    
    
    def dealer_phone():
        try:
            dealer_phone = soup.find('span' , attrs={'class' : "dealerSalesPhone"})
            if dealer_phone:
                return dealer_phone.text
            else:
                return 'does not exist'
        except Exception as e:
            print(e)
            failed.append(f'{dealer_name} phone not found')
            return 'doees not exist'
    def dealer_rate():
        try:
            dealer_rate = soup.find('div' , attrs = {'class' : 'starRating'})
            if dealer_rate:
                return dealer_rate['title']
            else:
                return 0
        except Exception as e:
            print(e)
            failed.append(f'{dealer_name} rate not found')
            return 'doees not exist'
    def dealer_reviews():
        try:
            dealer_reviews =soup.find('div' , attrs = {'class' : 'details'})
            if dealer_reviews:
                dealer_reviews =  dealer_reviews.text.split()[-1]
                if dealer_reviews == 'Reviews':
                    dealer_reviews = 0 
                return dealer_reviews 
            else:
                return 0
        except Exception as e:
            print(e)
            failed.append(f'{dealer_name} reviews not found')
            return 'does not exist'
    
    def dealer_time():

        try:
            dealer_time = soup.find('div' , attrs={'class' : 'dealerText' })
            if dealer_time:
                if dealer_time.text:
                    return ' '.join(dealer_time.text.split())
                elif dealer_time.strong:
                    time = dealer_time.strong.text
                else:
                    time = dealer_time.span.text.split()
                    return  ' '.join(time)
            else:
                return 'does not exist'
        except Exception as e:
            print(e)
            failed.append(f'{dealer_name} dealer_time not found')
            return 'does not exist'
    dealer_name = dealer_name()
   #print(dealer_name.text)
    dealer_web = dealer_web()
    dealer_phone = dealer_phone()
    dealer_time = dealer_time()
    dealer_rate = dealer_rate()
    dealer_reviews = dealer_reviews()
    dealer_count = dealer_count()
    out_put = ( dealer_name.text , dealer_phone , dealer_web , dealer_count, dealer_rate ,
        dealer_reviews , dealer_time)

    return out_put





