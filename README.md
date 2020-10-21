# twitter-threader


## Introduction

Twitter Thread is a list of tools to manage threads on Twitter. 



## Installation

```bash
pip install twitter-threader
```


## Usage
### Guide


1. Get a thread on Twitter


```python
import Thread


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)
api = tweepy.API(auth)


thread = Thread('')
thread.convert_to_post()
```

2. Post a thread on Twitter


## Testing

```bash
pytest
```