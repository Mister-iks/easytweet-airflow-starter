from tweepy import Stream
from datetime import datetime
import os
import pandas as pd


class Listener(Stream):
    def __init__(self, consumer_key: str, consumer_secret: str, access_token: str, access_token_secret: str, folder_name: str):
        Stream.__init__(self, consumer_key=consumer_key, consumer_secret=consumer_secret,
                        access_token=access_token, access_token_secret=access_token_secret)
        self.destination = folder_name

    def on_status(self, status):
        try:
            os.mkdir(f".dags/data/output_files/streaming/{self.destination}")
        except:
            pass
        frame = pd.DataFrame(data=[[status.user.screen_name, status.text]], columns=['name', 'content'])
        frame.to_csv(f"./dags/data/output_files/streaming/{self.destination}/{datetime.now().day}_{datetime.now().month}_{datetime.now().year}_{datetime.now().hour}_{datetime.now().minute}_{datetime.now().second}_{datetime.now().microsecond}")


