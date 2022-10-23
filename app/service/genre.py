from app.service_container import GenreDAO
from app.dao.models.genre import Genre


class GenreService:
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_one(self, uid: int) -> Genre:
        return self.dao.get_one(uid)

    def get_all(self) -> list[Genre]:
        return self.dao.get_all()
