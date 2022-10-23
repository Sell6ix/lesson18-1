from app.service_container import MovieDAO
from app.dao.models.movie import Movie


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def create(self, data) -> Movie:
        return self.dao.create(data)

    def get_one(self, uid: int) -> Movie:
        return self.dao.get_one(uid)

    def get_all(self, director_id:int=None, genre_id:int=None, year:int=None) -> list[Movie]:
        return self.dao.get_all(director_id=director_id, genre_id=genre_id, year=year)

    def update(self, data: dict[str, str], uid: int) -> None:
        self.dao.update(data, uid)

    def update_particular(self, data: dict[str, str], uid: int) -> None:
        self.dao.update_particular(data, uid)

    def delete(self, uid: int):
        self.dao.delete(uid)