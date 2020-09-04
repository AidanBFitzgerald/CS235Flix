from domainmodel.movie import Movie
import pytest


class WatchingQueue:
    def __init__(self):
        self.__movie_queue = []

    def add_to_queue(self, movie: Movie):
        if isinstance(movie, Movie) and movie not in self.__movie_queue:
            self.__movie_queue.append(movie)

    def remove_from_queue(self, movie: Movie):
        if isinstance(movie, Movie) and movie in self.__movie_queue:
            self.__movie_queue.remove(movie)

    def watch_next(self) -> Movie:
        if len(self.__movie_queue) > 0:
            return self.__movie_queue.pop(0)

    def size(self):
        return len(self.__movie_queue)

    def next_in_queue(self):
        if len(self.__movie_queue) > 0:
            return self.__movie_queue[0]


class TestWatchingQueueMethods:
    @pytest.fixture
    def watching_queue(self):
        watching_queue = WatchingQueue()
        watching_queue.add_to_queue(Movie("Star Wars", 2018))
        watching_queue.add_to_queue(Movie("Ice Age", 2002))
        watching_queue.add_to_queue((Movie("Frozen", 2013)))
        return watching_queue

    def test_init(self):
        watching_queue = WatchingQueue()
        assert watching_queue.size() == 0
        assert watching_queue.remove_from_queue(Movie("Test", 2000)) is None
        assert watching_queue.watch_next() is None
        assert watching_queue.next_in_queue() is None

    def test_queued(self, watching_queue):
        assert watching_queue.size() == 3
        watching_queue.remove_from_queue(Movie("Ice Age", 2002))
        assert watching_queue.size() == 2
        assert watching_queue.watch_next() == Movie("Star Wars", 2018)
        assert watching_queue.size() == 1
        assert watching_queue.next_in_queue() == Movie("Frozen", 2013)
        watching_queue.watch_next()
        assert watching_queue.size() == 0