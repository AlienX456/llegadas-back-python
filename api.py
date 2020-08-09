
from flask import Flask,request,Response
from werkzeug.exceptions import HTTPException
import json
from datetime import datetime

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

@app.route('/api/v1/entrada', methods=['GET'])
def testear():
    return Response(status = 200)

@app.route('/api/v1/entrada/<fecha_inicio>/<fecha_final>', methods=['GET'])
def buscar(fecha_inicio,fecha_final):

    try:
        datetime.strptime(fecha_inicio, '%Y-%m-%d')
        datetime.strptime(fecha_final, '%Y-%m-%d')
    except ValueError:
        return Response(status = 400)
    

    client_response=MongoClient(url)[mongdb][collection].find({"fecha": {"$gte": fecha_inicio, "$lt": fecha_final}},{ "_id": False})

    mylist = [x for x in client_response]

    return Response(response = json.dumps(mylist),status = 200,content_type='application/json')




@app.route('/api/v1/entrada', methods=['POST'])
def registrar():

    if request.get_json() is None:

        return get_bad_request_400()
    
    else:

        data = request.get_json()

        formato_llegadas_v1 = ["vuelo","fecha","retraso_horas","origen_ciudad","internacional","aerolinea","pasajeros","avion","escala"]

        llaves_llegadas = list(data.keys())

        if formato_llegadas_v1 == llaves_llegadas:

            client_response=MongoClient(url)[mongdb][collection].insert_one(data)

            return Response(status = 201)

        else:
            return Response(status = 400)






if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0", port=5000)