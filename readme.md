# Scheduled Streaming using Apache Airflow
* Pre-requisite: all the kafka and airflow services and servers should be running
## Create a kafka topic
```bash
kafka-tpics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic Daily_Stock_Prices
```
## Run the kafka consumer as a daemon service
```bash
cp kafka-consumer.service /etc/systemd/system/
```
```bash
sudo systemctl enable kafka-consumer
```
```bash
systemctl daemon-reload
```
```bash
sudo systemctl start kafka-consumer 
```
## Run the kafka producer
```bash
python3 producer.py
```
