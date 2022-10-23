from flask_restx import Resource, Namespace
from app.service_container import director_service as service
from app.dao.models.director import DirectorScheme

directors_ns = Namespace('directors')
models_scheme = DirectorScheme(many=True)
model_schemes = DirectorScheme()

@directors_ns.route('/')
class DirectorView(Resource):
    def get(self):
        models = service.get_all()
        return models_scheme.dump(models), 200

@directors_ns.route('/<int:id>')
class DirectorView(Resource):
    def get(self, id: int):
        try:
            model = service.get_one(id)
            return model_schemes.dump(model), 200
        except Exception as e:
            return str(e), 404