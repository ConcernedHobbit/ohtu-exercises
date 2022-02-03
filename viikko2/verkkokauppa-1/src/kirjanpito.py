class Kirjanpito:
    __instanssi = None

    @staticmethod
    def get_instance():
        if not Kirjanpito.__instanssi:
            Kirjanpito.__instanssi = Kirjanpito()

        return Kirjanpito.__instanssi

    def __init__(self):
        self.tapahtumat = []

    def lisaa_tapahtuma(self, tapahtuma):
        self.tapahtumat.append(tapahtuma)
