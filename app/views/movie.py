from flask_restx import Resource, Namespace
from app.service_container import movie_service as service
from app.dao.models.movie import MovieScheme
from flask import request

movies_ns = Namespace('movies')
models_scheme = MovieScheme(many=True)
model_scheme = MovieScheme()


@movies_ns.route('/')
class MoviesView(Resource):
    def get(self):
        director_id = None
        genre_id = None
        year = None
        args = request.args

        if "director_id" in args:
            director_id = args.get("director_id")

        if "genre_id" in args:
            genre_id = args.get("genre_id")

        if "year" in args:
            year = args.get("year")
        models = service.get_all(director_id=director_id, genre_id=genre_id, year=year)
        print(models)
        return models_scheme.dump(models), 200

    def post(self):
        try:
            service.create(request.json)
            return "", 201
        except Exception as e:
            return str(e), 404

@movies_ns.route('/<int:id>')
class MovieView(Resource):
    def get(self, id: int):
        try:
            model = service.get_one(id)
            return model_scheme.dump(model), 200
        except Exception as e:
            return str(e), 404

    def put(self, id: int):
        try:
            data = request.json
            service.update(data, id)
            return "", 204
        except Exception as e:
            return str(e), 404

    def patch(self, id: int):
        try:
            data = request.json
            service.update_particular(data, id)
            return "", 204
        except Exception as e:
            return str(e), 404

    def delete(self, id: int):
        service.delete(id)
        return "", 204