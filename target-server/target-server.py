from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return 'Hello world'


# http://localhost:4567/
""" the next function is used only if the program is started with
`python target-server.py`"""
if __name__ == '__main__':
    app.run(debug=True, port=4567)
