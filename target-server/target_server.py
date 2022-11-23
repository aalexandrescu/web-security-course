from flask import Flask,redirect,render_template,url_for,request,session

# The Session instance is not used for direct access, you should always use flask.session
from flask_session import Session

import logging
import db_init

logging.basicConfig(filename='target_server.log', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

app = Flask(__name__)
app.config.from_pyfile('config.py')

# configure the session
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem" # the session is stored under a /flask_session directory
Session(app)

db_init.init_db()


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


''' User registration logic '''

@app.route('/register', methods=['GET'])
def register():
    return render_template('registration_form.html')


@app.route('/confirm-registration', methods=['POST'])
def add_user():
    email = request.form.get('email', '')
    password = request.form.get('password', '')
    confirmPassword = request.form.get('confirmPassword', '')
    # TODO
    print(email)
    return redirect(url_for('index'))

''' End User registration logic '''

''' User authentication logic '''

@app.route('/login', methods=['GET'])
def login():
    return render_template('login_form.html')


@app.route('/confirm-login', methods=['POST'])
def confirm_login():   
    email = request.form.get('email', '')
    print('confirm_login: %s' % email)
    password = request.form.get('password', '')
    # TODO - it is a trivial example email == password
    if (email == password):
        # save the email in the email session variable
        session["email"] = email
        return redirect(url_for('my_account'))
    else:
        return redirect(url_for('login'))


@app.route('/my-account', methods=['GET'])
def my_account():
    print('my_account: %s' % session.get("email"))
    # if the user is not authenticated, i.e., the `email` session property does not exist
    if not session.get("email"):
        # redirect the user to the login page
        return redirect(url_for('login'))
    else:
        # obtain the email address from the session object and send it to the renderer
        return render_template('my_account.html', emailAddress = session.get("email"))


''' End User authentication logic '''

# http://localhost:4567/
""" the next function is used only if the program is started with
`python target-server.py`"""
if __name__ == '__main__':
    app.run(debug=True, port=4567)
