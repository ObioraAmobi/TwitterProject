import tweepy
from tweepy import OAuthHandler
from auth import get_api

api = get_api()

user = api.get_user('@madonna')

print(user.screen_name)
print(user.followers_count)

for friend in user.friends():
    print
    print(friend.screen_name)
    print(friend.followers_count)


# harvest tweets on homeline
for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a tweet
    print(status.text)