# web-security-course

## Configuring the Python project

Source: https://flask.palletsprojects.com/en/2.2.x/installation/

Create a directory for the project and, inside the directory, create a virtual environment with the `venv` module.

```
mkdir myproject
cd myproject
py -3 -m venv venv
````

Activate the environment:
```
venv\Scripts\activate
```

Install Flask within the activated environment:
```
pip install Flask
```

## Running the Python web server

```
flask --app target-server --debug run --port 4567 --host=0.0.0.0
```

The `--host=0.0.0.0` argument exposes the web application on all IPs.


If error when importing from flask_oidc then downgrade: pip install itsdangerous==2.0.1

## Verificarea problemelor de linting

```
pip install flake8
```
Din directorul `target-server`:
```
flake8 .\target-server.py
```
