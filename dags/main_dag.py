from datetime import datetime, timedelta
from airflow import DAG
from airflow.decorators import task
from common.easytweet.timeline import MyTimeline
from common.easytweet.access_config import ApiConfig
import pandas as pd_data

CONSUMER_KEY = "your_consumer_key"
CONSUMER_SECRET_KEY = "your_consumer_secret_key"
ACCESS_TOKEN = "your_access_token"
ACCESS_TOKEN_SECRET = "your_access_token_secret"
default_args = {
    'owner': 'Ibrahima',
    'depends_on_past': False,
    'start_date': datetime(2022, 12, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
}


with DAG(dag_id="demo", start_date=datetime(2022, 11, 2), default_args=default_args, schedule="@once") as dag:

    @task
    def get_tweets_regarding_to(topic: str, count):
        """
        Allows you to retrieve daily trends on twitter
        """
        conf = ApiConfig(consumer_key=CONSUMER_KEY, consumer_secret_key=CONSUMER_SECRET_KEY,
                         access_token=ACCESS_TOKEN, access_token_secret=ACCESS_TOKEN_SECRET)
        timeline = MyTimeline(config=conf, pandas=pd_data)
        timeline.tweet_regarding(to=topic, count=count)

    @task
    def get_trends():
        """
        Allows you to retrieve daily trends on twitter
        """
        conf = ApiConfig(consumer_key=CONSUMER_KEY, consumer_secret_key=CONSUMER_SECRET_KEY,
                         access_token=ACCESS_TOKEN, access_token_secret=ACCESS_TOKEN_SECRET)
        timeline = MyTimeline(config=conf, pandas=pd_data)
        timeline.trends()


    get_trends() >> get_tweets_regarding_to(topic="messi", count=90)
