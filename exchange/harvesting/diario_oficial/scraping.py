from datetime import datetime
from datetime import timedelta
from urllib.request import urlopen
# external
from lxml import etree

class  ConsultDiarioOficial():
    """
    This class consult indicator values from 
    https://www.dof.gob.mx/
    This method use lxml to extract html result
    """
    def __init__(
        self,
        url:str="https://www.dof.gob.mx/indicadores_detalle.php?"
    ):
        self.indicators_url = url
        self.indicators_query_body = (
            "cod_tipo_indicador={indicator_type}"
            "&dfecha={from_day}%2F{from_month}%2F{from_year}"
            "&hfecha={to_day}%2F{to_month}%2F{to_year}"
            )
        self.xpath_search_pathern = '//tr[contains(@class, "Celda 1")]//td//text()'
        
    def get_last_price_for_idicator(
        self,
        indicator_id:int
    ):
        """
        This method gets last valuation for spected indicator,
        indicators limits was calculated from test_diario_oficial 
        to see how many indicators responds with a 200 value
        """
        now_date = datetime.now()
        yesterday_date = now_date - timedelta(days=1)
        return self.get_indicator_values(
            indicator=indicator_id,
            from_date=yesterday_date,
            to_date=now_date
        )
    
    def get_indicator_values(
        self,
        indicator:int,
        from_date:datetime, 
        to_date:datetime
    )->list:
        indicator_responce =  self.get_inidicator_html(
            indicator=indicator,
            from_date=from_date,
            to_date=to_date
        )
        parser = etree.HTMLParser()
        tree = etree.parse(indicator_responce, parser)
        return tree.xpath(self.xpath_search_pathern)

    def get_inidicator_html(
        self,
        indicator:int,
        from_date:datetime,
        to_date:datetime
    ):
        url = self.url_builder(
            indicator=indicator,
            from_date=from_date,
            to_date=to_date
        )
        return urlopen(url)

    def url_builder(
        self,
        indicator:int,
        from_date:datetime,
        to_date:datetime
    )->str:
        query =  self.indicators_query_body .format(
            indicator_type=indicator,
            from_day=self.formater(from_date.day),
            from_month=self.formater(from_date.month),
            from_year=from_date.year,
            to_day=self.formater(to_date.day),
            to_month=self.formater(to_date.month),
            to_year=to_date.year
        )
        url = "{url}{query}".format(
            url=self.indicators_url,
            query=query
        )
        return url

    def formater(
        self,
        value:int,
        ljust_val:int=2
    )->str:
        return '{value}'.format(value=value).rjust(ljust_val, '0')