from flask import Flask
app = Flask(__name__)



#@app.route('/test')
@app.route('/post/<int:number>')
def another_home1(number):
    return 'test view {}'.format(number)



@app.route('/<path:username>')
def another_home(username):
    return 'hello user, {}!'.format(username)



if __name__ == '__main__':
    app.run()




















# @app.route('/<user>')
# @app.route('/<path:user_name>')
# def username(user):
#     return 'hello, user: ' + user