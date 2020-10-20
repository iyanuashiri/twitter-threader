import os

import tweepy
from dotenv import load_dotenv
load_dotenv()


consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")
access_token_key = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)

api = tweepy.API(auth)


class Thread:
    def __init__(self, status_id):
        self.status_id = status_id

    def get_thread(self, status_id=None, thread=None):
        status = api.get_status(self.status_id, tweet_mode='extended') if status_id is None else api.get_status(status_id, tweet_mode='extended')
        thread = [] if thread is None else thread
        status_id = status.in_reply_to_status_id
        tweet = str(status.full_text)
        thread.append(tweet)
        if status_id is None:
            return thread
        else:
            return self.get_thread(status_id, thread)

    def convert_to_post(self):
        thread = self.get_thread()
        thread = reversed(thread)
        post = " ".join(thread)
        return post
