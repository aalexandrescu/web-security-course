from flask import Flask, request, jsonify, json, make_response
import logging

# logging.basicConfig(filename='attacker_server.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
app = Flask(__name__)

@app.route('/api/data', methods=['GET', 'POST', 'OPTIONS'])
def apiData():
    try:
        # app.logger.info("Responding to request for /api/data")
        headers = request.headers
        # app.logger.info(f"Headers: {headers}")
        # app.logger.info(f"request.values: {request.values}")
        # app.logger.info(f"request.json: {request.json}")
        # response = jsonify({ "mesaj": "Hello World!" })
        # print(request.json)
        
        response = make_response()
        response.headers.add("Access-Control-Allow-Origin", "*")
        response.headers.add('Access-Control-Allow-Headers', "*")
        response.headers.add('Access-Control-Allow-Methods', "*")
        response.content_type = "application/json"
        response.data = json.dumps({ "mesaj": "Hello World!" })
        response.status_code = 200
        print(response)
        return response
    except Exception as e:
        print(e)
        response = make_response()
        response.status_code = 500
        return response 
      

if __name__ == '__main__':
  app.run(debug=True)
