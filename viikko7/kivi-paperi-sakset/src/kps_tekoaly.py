from kps import KPS
from tekoaly import Tekoaly


class KPSTekoaly(KPS):
    def __init__(self):
        self.tekoaly = Tekoaly()

    def _toisen_siirto(self, ensimmaisen_siirto):
        return self.tekoaly.anna_siirto(ensimmaisen_siirto)