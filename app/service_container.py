# Тут создаем DAO и сервисы, чтобы импортировать их например во вьюшках
from app.database import db
from app.dao.movie_dao import MovieDAO
from app.dao.genre_dao import GenreDAO
from app.dao.director_dao import DirectorDAO

from app.service.movie import MovieService
from app.service.genre import GenreService
from app.service.director import DirectorService

movie_dao = MovieDAO(db.session)
movie_service = MovieService(dao=movie_dao)

genre_dao = GenreDAO(db.session)
genre_service = GenreService(dao=genre_dao)

director_dao = DirectorDAO(db.session)
director_service = DirectorService(dao=director_dao)