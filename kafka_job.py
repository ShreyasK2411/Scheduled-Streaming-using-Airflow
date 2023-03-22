from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

# setting the default arguments
default_args = {
    'owner':'Shreyas',
    'start_date':datetime(2023,3,21,13), # starting from today at 3pm
    'retries':3,
    'retry_delay':timedelta(minutes=5) # if failed retry after every 5 mins
}

dag = DAG(
    dag_id = "Kafka_Streaming_Job",
    default_args = default_args,
    description = "Stream daily stocks data using kafka and put it in database.",
    schedule_interval= '57 13 * * 1-5', # schedule everyday at 3pm
    catchup = True
)

# start the producer
stream = BashOperator(
    task_id = 'Start_the_producer',
    bash_command = 'python3 /home/talentum/kafka-project/producer.py',
    dag = dag
)

stream
