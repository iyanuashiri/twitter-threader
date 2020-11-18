import textwrap
import tweepy


class Thread:
    def __init__(self, api):
        self.api = api

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

    def _check_username(self, user):
        user = self.api.get_user(user)
        screen_name = user.screen_name
        return screen_name

    def _convert_username(self, username):
        mention = f'@{self._check_username(username)} '
        return mention

    def post_thread(self, sentences, username, in_reply_to_status_id=None, thread=None):
        mention = self._convert_username(username)
        mention_length = len(mention)
        left = 280 - mention_length

        thread = [] if thread is None else thread
        print(thread)
        tweets = textwrap.wrap(sentences, width=left)
        for tweet in tweets:
            sentences = sentences[len(tweet):]
            tweet = self.api.update_status(mention + f'{tweet}', in_reply_to_status_id)
            thread.append(tweet.id)
            if sentences is None:
                return thread
            else:
                in_reply_to_status_id = int(tweet.id)
                return self.post_thread(sentences, mention, in_reply_to_status_id, thread)


