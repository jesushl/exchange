# python
from urllib3 import PoolManager
import json
from datetime import datetime
# django
from django.test import TestCase
# local
from harvesting.fixer.exchange import FixerExchange

class ConsultFixerTest(TestCase):
    def setUp(self):
        self.consultFixer_client = FixerExchange()

    def test_get_last_exchange_USD_MXN(self):
        _ = self.consultFixer_client.get_last_exchange_USD_MXN()
        self.assertIsInstance(_['date'], datetime)
        self.assertIsInstance(_['price'] , float)
        
    def test_get_last_exchange(
        self
    ):
        _ = self.consultFixer_client.get_last_exchange(
            coin_base='EUR',
            to_exchange=['MXN']
        )
        self.assertEqual(_['success'], True)
    
    def test_USD_access(self):
        _ = self.consultFixer_client.get_last_exchange(
            coin_base='USD',
            to_exchange=['MXN']
        )
        self.assertEqual(_['success'], True, "Fixer is not accesing to USD")
        if  _['success'] == False:
            usd_restricted_msg = "'base_currency_access_restricted'"
            self.assertEqual(
                _['error']['type'], 
                usd_restricted_msg,
                "Access is not caused by key restriction: {} ".format(
                    _['error']
                )
            )

    
    def test_api_key_validation(self):
        key = self.consultFixer_client.access_key
        self.assertIsNotNone(
            key, 
            "Access keyu for Fixer is None, change settings value or add fixer env var "
        )
        url = "{base_url}?access_key={api_key}".format(
            base_url=self.consultFixer_client.base_url,
            api_key=self.consultFixer_client.access_key,
        )
        http  =     PoolManager()
        response = http.request('GET', url)
        self.assertEqual(response.status, 200, 'Default response for key fails')
        response_dict = json.loads(response.data.decode(self.consultFixer_client.decode))
        self.assertNotEqual(
            response_dict['success'], 
            False, 
            "Default response from server is not successful"
        )
        url = "{base_url}?access_key={api_key}".format(
            base_url=self.consultFixer_client.base_url,
            api_key='bad_key'
        )
        response = http.request('GET', url)
        response_dict = json.loads(response.data.decode(self.consultFixer_client.decode))
        self.assertEqual(
            response_dict['success'], 
            False, 
            """Bad key retuns  a sucess value,
             this require a documentation revission with fixer: {}
             """.format(
                response_dict['error']['info']
            )
        )