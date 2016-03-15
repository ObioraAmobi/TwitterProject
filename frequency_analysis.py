import json
import tweepy
from collections import Counter
from prettytable import PrettyTable
from auth import get_api

api = get_api()

count = 50
query = 'Weather'

results = [status for status in tweepy.Cursor(api.search, q=query).items(count)]

status_texts = [ status._json['text'] for status in results]

screen_names = [ status._json['user']['screen_name']
                 for status in results
                    for mention in status._json['entities']['user_mentions'] ]

hashtags = [ hashtag['text'] for status in results
                for hashtag in
                    status._json['entities']['hashtags']]

words = [ w
            for t in status_texts
                    for w in t.split()]

for entry in [screen_names, hashtags, words]:
    counter = Counter(entry)
    print counter.most_common()[:10] # the top 10 results
    print

for label, data in (('Text', status_texts), ('Screen Name', screen_names), ('Word', words)):
    table = PrettyTable(field_names=[label, 'Count'])
    counter = Counter(data)
    [ table.add_row(entry) for entry in counter.most_common()[:10] ]
    table.align[label], table.align['Count'] = '1', 'r' #align the columns
    print table