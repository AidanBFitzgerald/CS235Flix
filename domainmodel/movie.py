from domainmodel.genre import Genre
from domainmodel.actor import Actor
from domainmodel.director import Director
import pytest


class Movie:
    def __init__(self, title: str, year: int):
        self.__description = None
        self.__director = None
        self.__actors = []
        self.__genres = []
        self.__runtime_minutes = None

        if year >= 1900:
            self.__year = year
        else:
            self.__year = None
        if title == "" or type(title) is not str:
            self.__title = None
        else:
            self.__title = title.strip()

    @property
    def title(self) -> str:
        return self.__title

    @property
    def description(self) -> str:
        return self.__description

    @property
    def director(self) -> Director:
        return self.__director

    @property
    def actors(self) -> list:
        return self.__actors

    @property
    def genres(self) -> list:
        return self.__genres

    @property
    def runtime_minutes(self) -> int:
        return self.__runtime_minutes

    @title.setter
    def title(self, new_title: str):
        if new_title == "" or type(new_title) is not str:
            self.__title = None
        else:
            self.__title = new_title.strip()

    @description.setter
    def description(self, new_description: str):
        if new_description == "" or type(new_description) is not str:
            self.__description = None
        else:
            self.__description = new_description.strip()

    @director.setter
    def director(self, new_director: Director):
        if isinstance(new_director, Director):
            self.__director = new_director

    @actors.setter
    def actors(self, new_actors: list):
        if type(new_actors) is list:
            self.__actors = new_actors

    @genres.setter
    def genres(self, new_genres):
        if type(new_genres) is list:
            self.__genres = new_genres

    @runtime_minutes.setter
    def runtime_minutes(self, new_runtime: int):
        if type(new_runtime) is int:
            if new_runtime <= 0:
                raise ValueError
            self.__runtime_minutes = new_runtime

    def __repr__(self):
        return f"<Movie {self.__title}, {self.__year}>"

    def __eq__(self, other):
        if not isinstance(other, Movie):
            return False
        return self.__title == other.__title and self.__year == other.__year

    def __lt__(self, other):
        if isinstance(other,Movie):
            if self.__title == other.title:
                return self.__year < other.__year
            else:
                return self.__title < other.title
        return False

    def __hash__(self):
        return hash((self.__title, self.__year))

    def add_actor(self, actor: Actor):
        if isinstance(actor, Actor) and actor not in self.__actors:
            self.__actors.append(actor)

    def remove_actor(self, actor):
        try:
            self.__actors.remove(actor)

        except ValueError:
            return

    def add_genre(self, genre):
        if isinstance(genre, Genre) and genre not in self.__genres:
            self.__genres.append(genre)

    def remove_genre(self, genre):
        try:
            self.__genres.remove(genre)

        except ValueError:
            return

class TestMovieMethods:
    @pytest.fixture
    def movie(self):
        movie = Movie("Lady Bug and Bee",2017)
        movie.runtime_minutes = 100
        movie.director = Director("Dave")
        movie.add_actor(Actor("Sam"))
        movie.add_actor(Actor("Cherry"))
        movie.add_genre(Genre("Kids"))
        return movie

    def test_init(self,movie):
        assert repr(movie) == "<Movie Lady Bug and Bee, 2017>"

    def test_set_people(self,movie):
        assert movie.actors == [Actor("Sam"), Actor("Cherry")]
        assert movie.director == Director("Dave")
        assert movie.runtime_minutes == 100
        movie.runtime_minutes = "pam"
        assert movie.runtime_minutes == 100
        assert movie.genres == [Genre("Kids")]
        movie1 = Movie("Same", 120)
        assert repr(movie1) == "<Movie Same, None>"

    def test_remove_people(self,movie):
        movie.remove_actor(Actor("Sam"))
        assert movie.actors == [Actor("Cherry")]
        movie.remove_genre(Genre("Kids"))
        assert movie.genres == []
        movie.remove_genre(Genre("Comedy"))
        assert movie.genres == []
        movie.remove_actor(Actor("Paul"))
        assert movie.actors == [Actor("Cherry")]

    def test_compare(self, movie):
        movie1 = Movie("Am", 2017)
        assert movie1 < movie
        assert not movie == movie1
        movie2 = Movie("Am", 2017)
        assert movie1 == movie2
        assert not movie1 < movie2
        movie3 = Movie("Am", 2000)
        assert movie3 < movie2
        assert not movie3 == movie2

