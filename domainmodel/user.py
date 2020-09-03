from domainmodel.movie import Movie
from domainmodel.review import Review
import pytest


class User:
    def __init__(self, username: str, password: str):
        if username == "" or type(username) is not str:
            self.__username = None
        else:
            self.__username = username.lower().strip()
        if password == "" or type(password) is not str:
            self.__password = None
        else:
            self.__password = password

        self.__watched_movies = []
        self.__reviews = []
        self.__time_spent_watching_movies = 0

    @property
    def user_name(self) -> str:
        return self.__username

    @property
    def password(self) -> str:
        return self.__password

    @property
    def watched_movies(self) -> list:
        return self.__watched_movies

    @property
    def reviews(self) -> list:
        return self.__reviews

    @property
    def time_spent_watching_movies_minutes(self) -> int:
        return self.__time_spent_watching_movies

    def __repr__(self):
        return f"<User {self.__username}>"

    def __eq__(self, other):
        if not isinstance(other, User):
            return False
        return self.__username == other.user_name

    def __lt__(self, other):
        if not isinstance(other, User):
            return False
        return self.__username < other.user_name

    def __hash__(self):
        return hash(self.__username)

    def watch_movie(self, movie: Movie):
        if isinstance(movie, Movie):
            if movie not in self.__watched_movies:
                self.__watched_movies.append(movie)
            runtime = movie.runtime_minutes
            if runtime is None:
                runtime = 0
            self.__time_spent_watching_movies += runtime

    def add_review(self, review: Review):
        if isinstance(review, Review):
            self.__reviews.append(review)


user1 = User("Dave", "sam")
user1.watch_movie(Movie("Split", 2017))
print(user1.watched_movies)
print(user1.time_spent_watching_movies_minutes)


class TestUserMethods:
    @pytest.fixture
    def user(self):
        return User("Dave", "Qwasd")

    def test_init(self, user):
        assert repr(user) == "<User dave>"
        assert user.user_name == "dave"
        assert user.password == "Qwasd"
        assert user.watched_movies == []
        assert user.reviews == []
        assert user.time_spent_watching_movies_minutes == 0

    def test_watch_movie(self, user):
        movie = Movie("Wow", 1999)
        movie.runtime_minutes = 100
        user.watch_movie(movie)
        assert user.watched_movies == [Movie("Wow", 1999)]
        assert user.time_spent_watching_movies_minutes == 100

    def test_comparisons(self, user):
        user1 = User("Dave", "dasd")
        assert user == user1
        user2 = User("Sam", "Qwasd")
        assert user != user2
        assert user < user2
        assert hash(user) == hash("dave")
