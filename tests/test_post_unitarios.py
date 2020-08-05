import json
import unittest

from api import app

app.testing = True


class TestPOST(unittest.TestCase):

    def test_entrada_datos(self):

        with app.test_client() as client:

            data = {
                    "vuelo": "AV852",
                    "fecha": "2020-09-04T20:20:10.000Z",
                    "retraso_horas": 5,
                    "origen_ciudad": "Toronto",
                    "internacional": True,
                    "aerolinea": "Air Canada",
                    "pasajeros": 100,
                    "avion": "787-7",
                    "escala": False
                    }

            result = client.post('/api/v1/entrada',data=json.dumps(data),content_type='application/json')
            
            self.assertEqual(result.status_code, 201)



    def test_entrada_fomato(self):
        
        with app.test_client() as client:
            
            data = {
                        "vuel": "AV270",
                        "fecha": "2020-08-04T20:20:10.000Z",
                        "retraso_horas": 5,
                        "origen_ciudad": "Toronto",
                        "internacional": True,
                        "aerolinea": "Air Canada",
                        "pasajeros": 100,
                        "avion": "787-7",
                        "escala": False
                    }

            result = client.post('/api/v1/entrada',data=json.dumps(data),content_type='application/json')

            self.assertEqual(result.status_code, 400)