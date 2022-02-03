from kirjanpito import Kirjanpito


class Pankki:
    __instanssi = None

    @staticmethod
    def get_instance():
        if not Pankki.__instanssi:
            Pankki.__instanssi = Pankki()

        return Pankki.__instanssi

    def __init__(self):
        self._kirjanpito = Kirjanpito.get_instance()

    def tilisiirto(self, nimi, viitenumero, tililta, tilille, summa):
        self._kirjanpito.lisaa_tapahtuma(
            f"tilisiirto: tililtä {tililta} tilille {tilille} viite {viitenumero} summa {summa}e"
        )

        # täällä olisi koodi joka ottaa yhteyden pankin verkkorajapintaan
        return True
