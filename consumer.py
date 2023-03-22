from kafka import KafkaConsumer,TopicPartition
import json
from sqlite3 import connect
from datetime import date

bootstrap_servers = ['localhost:9092']
TOPIC = 'Daily_Stock_Prices'

consumer = KafkaConsumer(TOPIC,bootstrap_servers=['localhost:9092'])


while True:
	for data in consumer:
		data = json.loads(data.value.decode('utf-8'))
		with connect('/home/talentum/kafka-project/investment.db') as conn:
                    cursor = conn.cursor()
                    query = "insert into daily_stock_prices (date,market,symbol,open,high,low,close) values (?,?,?,?,?,?,?)"
                    values = (date.today(),'NYSE',data['symbol'],float(data['Open']),float(data['High']),float(data['Low']),float(data['Previous Close']))
                    cursor.execute(query,values)
                    print(data)

