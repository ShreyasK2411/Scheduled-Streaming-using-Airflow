import requests
from bs4 import BeautifulSoup
import re
from kafka import KafkaProducer
import json
import time

stocks = {'Apple':{'symbol':'AAPL','url':'https://www.moneycontrol.com/us-markets/stockpricequote/apple/AAPL'},
          'Meta':{'symbol':'FB','url':'https://www.moneycontrol.com/us-markets/stockpricequote/meta/FB'},
          'Alphabet':{'symbol':'GOOG','url':'https://www.moneycontrol.com/us-markets/stockpricequote/alphabet/GOOG'},
          'Amazon':{'symbol':'AMZN','url':'https://www.moneycontrol.com/us-markets/stockpricequote/amazon/AMZN'},
          'Netflix':{'symbol':'NFLX','url':'https://www.moneycontrol.com/us-markets/stockpricequote/netflix/NFLX'},
          }

prices = {}
bootstrap_servers = ['127.0.0.1:9092']
TOPIC = 'Daily_Stock_Prices'
producer = KafkaProducer(bootstrap_servers = bootstrap_servers)

for stock in stocks.keys():
    page = requests.get(stocks[stock]['url'])
    soup = BeautifulSoup(page.content, 'html.parser')

    divs = soup.find_all('div', {'class' : 'overview_overview_tbl_sec__Bmlto'})[0]
    tds = divs.find_all('td')
    prices = {}
    prices.update({'symbol':stocks[stock]['symbol']})

    for i in range(0,10,2): 
        prices.update({tds[i].contents[0]:tds[i+1].contents[0]})

    del prices['Beta']
    print(prices)
    producer.send(TOPIC,json.dumps(prices).encode('utf-8'))
    producer.flush()
    time.sleep(5)
