import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

VIITE = 42


class TestKauppa(unittest.TestCase):
    def setUp(self):
        # luodaan mock-oliot
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()
        self.varasto_mock = Mock()

        # viitegeneraattori palauttaa aina viitteen 42
        self.viitegeneraattori_mock.uusi.return_value = VIITE

        # luodaan mock-varastoon saldo ja hae_tuote -metodit
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id == 2:
                return 5
            if tuote_id == 3:
                return 0

        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(2, "leipä", 2)
            if tuote_id == 3:
                return Tuote(3, "kala", 8)

        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # luodaan näillä kauppa-mocki
        self.kauppa = Kauppa(
            self.varasto_mock,
            self.pankki_mock,
            self.viitegeneraattori_mock
        )

    def test_ostoksen_paatyttya_pankin_metodia_tilisiirto_kutsutaan(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_ostoksen_paatyttya_pankin_metodia_tilisiirto_kutsutaan_oikeilla_arvoilla(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka",
            VIITE,
            "12345",
            ANY,
            5
        )

    def test_kahden_eri_ostoksen_oston_paatyttya_pankin_metodia_tilisiirto_kutsutaan_oikeilla_arvoilla(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("kalle", "6789")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called_with(
            "kalle",
            VIITE,
            "6789",
            ANY,
            7
        )

    def test_kahden_saman_ostoksen_oston_paatyttya_pankin_metodia_tilisiirto_kutsutaan_oikeilla_arvoilla(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("kaarle", "0835")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called_with(
            "kaarle",
            VIITE,
            "0835",
            ANY,
            10
        )

    def test_yhden_ostoksen_ja_yhden_loppuneen_oston_paatyttya_pankin_metodia_tilisiirto_kutsutaan_oikeilla_arvoilla(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        # kala on varastosta loppu
        self.kauppa.lisaa_koriin(3)
        self.kauppa.tilimaksu("dorian", "8456")

        # varmistetaan, että metodia tilisiirto on kutsuttu ja lopussa ollutta tuotetta ei veloitettu
        self.pankki_mock.tilisiirto.assert_called_with(
            "dorian",
            VIITE,
            "8456",
            ANY,
            5
        )

    def test_aloita_asiointi_nollaa_edelliset_ostokset(self):
        # tehdään ensimmäiset ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)

        # aloitetaan uusi asiointi
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("fabian", "5943")

        # varmistetaan, että metodia tilisiirto on kutsuttu vain uuden asioinnin ostosten hinnalla
        self.pankki_mock.tilisiirto.assert_called_with(
            "fabian",
            VIITE,
            "5943",
            ANY,
            5
        )

    def test_tilimaksu_pyytaa_uuden_viitenumeron_joka_kerta(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.tilimaksu("kaarle", "4354")

        self.kauppa.aloita_asiointi()
        self.kauppa.tilimaksu("fabian", "5943")

        self.kauppa.aloita_asiointi()
        self.kauppa.tilimaksu("dorian", "8456")

        self.assertEqual(self.viitegeneraattori_mock.uusi.call_count, 3)

    def test_poista_korista_ei_veloita_tuotetta(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.poista_korista(1)
        self.kauppa.tilimaksu("karlos", "3423")

        self.pankki_mock.tilisiirto.assert_called_with(
            "karlos",
            VIITE,
            "3423",
            ANY,
            0
        )

    def test_poista_korista_palauttaa_varastoon(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.poista_korista(1)

        self.varasto_mock.palauta_varastoon.assert_called_once()
