from tuote import Tuote
from ostos import Ostos


class Ostoskori:
    def __init__(self):
        self._ostokset = []
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def _ostos_tuotteelle(self, tuote: Tuote):
        return next(
            filter(
                lambda ostos: ostos.tuotteen_nimi() == tuote.nimi(),
                self._ostokset
            ),
            None
        )

    def tavaroita_korissa(self):
        return sum(
            map(
                lambda ostos: ostos.lukumaara(),
                self._ostokset
            )
        )
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2

    def hinta(self):
        return sum(
            map(lambda ostos: ostos.hinta(), self._ostokset)
        )
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

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
        ostos.muuta_lukumaaraa(-1)

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        return self._ostokset
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
