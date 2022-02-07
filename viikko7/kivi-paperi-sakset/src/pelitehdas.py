from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly


class Pelitehdas:
  @staticmethod
  def luo_pvp_peli():
        return KPSPelaajaVsPelaaja()

  @staticmethod
  def luo_tekoaly_peli():
      return KPSTekoaly()

  @staticmethod
  def luo_parempi_tekoaly_peli():
      return KPSParempiTekoaly()