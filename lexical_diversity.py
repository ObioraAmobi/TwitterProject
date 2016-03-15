import json
import tweepy
from auth import get_api

api = get_api()

DUB_WOE_ID = 560743
LON_WOE_ID = 44418

dub_trends = api.trends_place(DUB_WOE_ID)
lon_trends = api.trends_place(LON_WOE_ID)

dub_trends_set = set([trend['name']
                      for trend in dub_trends[0]['trends']])

lon_trends_set = set([trend['name']
                      for trend in lon_trends[0]['trends']])

count = 50
query = 'Weather'

# results = [status for status in tweepy.Cursor(api.search, q=query).items(count)]
#
# status_texts = [ status._json['text'] for status in results]
#
# screen_names = [ status._json['user']['screen_name']
#                  for status in results
#                     for mention in status._json['entities']['user_mentions'] ]
#
# hashtags = [ hashtag['text'] for status in results
#                 for hashtag in
#                     status._json['entities']['hashtags']]
#
# words = [ w
#             for t in status_texts
#                     for w in t.split()]
#
# for entry in [screen_names, hashtags, words]:
#     counter = Counter(entry)
#     print counter.most_common()[:10] # the top 10 results
#     print
#
# for label, data in (('Text', status_texts), ('Screen Name', screen_names), ('Word', words)):
#     table = PrettyTable(field_names=[label, 'Count'])
#     counter = Counter(data)
#     [ table.add_row(entry) for entry in counter.most_common()[:10] ]
#     table.align[label], table.align['Count'] = '1', 'r' #align the columns
#     print table

def get_lexical_diversity(items):
    return 1.0*len(set(items))/len(items)

def get_average_words(tweets):
    total_words = sum([len(tweet.split()) for tweet in tweets])
    return 1.0*total_words/len(tweets)

print "Average words: %s" % get_average_words(dub_trends_set)
print "Word Diversity: %s" % get_lexical_diversity(dub_trends_set)
print "Screen Name Diversity: %s" % get_lexical_diversity(dub_trends_set)
print "Hashtag Diversity: %s" % get_lexical_diversity(dub_trends_set)