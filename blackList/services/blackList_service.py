from models.blackList import blackList as BlackList
from helpers.utils import object_as_dict


def create_blackList_service(blackList):
    status: int = 200
    try:
        new_blackList = BlackList(blackList['email'], blackList['app_uuid'], blackList['blocked_reason'], '99.65.122.3')
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

