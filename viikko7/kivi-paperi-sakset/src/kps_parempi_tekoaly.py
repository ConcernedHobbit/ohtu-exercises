from kps import KPS
from tekoaly_parannettu import TekoalyParannettu


class KPSParempiTekoaly(KPS):
    def __init__(self):
        self.tekoaly_parannettu = TekoalyParannettu()

    def _toisen_siirto(self, ensimmaisen_siirto):
        return self.tekoaly_parannettu.anna_siirto(ensimmaisen_siirto)