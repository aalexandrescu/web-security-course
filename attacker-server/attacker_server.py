from flask import Flask, request
import logging

logging.basicConfig(filename='attacker_server.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
app = Flask(__name__)

@app.route('/api/data', methods=['GET', 'POST'])
def apiData():
    app.logger.info("Responding to request for /api/data")
    headers = request.headers
    # app.logger.info(f"Headers: {headers}")
    app.logger.info(f"request.values: {request.values}")
    app.logger.info(f"request.json: {request.json}")
    return "Hello World!"

if __name__ == '__main__':
  app.run(debug=True)
