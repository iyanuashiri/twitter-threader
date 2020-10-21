import tweepy


class Thread:
    def __init__(self, consumer_key, consumer_secret, access_token_key, access_token_secret):
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token_key, access_token_secret)

        self.api = tweepy.API(auth)

    def get_thread(self, status_id, thread=None):
        status = self.api.get_status(status_id, tweet_mode='extended') if status_id is None else self.api.get_status(status_id, tweet_mode='extended')
        thread = [] if thread is None else thread
        status_id = status.in_reply_to_status_id
        tweet = str(status.full_text)
        thread.append(tweet)
        if status_id is None:
            return thread
        else:
            return self.get_thread(status_id, thread)

    def convert_to_post(self, status_id):
        thread = self.get_thread(status_id)
        thread = reversed(thread)
        post = " ".join(thread)
        return post
