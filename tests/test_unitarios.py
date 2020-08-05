import json
import unittest

from api import app

app.testing = True


class TestGET(unittest.TestCase):

    def test_entrada_datos(self):

        with app.test_client() as client:

            fechas = {"fecha_inicio":"2020-08-04", "fecha_final":"2020-08-05"}

            resultado_esperado = [{  "vuelo": "AV244",
                                    "fecha": "2020-08-04T20:20:10.000Z",
                                    "retraso_horas": 5,
                                    "destino_ciudad": "Toronto",
                                    "internacional": True,
                                    "aerolínea": "Air Canada",
                                    "Pasajeros": 100,
                                    "avion": "787-7"
                                },
                                {
                                    "vuelo": "AV270",
                                    "fecha": "2020-08-04T20:20:10.000Z",
                                    "retraso_horas": 5,
                                    "destino_ciudad": "Toronto",
                                    "internacional": True,
                                    "aerolínea": "Air Canada",
                                    "Pasajeros": 100,
                                    "avion": "787-7"
                                }]

            result = client.get('/api/v1/entrada',data=json.dumps(fechas),content_type='application/json')
            
            self.assertEqual(json.dumps(result.json), json.dumps(resultado_esperado))



    def test_entrada_fomato(self):
        
        with app.test_client() as client:
            
            fechas = {"fecha_inici":"2020-08-04", "fecha_final":"2020-08-05"}

            result = client.get('/api/v1/entrada',data=json.dumps(fechas),content_type='application/json')

            self.assertEqual(result.status_code, 400)