import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database


# TODO IMPLEMENT DATABASE URL<Put your local database url>
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:Raudin@localhost:5432/fyyur'
