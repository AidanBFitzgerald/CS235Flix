
class Genre:
    def __init__(self, genre_name: str):
        if genre_name == "" or type(genre_name) is not str:
            self.__genre_name = None
        else:
            self.__genre_name = genre_name.strip()

    @property
    def genre_name(self) -> str:
        return self.__genre_name

    def __repr__(self):
        return f"<Genre {self.__genre_name}>"

    def __eq__(self,other):
        if not isinstance(other,Genre):
            return False
        return self.genre_name == other.genre_name

    def __lt__(self, other):
        if not isinstance(other,Genre):
            return False
        return self.genre_name < other.genre_name

    def __hash__(self):
        return hash(self.genre_name)

class TestGenreMethods:

    def test_init(self):
        genre1 = Genre("Comedy")
        assert repr(genre1) == "<Genre Comedy>"
