from os import path

SQLALCHEMY_DATABASE_URI = f'sqlite:///{path.abspath("storage.db")}'
ENV = 'development'
DEBUG = True
TESTING = True
