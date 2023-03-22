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
## Turn on the dag
## Successful execution
![alt](https://github.com/ShreyasK2411/Scheduled-Streaming-using-Airflow/blob/aa7a808c75d1d7937505e2349ed311a333880c09/images/Screenshot%20(74).png?raw=True)
![alt](https://github.com/ShreyasK2411/Scheduled-Streaming-using-Airflow/blob/9e472e5956f76387ecbed3de3a667bcd48eb8a83/images/success.PNG?raw=True)
