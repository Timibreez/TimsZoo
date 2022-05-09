import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'timszoo.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'TimsZoo'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'Timibreez'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'Adegbe01'
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'timibreez01'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'SPa4dZYZsS5z5Pl4+l3bVyktqddwRnpcpGT0HVW9UnajxxcFlS8ORS5pf00GDpJDCcu9z5Jlz1hI+9AEuZ91Zw=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'
