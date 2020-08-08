
from flask import Flask,request,Response
from werkzeug.exceptions import HTTPException
import json

#MONGO
from pymongo import MongoClient
mongdb = "llegadas-db"
collection = "llegadas"
#CRED
import os

user = os.getenv('USERMONGO')
passmongo = os.getenv('PASSMONGO')

url = "mongodb+srv://"+user+":"+passmongo+"@cluster0.6zcns.mongodb.net/<dbname>?retryWrites=true&w=majority"

app = Flask(__name__)



@app.route('/api/v1/entrada', methods=['GET','POST'])
def admin_request():

    if request.get_json() is None:

        return get_bad_request_400()
    
    else:

        if request.method == 'GET':
        
            fechas = request.get_json()

            formato_fecha_v1 = ["fecha_inicio","fecha_final"]

            llaves_fechas = list(fechas.keys())

            if formato_fecha_v1 == llaves_fechas:

                client_response=MongoClient(url)[mongdb][collection].find({"fecha": {"$gte": fechas[formato_fecha_v1[0]], "$lt": fechas[formato_fecha_v1[1]]}},{ "_id": False})

                mylist = [x for x in client_response]

                return Response(response = json.dumps(mylist),status = 200,content_type='application/json')

            else:
                return get_bad_request_400()


        else:

            data = request.get_json()

            formato_llegadas_v1 = ["vuelo","fecha","retraso_horas","origen_ciudad","internacional","aerolinea","pasajeros","avion","escala"]

            llaves_llegadas = list(data.keys())

            if formato_llegadas_v1 == llaves_llegadas:

                client_response=MongoClient(url)[mongdb][collection].insert_one(data)

                return Response(status = 201)

            else:
                return get_bad_request_400()


def get_bad_request_400():

    return Response(response=json.dumps({"error":"verifique la petición"}), content_type='application/json', status = 400)





if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0", port=5000)