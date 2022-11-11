from flask import Flask,redirect,render_template,url_for,request

import logging
import db_init

logging.basicConfig(filename='target-server.log', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

app = Flask(__name__)
app.config.from_pyfile('config.py')


db_init.init_db()


@app.route('/', methods=['GET', 'POST'])
def index():
    return 'Hello world'


@app.route('/register', methods=['GET'])
def register():
    return render_template('registration_form.html')


@app.route('/confirm-registration', methods=['POST'])
def add_user():
    email = request.form.get('email', '')
    password = request.form.get('password', '')
    confirmPassword = request.form.get('confirmPassword', '')
    print(email)
    return redirect(url_for(app.index))


# http://localhost:4567/
""" the next function is used only if the program is started with
`python target-server.py`"""
if __name__ == '__main__':
    app.run(debug=True, port=4567)
