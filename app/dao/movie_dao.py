from app.dao.models.movie import Movie

class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, uid) -> Movie:
        return self.session.query(Movie).get(uid)

    def get_all(self, director_id: int = None, genre_id : int = None, year: int = None) -> list[Movie]:
        data = self.session.query(Movie)

        if director_id is not None:
            data = data.filter(Movie.director_id == director_id)

        if genre_id is not None:
            data = data.filter(Movie.genre_id == genre_id)

        if year is not None:
            data = data.filter(Movie.year == year)

        return data.all()

    def create(self, data) -> Movie:
        model = Movie(**data)
        self.session.add(model)
        self.session.commit()
        return model

    def update(self, data, uid) -> None:
        self.session.query(Movie).filter(Movie.id == uid).update(data)
        self.session.commit()

    def delete(self, uid: int) -> None:
        model = self.get_one(uid)
        self.session.delete(model)
        self.session.commit()

    def update_particular(self, data: dict[str, str], uid: int) -> None:
        model = self.get_one(uid)

        if 'name' in data:
            model.name = data.get('name')

        if 'description' in data:
            model.description = data.get('description')

        if 'trailer' in data:
            model.trailer = data.get('trailer')

        if 'year' in data:
            model.year = data.get('year')

        if 'rating' in data:
            model.rating = data.get('rating')

        if 'genre_id' in data:
            model.genre_id = data.get('genre_id')

        if 'director_id' in data:
            model.director_id = data.get('director_id')

        self.session.add(model)
        self.session.commit()