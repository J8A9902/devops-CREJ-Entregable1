from flask import Blueprint, jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required, create_access_token
from authentication.auth import login_required
from services.trayecto_service import crear_trayecto, get_trayecto_by_id, find_trayecto
from models.trayecto import Trayecto

trayecto = Blueprint('routes', __name__, url_prefix='/routes')


@trayecto.route('/', methods=['POST'])
@login_required
def create_trayecto(user_id: int):
    data = request.json
    try:
        data['sourceAirportCode'] = data['sourceAirportCode']
        data['sourceCountry'] = data['sourceCountry']
        data['destinyAirportCode'] = data['destinyAirportCode']
        data['destinyCountry'] = data['destinyCountry']
        data['bagCost'] = data['bagCost']
    except Exception as e:
        print("--------------------------------")
        status = 400
        message = 'La petición no contiene todos los campos requeridos.'
        return {'message': message}, status

    response = crear_trayecto(data)

    return response


@trayecto.route('/<trayecto_id>', methods=['GET']) 
@login_required
def get_trayecto_id(user_id):
    try:
        id_trayecto: int = int(request.view_args['trayecto_id'])
        response = get_trayecto_by_id(id_trayecto)

    except Exception as e:
        response = { 'body': 'el id debe ser númerico'}, 400

    return response


@trayecto.route('', methods=['GET'])
@login_required
def get_trayecto_filter(user_id: int):
    args = request.args
    fromCode = ''
    toCode = ''
    whenDate = ''
    if args.get("from") is not None:
        fromCode = args.get("from")
    if args.get("to") is not None:
        toCode = args.get("to")
    if args.get("when") is not None:
        whenDate = args.get("when")

    response = find_trayecto(fromCode, toCode, whenDate)
    return response


@trayecto.route('/ping', methods=['GET'])
def validate_health():
    return 'pong'
