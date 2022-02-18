from distutils.log import debug
from flask import Flask

app = Flask(__name__)

@app.route('/')
def test():
    return "this is a test"

if __name__ == "__main__":
    app.run(debug=True)
