from datetime import datetime
import unittest
# diario
from harvesting.diario_oficial.scraping import ConsultDiarioOficial
class TestDiarioWebResults(unittest.TestCase):
    def setUp(self):
        self.c_diario = ConsultDiarioOficial()
        date_format = "%d-%m-%Y"
        self.now_str = '07-11-2020'
        self.yesterday_str = '06-11-2020'
        self.now_date = datetime.strptime(self.now_str, date_format)
        self.yesterday_date = datetime.strptime(self.yesterday_str, date_format)
    
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
       import pdb; pdb.set_trace()
