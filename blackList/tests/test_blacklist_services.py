import unittest

from services import blackList_service

class blackListTestCase(unittest.TestCase):
    def test_create_blackList(self):

        test_response = blackList_service.create_blackList_service({'email':"ejemplo@fdsfds.co",
                                                                    'app_uuid':"123",
                                                                    'blocked_reason':""})
        print('----------------------------------------------')
        print(test_response)

        assert test_response[1] == 412
