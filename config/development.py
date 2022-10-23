class Config(dict):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///./../data/movies.db'
    SQLALCHEMY_TRACK_NOTIFICATION = False
