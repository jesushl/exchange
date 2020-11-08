# python
from datetime import datetime, timezone
from datetime import timedelta
from urllib3 import PoolManager
import json
import pytz
# settings
from exchange.settings import banxico_APIToken as django_banxico_access

class BanxicoExchange():
    def __init__(
        self,
        banxico_APIToken:str=None
    ):
        if banxico_APIToken:
            self.api_token = banxico_APIToken
        else:
            self.api_token = django_banxico_access
        
        self.date_format = '%Y-%m-%d'
        self.response_date_format = '%d/%m/%Y'
        self.usd_serie_id = "SF43718"
        self.base_url = ("https://www.banxico.org.mx/"
                                        "SieAPIRest/service/v1/"
                                        "series/{serie_id}/"
                                        "datos/{from_date}/{to_date}"
                                    )
        self.MXT = pytz.timezone('America/Mexico_City')
        self.decode = 'utf-8'

    
    def get_header(self):
        return {
            "Accept": "application/json",
            "Bmx-Token": self.api_token
        }
    
    def get_last_exchange(
        self,
        serie_id:str 
    ):
        data_dict = self.get_last_exchange_dict(serie_id=serie_id)
        try:
            datos =  data_dict['bmx']['series'][0]['datos'][0]
            fecha_date_time = datetime.strptime(
                datos['fecha'], 
                self.response_date_format
            )
            return  {
                'date': fecha_date_time, 
                'price': datos['dato']
            }
        except KeyError:
            # TODO: handle this error, this problem comes id api change response 
            # structure
            pass


    def get_last_exchange_dict(
        self,
        serie_id="SF43718"
    ):
        """
        Banxico returns last value from  a day before 
        actual date, date should be same as mexico city
        """
        http  = PoolManager()
        _now  = datetime.now(self.MXT )
        _yesterday = _now - timedelta(days=1)
        response = http.request(
            'GET',
            self.get_url(
                serie_id=serie_id,
                from_date=_yesterday,
                to_date=_now
            ),
            headers=self.get_header()
        )
        return json.loads(response.data.decode(self.decode))

    
    def get_url(
        self,
        serie_id:str,
        from_date:datetime,
        to_date:datetime
    )->str:
        from_date_str = from_date.strftime(self.date_format)
        to_date_str = to_date.strftime(self.date_format)
        url = self.base_url.format(
            serie_id=serie_id,
            from_date=from_date_str,
            to_date=to_date_str
        )
        return url