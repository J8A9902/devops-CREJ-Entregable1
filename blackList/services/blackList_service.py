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


# def get_trayecto_by_id(id: int):
#     message: str = ''
#     status: int = 200
#     print(id)
#     try:
#         trayecto = Trayecto.find_by_id(id)
#         message = object_as_dict(trayecto)
#     except Exception as e:
#         status = 404
#         message = {"Error": "No existe el trayecto con ese identificador."}
#     print(id)
#     return message, status

