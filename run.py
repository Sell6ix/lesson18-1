from app import create_app
from flask import Flask
from flask_restx import Api
from app.database import db
from app.views.genre import genre_ns
from app.views.director import directors_ns
from app.views.movie import movies_ns


def configure_app(application: Flask):
    ''' Configure flask app. Api with namespaces and create data.'''
    with application.app_context():
        db.init_app(application)
        db.create_all()
        api = Api(application)
        api.add_namespace(genre_ns)
        api.add_namespace(directors_ns)
        api.add_namespace(movies_ns)
        create_data(app, db)


def create_data(app, db):
    '''Create default data in databse'''
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    app = create_app()
    configure_app(app)
    app.run()
