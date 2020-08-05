
from flask import Flask,request
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

@app.route('/api/v1/entrada', methods=['GET','POST'])
def admin_request():
    return None


#Error Handler propuesto por flask
@app.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response



if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0", port=5000)