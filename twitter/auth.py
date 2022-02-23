from decouple import config
import tweepy

API_KEY = config('API_KEY')
API_SECRET = config('API_SECRET')
BEARER_TOKEN = config('BEARER_TOKEN')
ACCESS_TOKEN = config('ACCESS_TOKEN')
ACCESS_SECRET = config('ACCESS_SECRET')

def OAuth():
    try:
        auth = tweepy.OAuthHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
        return auth
    except Exception as e:
        return e

oauth = OAuth()
api = tweepy.API(oauth)
api.verify_credentials()
api.update_status('My first tweet using Python')