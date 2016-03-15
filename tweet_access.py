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

count = 50
query = 'Dublin'

results = [status for status in tweepy.Cursor(api.search, q=query).items(count)]

# for result in results:
#     print results

# for result in results:
#     print json.dumps(result._json, indent=2)

print json.dumps(results[0]._json, indent=4)

for status in results:
    print status.text.encode('utf-8')
    print status.user.id
    print status.user.screen_name
    print status.user.profile_image_url_https
    print status.user.followers_count
    print status.place