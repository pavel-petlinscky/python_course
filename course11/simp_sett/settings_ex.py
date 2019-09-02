from flask import Flask, request
from simple_settings import settings

app = Flask(__name__)
app.config.update(**settings.as_dict())


@app.route('/', methods=['GET', 'POST'])
def home():
    return 'hello world!', 200

# print(request, type(request), request.method)

# with app.test_request_context('/?next=http://example.com/'):
#     print(request, type(request), request.method)


if __name__ == '__main__':
    app.run()
