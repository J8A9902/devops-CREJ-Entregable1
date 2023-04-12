from models.trayecto import Trayecto
from helpers.utils import object_as_dict
from datetime import datetime, timedelta


def crear_trayecto(trayecto):
    status: int = 201
    try:
        ##Valida que no exista un trayecto activo
        diasDiferencia = datetime.now()
        print(datetime.now())
        print(diasDiferencia)
        print(trayecto['sourceAirportCode'])
        print(trayecto['destinyAirportCode'])
        print(trayecto['sourceCountry'])
        print(trayecto['destinyCountry'])
        fechaActual = datetime.now()
        print(fechaActual)
        trayectos = Trayecto.get_trayectos_filter(trayecto['sourceAirportCode'], trayecto['destinyAirportCode'])
        for i in range(len(trayectos)):
            trayecto = trayectos[i]
            diasDiferencia = trayecto.createdAt + timedelta(30)
            if (diasDiferencia >= fechaActual):
                raise Exception("El trayecto ya existe y esta activo")

        nuevo_trayecto = Trayecto(trayecto['sourceAirportCode'], trayecto['sourceCountry'],
                                  trayecto['destinyAirportCode'], trayecto['destinyCountry'], trayecto['bagCost'])
        nuevo_trayecto.save()
        message = {
            "id": nuevo_trayecto.id,
            "createdAt": fechaActual,
            "expireAt": fechaActual + timedelta(30)
        }
    except Exception as e:
        status = 412
        message = f'Error: {e}'

    return message, status


def get_trayecto_by_id(id: int):
    message: str = ''
    status: int = 200
    print(id)
    try:
        trayecto = Trayecto.find_by_id(id)
        message = object_as_dict(trayecto)
    except Exception as e:
        status = 404
        message = {"Error": "No existe el trayecto con ese identificador."}
    print(id)
    return message, status


def find_trayecto(fromCode: str, toCode: str, whenDate: str):
    message: list = []
    status: int = 200
    hayTrayectos = 0
    fechaActual = datetime.now()
    print(fechaActual)
    try:
        if fromCode != '' and toCode != '':
            print(fromCode)
            trayectos = Trayecto.get_trayectos_filter(fromCode, toCode)
        elif fromCode != '':
            print(fromCode)
            trayectos = Trayecto.get_trayectos_by_fromCode(fromCode)
        elif toCode != '':
            print(toCode)
            trayectos = Trayecto.get_trayectos_by_toCode(toCode)
        elif whenDate != '':
            print(whenDate)
            trayectos = Trayecto.get_trayectos()

        if whenDate != '':
            fechaFiltro = datetime.strptime(whenDate, '%Y-%m-%d')
            for i in range(len(trayectos)):
                trayecto = trayectos[i]
                diasDiferencia = trayecto.createdAt + timedelta(30)
                if (diasDiferencia >= fechaActual) and (trayecto.createdAt >= fechaFiltro):
                    trayectoEnv = object_as_dict(trayectos[i])
                    message.append(trayectoEnv)
        else:
            for i in range(len(trayectos)):
                trayecto = trayectos[i]
                diasDiferencia = trayecto.createdAt + timedelta(30)
                if (diasDiferencia >= fechaActual):
                    hayTrayectos = 1
                    trayectoEnv = object_as_dict(trayectos[i])
                    message.append(trayectoEnv)

        if hayTrayectos == 0 and whenDate != '':
            for i in range(len(trayectos)):
                trayectoEnv = object_as_dict(trayectos[i])
                message.append(trayectoEnv)

    except Exception as e:
        status = 400
        message = f'Error: {"Alguno de los valores no tiene un formato correcto."}'

    return message, status
