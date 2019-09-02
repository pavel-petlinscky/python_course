from flask import Flask, request
import os

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = os.environ['S']
#app.config['DB_PASSWORD'] = 'VERY BIG SECRET!'


app.config.update(
    DEBUG=True,
    #SECRET_KEY=os.environ['S'],
)


@app.route('/', methods=['GET', 'POST'])
def home():
    return 'hello world!', 200

#print(request, type(request), request.method)

with app.test_request_context('/test?kjghfdgkj=f', method='POST'):
    print(request, type(request), request.method)

@app.after_request
def a_request1(resp):
    # the variable current_url does not exist
    # but i want something that works like it
    print('After REQUEST!', request)
    return resp

@app.before_request
def before_request1():
    # the variable current_url does not exist
    # but i want something that works like it
    print('BEFORE REQUEST!', request)

@app.before_request
def before_request2():
    # the variable current_url does not exist
    # but i want something that works like it
    print('BEFORE REQUEST2!', request)

if __name__ == '__main__':
    app.run()
