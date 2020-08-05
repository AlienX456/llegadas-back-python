
from flask import Flask,request,Response
from werkzeug.exceptions import HTTPException
import json

app = Flask(__name__)

@app.route('/api/v1/entrada', methods=['GET','POST'])
def admin_request():

    if request.method == 'GET':
    
        fechas = request.get_json()

        formato_fecha_v1 = ["fecha_inicio","fecha_final"]

        llaves_fechas = list(fechas.keys())

        if formato_fecha_v1 == llaves_fechas:

            return Response(response=json.dumps(fechas),content_type='application/json')

        else:
            error = {"error":'Formato del body erroneo (llaves erroneas)'}
            return Response(response=json.dumps(error), content_type='application/json', status = 400)




if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0", port=5000)