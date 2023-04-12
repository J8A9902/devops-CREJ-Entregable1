from flask import Blueprint, jsonify, request
from authentication.auth import login_required
from services.blackList_service import create_blackList_service

trayecto = Blueprint('blacklists', __name__, url_prefix='/blacklists')


@trayecto.route('/', methods=['POST'])
#@login_required
def create_blackList():
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


# @trayecto.route('/<trayecto_id>', methods=['GET']) 
# @login_required
# def get_trayecto_id(user_id):
#     try:
#         id_trayecto: int = int(request.view_args['trayecto_id'])
#         response = get_trayecto_by_id(id_trayecto)

#     except Exception as e:
#         response = { 'body': 'el id debe ser númerico'}, 400

#     return response


