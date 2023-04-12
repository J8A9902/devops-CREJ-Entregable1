from flask import Blueprint, jsonify, request
import flask
from services.blackList_service import create_blackList_service, get_blackList_by_email

blackList = Blueprint('blacklists', __name__, url_prefix='/blacklists')


@blackList.route('/', methods=['POST'])
def create_blackList():
    responeToken = login_required()
    if responeToken == False: 
        status = 400
        message = 'El token no es válido.'
        return {'message': message}, status
    data = request.json
    print(data)
    try:
        data['email'] = data['email']
        data['app_uuid'] = data['app_uuid']
        data['blocked_reason'] = data['blocked_reason']
    except Exception as e:
        print("--------------------------------")
        status = 400
        message = 'La petición no contiene todos los campos requeridos.'
        return {'message': message}, status
    print('--------------------------')
    print(data)
    response = create_blackList_service(data)

    return response


@blackList.route('/<email>', methods=['GET']) 
def get_blackList_id(email):
    responeToken = login_required()
    if responeToken == False: 
        status = 400
        message = 'El token no es válido.'
        return {'message': message}, status
    try:
        response = get_blackList_by_email(email)

    except Exception as e:
        response = { 'body': 'error en el correo'}, 400

    return response


def login_required():
    headers = flask.request.headers
    if('Authorization' in headers):
        auth = headers['Authorization']
        print(auth)
        if auth != "Bearer 123456":
            return False    
    else:
        return False

    return True