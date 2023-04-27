from models.blackList import blackList as BlackList
from helpers.utils import object_as_dict


def create_blackList_service(blackList):
    status: int = 200
    try:
        if blackList['email'] == ' ':
            status = 400
            message = {"Error": "Email ingresado no es válido."}
            return message, status
        elif blackList['app_uuid'] == ' ':
            status = 400
            message = {"Error": "El UUID de la app no es válido"}
            return message, status
        elif blackList['blocked_reason'] == ' ':
            status = 400
            message = {"Error": "Debe completar la razón del bloqueo."}
            return message, status

        new_blackList = BlackList(blackList['email'], blackList['app_uuid'], blackList['blocked_reason'], blackList['ip'])
        new_blackList.save()
        message = {"Message": "Se agrego el email correctamente"}
    except Exception as e:
        status = 412
        message = f'Error: {e}'

    return message, status


def get_blackList_by_email(email: str):
    message: str = ''
    status: int = 200
    print(id)
    try:
        blackList = BlackList.find_by_email(email)
        message = object_as_dict(blackList)
    except Exception as e:
        status = 404
        message = {"Error": "No existe el blackList con ese identificador."}
    return message, status

