import json
import pandas as panda
import matplotlib.pyplot as plt

tweets_data_path = 'tweet_mining.json'

results = []

tweets_file = open(tweets_data_path, "r")
for tweet_line in tweets_file:
    try:
        status = json.loads(tweet_line)
        results.append(status)
    except:
        continue

print len(results)

# creating a dataframe
statuses = panda.DataFrame()

# store the text values
statuses['text'] = map(lambda status: status['text'], results)

# store the language values
statuses['lang'] = map(lambda status: status['lang'], results)

# sometimes there may not be a 'place' liste in the tweet, so set to 'None if not present
statuses['country'] = map(lambda status: status['place']['country'] if status['place'] != None else None, results)

# get each tweet language and the count of its appearance (not to be confused with programming languages
tweets_by_lang = statuses['lang'].value_counts()