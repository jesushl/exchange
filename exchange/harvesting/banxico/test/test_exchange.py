# django
from django.test import TestCase
# local
from harvesting.banxico.exchange import BanxicoExchange

class BanxicoExchangeTest(TestCase):
    
    def setUp(self):
        self.exchange = BanxicoExchange()
        self.usd_serie_id = "SF43718"

    def rest_last_exchange_dict(self):
        last_price =  self.exchange.get_last_exchange_dict(
            serie_id=self.usd_serie_id
        )
        self.assertIsInstance(dict, last_price)
    
    def test_get_last_exchange(self):
        last_price =  self.exchange.get_last_exchange(
            serie_id=self.usd_serie_id
        )
        self.assertIsInstance(last_price, dict)
        current_keys = ['date', 'price']
        for key in current_keys:
            self.assertIn(key, last_price.keys())
        