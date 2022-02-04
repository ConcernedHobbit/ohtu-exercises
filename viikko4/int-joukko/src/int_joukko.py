from __future__ import annotations
from typing import List, Optional


class IntJoukko:
    def __init__(self, kapasiteetti: int = 5, kasvatuskoko: int = 5):
        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko

        self.luvut = [0] * self.kapasiteetti
        self.pituus = 0

    def kuuluu(self, luku: int) -> bool:
        for i in range(0, self.pituus):
            if luku == self.luvut[i]:
                return True

        return False

    def lisaa(self, luku: int) -> bool:
        if self.pituus == 0:
            self.luvut[0] = luku
            self.pituus += 1
            return True

        if self.kuuluu(luku):
            return False

        self.luvut[self.pituus] = luku
        self.pituus += 1

        if self.pituus == len(self.luvut):
            self._kasvata()

        return True

    def lisaa_lista(self, lista: List[int]) -> None:
        for luku in lista:
            self.lisaa(luku)

    def indeksi(self, luku: int) -> Optional[int]:
        for i in range(0, self.pituus):
            if luku == self.luvut[i]:
                return i
        return None

    def poista(self, luku: int) -> bool:
        kohta = self.indeksi(luku)

        if kohta is None:
            return False

        for i in range(kohta, self.pituus):
            self.luvut[i] = self.luvut[i + 1]

        self.pituus = self.pituus - 1
        return True

    def mahtavuus(self) -> int:
        return self.pituus

    def _kasvata(self) -> None:
        vanha_jono = self.luvut[:]

        self.luvut = [0] * (self.pituus + self.kasvatuskoko)

        for indeksi, luku in enumerate(vanha_jono):
            self.luvut[indeksi] = luku

    # tehtävä ei määritä voiko metodeja uudelleennimetä,
    # oletan että tätä "käytetään" jossain muussakin
    # kuin testeissä ja indeksissä. muuten uusi nimi olisi
    # esim. listana(self)
    def to_int_list(self) -> List[int]:
        return self.luvut[:self.pituus]

    @staticmethod
    def yhdiste(a: IntJoukko, b: IntJoukko) -> IntJoukko:
        yhdiste_joukko = IntJoukko()
        yhdiste_joukko.lisaa_lista(a.to_int_list())
        yhdiste_joukko.lisaa_lista(b.to_int_list())

        return yhdiste_joukko

    @staticmethod
    def leikkaus(a: IntJoukko, b: IntJoukko) -> IntJoukko:
        leikkaus_joukko = IntJoukko()

        for luku in a.to_int_list():
            if b.kuuluu(luku):
                leikkaus_joukko.lisaa(luku)

        return leikkaus_joukko

    @staticmethod
    def erotus(a: IntJoukko, b: IntJoukko) -> IntJoukko:
        erotus_jouko = IntJoukko()

        for luku in a.to_int_list():
            if not b.kuuluu(luku):
                erotus_jouko.lisaa(luku)

        return erotus_jouko

    def __str__(self):
        lista = self.to_int_list()
        merkkijonoina = list(map(str, lista))
        return '{' + ', '.join(merkkijonoina) + '}'
