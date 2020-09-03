from datetime import datetime

from domainmodel.movie import Movie


class Review:
    def __init__(self, movie: Movie, review_text: str, rating: int):
        self.__movie = movie
        self.__review_text = review_text
        self.__rating = None
        if 1 <= rating <= 10:
            self.__rating = rating
        self.__time = datetime.today()

    @property
    def movie(self) -> Movie:
        return self.__movie

    @property
    def review_text(self) -> str:
        return self.__review_text

    @property
    def rating(self) -> int:
        return self.__rating

    @property
    def timestamp(self) -> datetime:
        return self.__time

    def __repr__(self):
        return f"<Review {self.__movie.title}, {self.__time}>"

    def __eq__(self, other):
        if not isinstance(other, Review):
            return False
        return self.__movie == other.movie and self.__review_text == other.__review_text and \
               self.__rating == other.rating and self.__time == other.timestamp
