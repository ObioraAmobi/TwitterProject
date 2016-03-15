import json
import tweepy
from tweepy import OAuthHandler

CONSUMER_KEY = 'JECzrghiBaSuECsyKSeROTI6O'
CONSUMER_SECRET = 'L4FUnYLofKZeYay1f56WrHCuqXbf3K7JqUpOYiqgyQzsuxy3vX'
OAUTH_TOKEN = '709340795975954432-9PSTdvZdYTRpio9ZUPBqCeBTaNMQGAh'
OAUTH_TOKEN_SECRET = 'Yw9NCmSxkLkeWOTzakd0nacmMGrcu6ypWaNwwVa0kPwEZ'

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

api = tweepy.API(auth)

DUB_WOE_ID = 560743
LON_WOE_ID = 44418

dub_trends = api.trends_place(DUB_WOE_ID)
lon_trends = api.trends_place(LON_WOE_ID)

# print json.dumps(dub_trends, indent=1)
# print json.dumps(lon_trends, indent=1)

dub_trends_set = set([trend['name']
                      for trend in dub_trends[0]['trends']])

lon_trends_set = set([trend['name']
                      for trend in lon_trends[0]['trends']])

common_trends = set.difference(dub_trends_set, lon_trends_set)

# print common_trends