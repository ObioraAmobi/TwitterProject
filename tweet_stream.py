from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

CONSUMER_KEY = 'JECzrghiBaSuECsyKSeROTI6O'
CONSUMER_SECRET = 'L4FUnYLofKZeYay1f56WrHCuqXbf3K7JqUpOYiqgyQzsuxy3vX'
OAUTH_TOKEN = '709340795975954432-9PSTdvZdYTRpio9ZUPBqCeBTaNMQGAh'
OAUTH_TOKEN_SECRET = 'Yw9NCmSxkLkeWOTzakd0nacmMGrcu6ypWaNwwVa0kPwEZ'

keyword_list = ['hilary clinton', 'donald trump', 'president'] #track list

class MyStreamListener(StreamListener):

    def on_data(self, data):
        try:
            with open('tweet_mining.json', 'a') as tweet_file:
                tweet_file.write(data)
                return True
        except BaseException as e:
            print("Failed on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

twitter_stream = Stream(auth, MyStreamListener())
twitter_stream.filter(track=keyword_list)