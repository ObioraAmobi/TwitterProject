import json
import tweepy
from collections import Counter
from prettytable import PrettyTable
from operator import itemgetter
from auth import get_api

api = get_api()

count = 150
query = 'Ireland'

results = [status for status in tweepy.Cursor(api.search, q=query).items(count)]

min_retweets = 10 # the min amount of times a status is retweeted to gain entry to our list.


pop_tweets = [ status for status in results
                    if status._json['retweet_count'] > min_retweets ]

# dictionary of tweet text and associated re tweets
tweets_tup = tuple([(tweet._json['text'].encode('utf-8'),
tweet._json['retweet_count']) for tweet in pop_tweets])

# put in set to remove duplicates
pop_tweets_set = set(tweets_tup)

# sort the tuple entries in descending order
sorted_tweets_tup = sorted(pop_tweets_set, key=itemgetter(1), reverse=True)[:5]

#prettify
table = PrettyTable(field_names=['Text', 'Retweet Count'])
for key, val in sorted_tweets_tup:
    table.add_row([key, val])
    table.max_width['Text'] = 50
    table.align['Text'], table.align['Retweet Count'] = '1', 'r' # align columns

print table