import json
import unittest

from api import app

app.testing = True


class TestGET(unittest.TestCase):

    def test_conexion(self):

        with app.test_client() as client:
        
            result = client.get('/api/v1/entrada')
                
            self.assertEqual(result.status_code,200)

    def test_entrada_datos(self):

        with app.test_client() as client:

            resultado_esperado = [{
                                    "vuelo": "AV244",
                                    "fecha": "2020-08-04T20:20:10.000Z",
                                    "retraso_horas": 5,
                                    "origen_ciudad": "Toronto",
                                    "internacional": True,
                                    "aerolinea": "Air Canada",
                                    "pasajeros": 100,
                                    "avion": "787-7",
                                    "escala": False
                                },
                                {
                                    "vuelo": "AV270",
                                    "fecha": "2020-08-04T20:20:10.000Z",
                                    "retraso_horas": 5,
                                    "origen_ciudad": "Toronto",
                                    "internacional": True,
                                    "aerolinea": "Air Canada",
                                    "pasajeros": 100,
                                    "avion": "787-7",
                                    "escala": False
                                }]

            result = client.get('/api/v1/entrada/2020-08-04/2020-08-05')
            
            self.assertEqual(json.dumps(result.json), json.dumps(resultado_esperado))