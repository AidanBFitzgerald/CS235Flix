class Actor:
    def __init__(self, actor_full_name: str):
        if actor_full_name == "" or type(actor_full_name) is not str:
            self.__actor_full_name = None
        else:
            self.__actor_full_name = actor_full_name.strip()
        self.__colleagues = []

    @property
    def actor_full_name(self) -> str:
        return self.__actor_full_name

    def __repr__(self):
        return f"<Actor {self.actor_full_name}>"

    def __eq__(self, other):
        if not isinstance(other, Actor):
            return False
        return self.actor_full_name == other.actor_full_name

    def __lt__(self, other):
        if not isinstance(other, Actor):
            return False
        return self.actor_full_name < other.actor_full_name

    def __hash__(self):
        return hash(self.actor_full_name)

    def add_actor_colleague(self, colleague):
        if colleague not in self.__colleagues and isinstance(colleague, Actor):
            self.__colleagues.append(colleague)

    def check_if_this_actor_worked_with(self,colleague):
        if colleague in self.__colleagues:
            return True
        return False

class TestActorMethods:
    def test_colleague(self):
        actor1 = Actor("Dave")
        actor2 = Actor("Sam")
        actor1.add_actor_colleague(actor2)
        assert actor1.check_if_this_actor_worked_with(actor2)