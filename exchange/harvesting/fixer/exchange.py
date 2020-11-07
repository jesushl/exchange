
class ConsultFixer():
    def __init__(
        self,
        fixer_APIAccessKey:str=None
    ):
        if  fixer_APIAccessKey:
            self.access_key = fixer_APIAccessKey
        else:
           self. access_key  = django_fixer_access
        self.base_url = "http://data.fixer.io/api/"
        self.date_format = "%Y-%m-%d"

    def get_exchange_for(
        self,
        coin_base:str="USD",
        to_exchange:list=['MXN']
    )->dict: 
        response = get(
            self.get_url(
                coin_base=coin_base,
                to_exchange=to_exchange
            )
        )
        return response
    
    def get_url(
        self,
        coin_base:str="USD",
        to_exchange:list=['MXN']
    )->str:
        url = "{base_url}?{api_key}&base={coin_base}&symbols={to_exchange}"
        to_exchange_formated = ','.join(to_exchange)
        _ = url.format(
            base_url=self.base_url,
            api_key=self.access_key,
            coin_base=coin_base,
            to_exchange=to_exchange_formated
        )
        return _