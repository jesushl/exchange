from datetime import datetime
from django.test import TestCase
# data types
from http.client import HTTPResponse
# diario
from harvesting.diario_oficial.scraping import ConsultDiarioOficial


class TestDiarioWebResults(TestCase):
    def setUp(self):
        self.c_diario = ConsultDiarioOficial()
        date_format = "%d-%m-%Y"
        self.now_str = '07-11-2020'
        self.yesterday_str = '06-11-2020'
        self.now_date = datetime.strptime(self.now_str, date_format)
        self.yesterday_date = datetime.strptime(self.yesterday_str, date_format)
        self.dollar_indicator_id = 158

    def test_get_indicator_values(
        self
    ):
        # This test also find other indicators
        today_indicators = {}
        for indicator_id in range(100,200):
            values = self.c_diario.get_indicator_values(
                indicator=indicator_id,
                from_date=self.yesterday_date,
                to_date=self.now_date
            )
            if bool(values):
                today_indicators.update({indicator_id: values})
        knowed_responses = today_indicators.keys()
        for indicator_id in  knowed_responses:
            self.assertIsInstance(
                today_indicators[indicator_id], 
                list, 
                "Indicator {} response in different format".format(indicator_id)
            )
    


    def test_url_builder(self):
        expected_string = (
            "https://www.dof.gob.mx/indicadores_detalle.php?"
            "cod_tipo_indicador=158&"
            "dfecha=06%2F11%2F2020"
            "&hfecha=07%2F11%2F2020"
        )
        self.assertEqual(
            self.c_diario.url_builder(
                    indicator=158,
                    from_date=self.yesterday_date,
                    to_date=self.now_date
                ),
            expected_string,
            "Final query string is not correct"
        )

    def test_get_indicator(self):
        response = self.c_diario.get_inidicator_html(
            indicator=158,
            from_date=self.yesterday_date,
            to_date=self.now_date
        )
        self.assertIsInstance(response, HTTPResponse )
        self.assertEqual(response.status, 200, 'Failure to get 200 on connection with server ')
    
    def test_formater(
        self
    ):
        bad_day = 3
        correct_day = '03'
        _ = self.c_diario.formater(bad_day)
        self.assertEqual(_, correct_day)