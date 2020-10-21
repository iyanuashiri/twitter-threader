# twitter-threader


## Introduction

Twitter Thread is a list of tools to manage threads on Twitter. You can GET and POST threads on Twitter.



## Installation

```bash
pip install twitter-threader
```


## Usage
### Guide


- Get a thread on Twitter


```python
import threader


thread = threader.Thread('consumer_key', 'consumer_secret', 'access_token_key', 'access_token_secret')
thread.convert_to_post('1247616218153902080')
```



## Testing

```bash
pytest
```