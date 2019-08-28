from flask import Flask
import time

app = Flask(__name__)

@app.route('/')
def hello():
    time.sleep(10)
    return 'Hello, World!'

app.run()
