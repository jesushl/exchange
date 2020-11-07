from datetime import datetime
from datetime import timedelta
# external
import wget

class  consult_diario_oficial():
    def __init__(
        self,
        url:str="https://www.dof.gob.mx/indicadores_detalle.php?"
    ):
        self.indicators_url = url
        self.indicators_query_body = (
            """cod_tipo_indicador={indicator_type}
            &dfecha={from_day}%2F{from_month}%2F{from_year}
            &hfecha={to_day}%2F{to_month}%2F{to_year}
            """)
        
    def get_last_price_for_idicator(
        self,
        indicator_id:int
    ):
        now_date = datetime.now()
        yesterday_date = now_date - timedelta(days=1)
    
    def get_inidicator_html(
        self,
        from_date:datetime,
        to_date:datetime
    ):
        wget.downlo


    def url_builder(
        self,
        indicator:int,
        from_date:datetime,
        to_date:datetime
    ):
        query =  self.indicators_query_body .format(
            indicator_type=indicator,
            from_day=from_date.day,
            from_month=from_date.month,
            from_year=from_date.year,
            to_day=to_date.day,
            to_month=to_date.month,
            to_year=to_date.year
        )
        url = "{url}{query}".format(
            url=self.indicators_url,
            query=query
        )

        result =  wget.download(url)
        return result