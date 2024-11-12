from flask import Flask
import os
import sqlalchemy
from yaml import load, Loader

#run: python -m flask run in order to start the app locally


def init_connection_engine():
    """ initialize database setup
    Takes in os variables from environment if on GCP
    Reads in local variables that will be ignored in public repository.
    Returns:
        pool -- a connection to GCP MySQL
    """
    # detect env local or gcp
    if os.environ.get('GAE_ENV') != 'standard':
        try:
            variables = load(open("app.yaml"), Loader=Loader)
        except OSError as e:
            print("Make sure you have the app.yaml file setup")
            exit()

        env_variables = variables['env_variables']
        for var in env_variables:
            os.environ[var] = env_variables[var]

    pool = sqlalchemy.create_engine(
        sqlalchemy.engine.url.URL(
            drivername="mysql+pymysql",
            username=os.environ.get('MYSQL_USER'),
            password=os.environ.get('MYSQL_PASSWORD'),
            database=os.environ.get('MYSQL_DB'),
            host=os.environ.get('MYSQL_HOST'),
            port=os.environ.get('MYSQL_PORT', 3306),
            query={}
        )
    )

    return pool

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
db = init_connection_engine()

from app import routes