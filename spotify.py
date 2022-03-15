from decouple import config
import spotipy
import spotipy.util as util
from twitter import Twitter

class Spotify(Twitter):

    def __init__(self):
        super
        self.client_id = config('S_CLIENT_ID')
        self.client_secret = config('S_CLIENT_SECRET')
        self.expires_in = 3600

    def getAccessToken(self):
        token = util.prompt_for_user_token(
                    username,
                    scope,
                    client_id=self.client_id, 
                    client_secret=self. client_secret,
                    redirect_uri='http://localhost:5000/') 
        sp = spotipy.Spotify(auth=token)
        return sp
    
    # def isNewSongLikedByUser(self):
        # TODO: check if user has liked a new song on Spotify by comparing with second most recent liked song

    # def getUsersTweeterAuth():
        # TODO: call parent class Twitter to get user's Auth and send tweet if prev method (isNewSnogLikedByUser) is true



if __name__ == "__main__":
    app.run(debug=True)
