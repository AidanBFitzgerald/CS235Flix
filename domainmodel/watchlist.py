from domainmodel.movie import Movie
import pytest


class WatchList:
    def __init__(self):
        self.__watchlist = []
        self.__iter_index = 0

    def add_movie(self, movie: Movie):
        if isinstance(movie, Movie) and movie not in self.__watchlist:
            self.__watchlist.append(movie)

    def remove_movie(self, movie: Movie):
        if movie in self.__watchlist:
            self.__watchlist.remove(movie)

    def select_movie_to_watch(self, index: int):
        if 0 <= index < len(self.__watchlist):
            return self.__watchlist[index]

    def size(self):
        return len(self.__watchlist)

    def first_movie_in_watchlist(self):
        if len(self.__watchlist) > 0:
            return self.__watchlist[0]

    def __iter__(self):
        return self

    def __next__(self):
        if self.__iter_index < len(self.__watchlist):
            ret_val = self.__watchlist[self.__iter_index]
            self.__iter_index += 1
            return ret_val
        else:
            raise StopIteration


class TestWatchListMethods:
    @pytest.fixture
    def watchlist(self):
        watchlist = WatchList()
        watchlist.add_movie(Movie("Movie1", 2001))
        watchlist.add_movie(Movie("Movie2", 2019))
        return watchlist

    def test_init(self):
        watchlist_empty = WatchList()
        assert watchlist_empty.size() == 0
        assert watchlist_empty.first_movie_in_watchlist() is None
        watchlist_empty.remove_movie(Movie("Mummy", 2018))
        assert watchlist_empty.size() == 0

    def test_iter(self, watchlist):
        for i in watchlist:
            assert isinstance(i, Movie)

    def test_remove(self, watchlist):
        assert watchlist.size() == 2
        watchlist.remove_movie(Movie("Movie1", 2001))
        assert watchlist.size() == 1
        assert watchlist.first_movie_in_watchlist() == Movie("Movie2", 2019)
        watchlist.remove_movie(Movie("Movie2", 2019))
        assert watchlist.first_movie_in_watchlist() is None
