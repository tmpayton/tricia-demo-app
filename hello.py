import os
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'This is a second test of an automatic CI/CD pipeline!'


port = os.getenv('PORT', '8080')
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(port))
