class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulokset = [tulos]

    @property
    def tulos(self):
        return self.tulokset[len(self.tulokset) - 1]

    @property
    def askeleet(self):
        return len(self.tulokset)

    @property
    def voi_kumota(self):
        return self.askeleet > 1

    def aseta_arvo(self, tulos):
        self.tulokset.append(tulos)

    def miinus(self, arvo):
        self.aseta_arvo(self.tulos - arvo)

    def plus(self, arvo):
        self.aseta_arvo(self.tulos + arvo)

    def nollaa(self):
        self.aseta_arvo(0)

    def kumoa(self):
        self.tulokset.pop()
