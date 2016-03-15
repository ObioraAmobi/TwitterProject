import json
import tweepy
from auth import get_api

api = get_api()

count = 3
query = 'Dublin'

results = [status for status in tweepy.Cursor(api.search, q=query).items(count)]


print json.dumps(results[0]._json, indent=4)
# status_texts = [ status._json['text'] for status in results]

# print status_texts

# screen_names = [ status._json['user']['screen_name']
#                  for status in results
#                     for mention in status._json['entities']['user_mentions'] ]

userid = [s.user.id for s in resulsts]
    # print status.entities.user_mentions

print userid