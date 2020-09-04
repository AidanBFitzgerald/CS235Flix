from domainmodel.movie import Movie
from domainmodel.user import User
import pytest

class WatchingSession:
    def __init__(self, host: User, movie: Movie):
        if isinstance(host, User):
            self.__host = host
        else:
            self.__host = None
        self.__friends = []
        if isinstance(movie, Movie):
            self.__watching = movie
        else:
            self.__watching = None

    def add_friend(self, host: User, friend: User):
        if host == self.__host and host is not None:
            if isinstance(friend, User) and friend != self.__host:
                self.__friends.append(friend)

    def kick_user(self, host: User, friend: User):
        if host == self.__host and host is not None:
            if friend in self.__friends:
                self.__friends.remove(friend)

    def change_host(self, old_host: User, new_host: User):
        if old_host == self.__host and isinstance(new_host, User):
            self.__host = new_host
            if self.__host in self.__friends:
                self.__friends.remove(self.__host)

    def change_movie(self, host: User, movie: Movie):
        if host == self.__host and host is not None and isinstance(movie, Movie):
            self.__watching = movie

    def end_session(self, host: User):
        if host == self.__host:
            self.__friends = []
            self.__watching = None

    def users_in_session(self):
        return [self.__host] + self.__friends

    def size(self):
        if self.__host is None:
            return len(self.__friends)
        return len(self.__friends) + 1

    @property
    def watching(self):
        return self.__watching

    @property
    def host(self):
        return self.__host


class TestWatchingSessionMethods:
    @pytest.fixture
    def watching_session(self):
        return WatchingSession(User("Aidan", "Wasx"), Movie("Cars", 2008))

    def test_init(self, watching_session):
        assert watching_session.size() == 1
        assert watching_session.watching == Movie("Cars", 2008)
        assert watching_session.host == User("Aidan", "Wasx")
        assert watching_session.users_in_session() == [User("Aidan", "Wasx")]

    def test_add_friend(self, watching_session):
        watching_session.add_friend(User("Aidan", "Wasx"), User("Iona", "Mort"))
        assert watching_session.size() == 2
        assert watching_session.users_in_session() == [User("Aidan", "Wasx"), User("Iona", "Mort")]
        watching_session.add_friend(User("Sam", "Waz"), User("Sam", "Waz"))
        assert watching_session.size() == 2
        watching_session.add_friend(User("Aidan", "Wasx"), User("Aidan", "Wasx"))
        assert  watching_session.size() == 2

    def test_kick_user(self, watching_session):
        user1 = User("Aidan", "Wasx")
        user2 = User("Iona", "Mort")
        watching_session.add_friend(user1, user2)
        assert watching_session.size() == 2
        watching_session.kick_user(user2, user2)
        assert watching_session.size() == 2
        watching_session.kick_user(user1, User("Dave", "Brown"))
        assert watching_session.size() == 2
        watching_session.kick_user(user1, user2)
        assert watching_session.size() == 1

    def test_change_host(self, watching_session):
        user1 = User("Aidan", "Wasx")
        user2 = User("Iona", "Mort")
        watching_session.change_host(user2, user2)
        assert watching_session.host == user1
        watching_session.add_friend(user1,user2)
        assert watching_session.size() == 2
        watching_session.change_host(user1, user2)
        assert watching_session.host == user2
        assert watching_session.size() == 1
        assert watching_session.users_in_session() == [user2]

    def test_change_movie(self, watching_session):
        user1 = User("Aidan", "Wasx")
        user2 = User("Iona", "Mort")
        watching_session.change_movie(user2, Movie("Lion King", 2019))
        assert watching_session.watching == Movie("Cars", 2008)
        watching_session.change_movie(user1, Movie("Lion King", 2019))
        assert watching_session.watching == Movie("Lion King", 2019)

    def test_end_session(self, watching_session):
        user1 = User("Aidan", "Wasx")
        user2 = User("Iona", "Mort")
        watching_session.add_friend(user1, user2)
        watching_session.end_session(user2)
        assert watching_session.size() == 2
        assert watching_session.watching == Movie("Cars", 2008)
        watching_session.end_session(user1)
        assert watching_session.size() == 1
        assert watching_session.users_in_session() == [user1]
        assert watching_session.watching is None
