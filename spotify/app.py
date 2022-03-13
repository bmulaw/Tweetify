from flask import Flask
from decouple import config
import spotipy
import spotipy.util as util

app = Flask(__name__)

client_id = config('CLIENT_ID')
client_secret = config('CLIENT_SECRET')

token = util.prompt_for_user_token(
             username,
             scope,
             client_id=client_id, 
             client_secret=client_secret,
             redirect_uri='http://localhost:5000/') 
sp = spotipy.Spotify(auth=token)

@app.route('/')
def test():
    return "this is a test on spotify.py"

if __name__ == "__main__":
    app.run(debug=True)
