from flask import Flask
from flask import json
import logging

app = Flask(__name__)

@app.route("/")
def hello():
    app.logger.info('Main request successfull')
    return "Hello World!"

@app.route("/status")
def healthcheck():
    response = app.response_class(
        response=json.dumps({"results":"OK - healthy"}),
        status=200,
        mimetype='application/json'
    )
    app.logger.info('Status request sucessfull')
    return response

@app.route("/metrics")
def metrics():
    response=app.response_class(
        response=json.dumps({"status":"success","code":0,"data":{"UserCount":140,"UserCountActive":23}}),
        status=200,
        mimetype='application/json'
    )
    app.logger.info('Metrics request successfull')
    return response


if __name__ == "__main__":
    
    logging.basicConfig(filename=app.log, level=logging.DEBUG)
    app.run(host='0.0.0.0')
