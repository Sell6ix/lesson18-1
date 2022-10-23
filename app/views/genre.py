from flask_restx import Resource, Namespace
from app.service_container import genre_service as service
from app.dao.models.genre import GenreScheme

genre_ns = Namespace('genres')
models_scheme = GenreScheme(many=True)
model_schemes = GenreScheme()

@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        models = service.get_all()
        return models_scheme.dump(models), 200


@genre_ns.route('/<int:id>')
class GenreView(Resource):
    def get(self, id: int):
        try:
            model = service.get_one(id)
            return model_schemes.dump(model), 200
        except Exception as e:
            return str(e), 404
