# EasyTweet
# Copyright 2022 Ibrahima Khalilou Lahi Samb
# @link : https://www.linkedin.com/in/ibrahima-samb-dev
# @twitter: @Mister__iks

from datetime import datetime
import pandas as pd
import tweepy
from common.easytweet.access_config import ApiConfig


class MyTimeline:
    """
    A class used to get access to twitter timeline.

    Attributes
    ----------
    config : access_config.Config
        A Config type object containing the access information to the twitter api
    pandas : pandas
        pandas library

    Methods
    -------
    tweet_regarding(to: str, count: int)
        Finds all tweets related to or containing the variable terms
    """

    def __init__(self, config: ApiConfig, pandas: pd):
        self.cfg = config
        self.api = tweepy.API(self.cfg.auth())
        self.pd = pd

    def tweet_regarding(self, to: str, count: int):
        """
        This method will allow you to retrieve tweets relating 
        to a specific subject and then save it in a csv file.

        Parameters
        ----------
        to :str 
            Topic on which our research focuses
        count :int
            Number of tweet to save.

        Return
        ------
        `pandas.DataFrame` 
            Returns a dataframe containing the result of the query
        """
        request = self.api.search_tweets(q=to, count=count)
        response_schema = ["user", "followers_count", "device", "location"]
        response_data = []

        for tweet in request:
            if (tweet.user.location != ''):
                response_data.append([tweet.user.screen_name,
                                      tweet.user.followers_count,
                                      tweet.source, tweet.user.location])
            else:
                response_data.append([tweet.user.screen_name,
                                      tweet.user.followers_count,
                                      tweet.source, "None"])
        dataframe = self.pd.DataFrame(
            data=response_data, columns=response_schema)
        dataframe.to_csv(f"./dags/data/output_files/tweet_regarding_to_{to}_{datetime.now().day}_{datetime.now().month}_{datetime.now().year}.csv",
                         header=True, index=None, sep=',', mode='a')
        return dataframe

    def trends(self):
        """
        Allows you to retrieve daily trends from twitter and save them in a csv file
        by retrieving the name of the trend as well as the volume

        Return
        ------
        `pandas.DataFrame` 
            Returns a dataframe containing the result of the query
        """
        request = self.api.get_place_trends(1)
        # creating the schema for trends data
        response_schema = ["name", "volume"]
        response_data = []
        for trend in request[0]['trends']:
            response_data.append([trend['name'], trend['tweet_volume']])
        trends_dataframe = self.pd.DataFrame(
            data=response_data, columns=response_schema)
        trends_dataframe.to_csv(
            f"./dags/data/output_files/trends_{datetime.now().day}_{datetime.now().month}_{datetime.now().year}.csv", header=None, index=None, sep=',', mode='a')
        return trends_dataframe
