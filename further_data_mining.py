import json
import pandas as panda
import matplotlib.pyplot as plt
import re


tweets_data_path = 'tweet_mining.json'

def read_json(file_path):
    results = []
    tweets_file = open(tweets_data_path, "r")
    for tweet_line in tweets_file:
        try:
            status = json.loads(tweet_line)
            results.append(status)
        except:
            continue
    return results

def is_token_in_tweet_text(token, tweet_text):
    token = token.lower()
    tweet_text = tweet_text.lower()
    match = re.search(token, tweet_text)
    if match:
        return True
    return False

results = read_json(tweets_data_path)

#create a dataframe
statuses = panda.DataFrame()

#store the text values
statuses['text'] = map(lambda status: status['text'], results)
#store the Language values
statuses['lang'] = map(lambda status: status['lang'], results)
#sometimes there may not be a 'place' listed in the tweet, so set to 'None' if not present
statuses['country'] = map(lambda status: status['place']['country'] if status['place'] != None else None, results)

# new DataFrame columns
statuses['Champions League'] = statuses['text'].apply(lambda status: is_token_in_tweet_text('Champions League', status))
statuses['UEFA'] = statuses['text'].apply(lambda status: is_token_in_tweet_text('UEFA', status))
statuses['PSV'] = statuses['text'].apply(lambda status: is_token_in_tweet_text('PSV', status))
statuses['Atletico'] = statuses['text'].apply(lambda status: is_token_in_tweet_text('Atletico', status))

print statuses['Champions League'].value_counts()[True]
print statuses['UEFA'].value_counts()[True]
print statuses['PSV'].value_counts()[True]
print statuses['Atletico'].value_counts()[True]