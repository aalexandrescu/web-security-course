from flask import Flask, render_template

import logging

logging.basicConfig(filename='target-server.log', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

app = Flask(__name__)
app.config.from_pyfile('config.py')

@app.route('/', methods=['GET', 'POST'])
def index():
    return 'Hello world'


@app.route('/register', methods=['GET'])
def register():
    return render_template('registration_form.html')


# http://localhost:4567/
""" the next function is used only if the program is started with
`python target-server.py`"""
if __name__ == '__main__':
    app.run(debug=True, port=4567)
