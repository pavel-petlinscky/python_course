# -*- coding: utf-8 -*-

from datetime import timedelta

import six

from flask import Flask, jsonify, make_response, request, current_app
from functools import update_wrapper


app = Flask(__name__)


def crossdomain(origin=None, methods=None, headers=None,
                max_age=21600, attach_to_all=True,
                automatic_options=True):
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance(headers, six.string_types):
        headers = ', '.join(x.upper() for x in headers)
    if not isinstance(origin, six.string_types):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(f):
        def wrapped_function(*args, **kwargs):
            if automatic_options and request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers

            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            return resp

        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)
    return decorator


@app.route('/ajax/<result>')
@crossdomain('*')
def ajax_method(result):
    if result == 'success':
        return jsonify({'status': result})
    else:
        resp = jsonify({'status': 'fail'})
        resp.status_code = 500
        return resp

def ll(f):
    print(f())

def foo(x):
    def bar():
        return x

    ll(bar)

if __name__ == '__main__':
    app.run()
