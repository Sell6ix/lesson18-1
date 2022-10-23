from app.service_container import DirectorDAO
from app.dao.models.director import Director


class DirectorService:
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_one(self, uid: int) -> Director:
        return self.dao.get_one(uid)

    def get_all(self) -> list[Director]:
        return self.dao.get_all()
