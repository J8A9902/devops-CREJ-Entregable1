import flask
from functools import wraps


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        headers = flask.request.headers

        if('Authorization' in headers):
            auth = headers['Authorization']
            print(auth)
            if auth != "Bearer 123456":
                return flask.jsonify({'message': '	El token no es válido o está vencido.'}), 401    
        else:
            return flask.jsonify({'message': '	El token no es válido o está vencido.'}), 401
    return decorated_function