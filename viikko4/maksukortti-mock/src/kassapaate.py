HINTA = 5


class Kassapaate:
    def __init__(self):
        self.myytyja_lounaita = 0

    def lataa(self, kortti, summa):
        kortti.lataa(summa)

    def osta_lounas(self, kortti):
        kortti.osta(HINTA)
        self.myytyja_lounaita = self.myytyja_lounaita + 1
