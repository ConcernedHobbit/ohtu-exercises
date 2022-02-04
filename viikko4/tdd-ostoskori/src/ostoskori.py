from tuote import Tuote
from ostos import Ostos


class Ostoskori:
    def __init__(self):
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote
        self._ostokset = []

    def _ostos_tuotteelle(self, tuote: Tuote):
        return next(
            filter(
                lambda ostos: ostos.tuotteen_nimi() == tuote.nimi(),
                self._ostokset
            ),
            None
        )

    def tavaroita_korissa(self):
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2
        return sum(
            map(
                lambda ostos: ostos.lukumaara(),
                self._ostokset
            )
        )

    def hinta(self):
        # kertoo korissa olevien ostosten yhteenlasketun hinnan
        return sum(
            map(lambda ostos: ostos.hinta(), self._ostokset)
        )

    def lisaa_tuote(self, lisattava: Tuote):
        # lisää tuotteen
        ostos = self._ostos_tuotteelle(lisattava)

        if ostos:
            ostos.muuta_lukumaaraa(1)
        else:
            self._ostokset.append(
                Ostos(lisattava)
            )

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        ostos = self._ostos_tuotteelle(poistettava)
        if ostos.lukumaara() > 1:
            ostos.muuta_lukumaaraa(-1)
        else:
            self.tyhjenna()

    def tyhjenna(self):
        # tyhjentää ostoskorin
        self._ostokset.clear()

    def ostokset(self):
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
        return self._ostokset
