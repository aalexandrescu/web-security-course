from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
   return 'Hello world'

# http://localhost:4567/
if __name__ == '__main__':
  app.run(debug=True, port=4567)