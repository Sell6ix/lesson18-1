class Config(dict):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///prod_db'
    SQLALCHEMY_TRACK_NOTIFICATION = True
