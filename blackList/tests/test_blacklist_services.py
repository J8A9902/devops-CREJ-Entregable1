import unittest

from services import blackList_service

class blackListTestCase(unittest.TestCase):
    # Prueba de crear un blackList sin correo
    def test_email_create_blackList(self):

        test_response = blackList_service.create_blackList_service({'email':" ",
                                                                    'app_uuid':"123",
                                                                    'blocked_reason':"Mineria",
                                                                    'ip':'123'})
        print('----------------------------------------------')
        print(test_response)

        assert test_response[1] == 400
    
    # Prueba de crear un blackList sin APP_UUID
    def test_uuid_create_blackList(self):

        test_response = blackList_service.create_blackList_service({'email':"ejemplo@fdsfds.co",
                                                                    'app_uuid':" ",
                                                                    'blocked_reason':"Mineria",
                                                                    'ip':'123'})
        print('----------------------------------------------')
        print(test_response)

        assert test_response[1] == 400
    
    # Prueba de crear un blackList sin blocked reason
    def test_reason_create_blackList(self):

        test_response = blackList_service.create_blackList_service({'email':"ejemplo@fdsfds.co",
                                                                    'app_uuid':"123",
                                                                    'blocked_reason':" ",
                                                                    'ip':'123'})
        print('----------------------------------------------')
        print(test_response)

        assert test_response[1] == 400
    
    # Prueba de crear un blackList sin respuesta de la base de datos
    def test_create_blackList(self):

        test_response = blackList_service.create_blackList_service({'email':"ejemplo@fdsfds.co",
                                                                    'app_uuid':"123",
                                                                    'blocked_reason':"Mineria",
                                                                    'ip':'123'})
        print('----------------------------------------------')
        print(test_response)

        assert test_response[1] == 412



# Email Test Cases
def test_get_blackList_by_existing_email(email: str):
    # Create blacklist
    test_email: str = 'test@m.com'
    test_response = blackList_service.create_blackList_service({'email': test_email,
                                                                    'app_uuid':"123",
                                                                    'blocked_reason':"",
                                                                    'ip': '127.0.0.0'})


    test_response = blackList_service.get_blackList_by_email(test_email)

    assert test_response[1] == 200


def test_get_blackList_by_unexisting_email(email: str):
    # Create blacklist
    test_email: str = 'test1@m.com'
    test_response = blackList_service.create_blackList_service({'email': test_email,
                                                                    'app_uuid':"123",
                                                                    'blocked_reason':"", 
                                                                    'ip': '127.0.0.0'})


    test_response = blackList_service.get_blackList_by_email('1212121212@gsfdf.com')

    assert test_response[1] == 404