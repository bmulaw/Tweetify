from flask import Flask
from twitter.auth import API_KEY, API_SECRET, BEARER_TOKEN

app = Flask(__name__)

@app.route('/')
def test():
    return "this is a test"

if __name__ == "__main__":
    app.run(debug=True)
