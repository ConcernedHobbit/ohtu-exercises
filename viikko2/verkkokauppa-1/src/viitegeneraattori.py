class Viitegeneraattori:
    __instanssi = None

    @staticmethod
    def get_instance():
        if not Viitegeneraattori.__instanssi:
            Viitegeneraattori.__instanssi = Viitegeneraattori()

        return Viitegeneraattori.__instanssi

    def __init__(self):
        self._seuraava = 1

    def uusi(self):
        self._seuraava = self._seuraava + 1

        return self._seuraava
