import logging
import db_init
import json
import requests

from flask import Flask,redirect,render_template,url_for,request,session
from flask_oidc import OpenIDConnect

# The Session instance is not used for direct access, you should always use flask.session
from flask_session import Session



logging.basicConfig(filename='target_server.log', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

app = Flask(__name__)
app.config.from_pyfile('config.py')

app.config.update({
    'SECRET_KEY': 'SomethingNotEntirelySecret',
    'TESTING': True,
    'DEBUG': True,
    'OIDC_CLIENT_SECRETS': 'client_secrets.json',
    'OIDC_ID_TOKEN_COOKIE_SECURE': False,
    'OIDC_REQUIRE_VERIFIED_EMAIL': False,
    'OIDC_USER_INFO_ENABLED': True,
    'OIDC_OPENID_REALM': 'flask-demo',
    'OIDC_SCOPES': ['openid', 'email', 'profile'],
    'OIDC_INTROSPECTION_AUTH_METHOD': 'client_secret_post'
})


# configure the session
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem" # the session is stored under a /flask_session directory
Session(app)

db_init.init_db()

oidc = OpenIDConnect(app)

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

# secure access to route /private

@app.route('/private')
@oidc.require_login
def hello_me():
    """Example for protected endpoint that extracts private information from the OpenID Connect id_token.
       Uses the accompanied access_token to access a backend service.
    """
    print("hello_me")
    info = oidc.user_getinfo(['preferred_username', 'email', 'sub'])
    print(info)
    username = info.get('preferred_username')
    email = info.get('email')
    user_id = info.get('sub')

    if user_id in oidc.credentials_store:
        try:
            from oauth2client.client import OAuth2Credentials
            access_token = OAuth2Credentials.from_json(oidc.credentials_store[user_id]).access_token
            print("access_token=<%s>" % access_token)
            headers = {'Authorization': 'Bearer %s' % (access_token)}
            # YOLO
            greeting = requests.get('http://localhost:8080/greeting', headers=headers).text
        except:
            print("Could not access greeting-service")
            greeting = "Hello %s" % username
    

    return ("""%s your email is %s and your user_id is %s!
               <ul>
                 <li><a href="/">Home</a></li>
                 <li><a href="//81.180.223.163:5039/realms/swrealm/account?referrer=flask-app&referrer_uri=http://localhost:5000/private&">Account</a></li>
                </ul>""" %
            (greeting, email, user_id))




# http://localhost:4567/
""" the next function is used only if the program is started with
`python target-server.py`"""
if __name__ == '__main__':
    app.run(debug=True, port=4567)
