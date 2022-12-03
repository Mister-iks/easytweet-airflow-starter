# EasyTweet
# Copyright 2022 Ibrahima Khalilou Lahi Samb
# @link : https://www.linkedin.com/in/ibrahima-samb-dev
# @twitter: @Mister__iks

class ApiConfig:
    """Config API v1.1
    This class will be used to configure the connection to the twitter API

    Parameters
    ----------
    consumer_key,
    consumer_secret_key,
    access_token,
    access_token_secret
    """

    def __init__(self, consumer_key: str, consumer_secret_key: str, access_token: str, access_token_secret: str):
        self.ck = consumer_key
        self.csk = consumer_secret_key
        self.at = access_token
        self.ats = access_token_secret

    def getCK(self):
        return self.ck

    def getCSK(self):
        return self.csk

    def getAT(self):
        return self.at

    def getATS(self):
        return self.ats

    def auth(self):
        """
        This method will be used to authenticate the user on Twitter

        Return `tweepy.OAuthHandler`
        -------
        """
        import tweepy
        try:
            auth = tweepy.OAuthHandler(self.getCK(), self.getCSK())
            auth.set_access_token(self.getAT(), self.getATS())
            return auth
        except tweepy.Unauthorized:
            logging.error("Y")
        except tweepy.HTTPException:
            print("Sorry the http request failed")
        except:
            print("Error")
