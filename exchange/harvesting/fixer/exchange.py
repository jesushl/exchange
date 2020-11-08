import json
from urllib3 import PoolManager
# settings 
from exchange.settings import fixer_APIAccessKey as django_fixer_access


class FixerExchange():
    def __init__(
        self,
        fixer_APIAccessKey:str=None
    ):
        if  fixer_APIAccessKey:
            self.access_key = fixer_APIAccessKey
        else:
           self. access_key  = django_fixer_access
        self.base_url = "http://data.fixer.io/api/latest"
        self.date_format = "%Y-%m-%d"
        self.decode = 'utf-8'

    def get_last_exchange(
        self,
        coin_base:str="USD",
        to_exchange:list=['MXN']
    )->dict: 
        url = self.get_url(
                coin_base=coin_base,
                to_exchange=to_exchange
            )
        http  =     PoolManager()
        response = http.request('GET', url)
        if response.status == 200:
            return json.loads(response.data.decode(self.decode))
        else:
            raise ConnectionError 
            
    def get_url(
        self,
        coin_base:str="USD",
        to_exchange:list=['MXN']
    )->str:
        url = ("{base_url}?access_key={api_key}&"
            "base={coin_base}&symbols={to_exchange}"
        )
        to_exchange_formated = ','.join(to_exchange)
        _ = url.format(
            base_url=self.base_url,
            api_key=self.access_key,
            coin_base=coin_base,
            to_exchange=to_exchange_formated
        )
        return _