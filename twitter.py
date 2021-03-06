from decouple import config
import tweepy

class Twitter():

    def __init__(self):
        self.API_KEY = config('T_API_KEY')
        self.API_SECRET = config('T_API_SECRET')
        self.BEARER_TOKEN = config('T_BEARER_TOKEN')
        self.ACCESS_TOKEN = config('T_ACCESS_TOKEN')
        self.ACCESS_SECRET = config('T_ACCESS_SECRET')

    def setOAuth(self):
        try:
            auth = tweepy.OAuthHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
            auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
            return auth, 200
        except Exception as e:
            return e, 404
        
    def sendTestTweet(self):
        oauth = self.setOAuth()
        api = tweepy.API(oauth)
        api.verify_credentials()
        api.update_status('My first tweet using Python')


if __name__ == "__main__":
    app.run(debug=True)

