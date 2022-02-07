from pelitehdas import Pelitehdas
from kps import KPS


def aloita_peli(peli: KPS):
    print(
        "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
    )
    peli.pelaa()

def main():
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()

        if vastaus.endswith("a"):
            aloita_peli(Pelitehdas.luo_pvp_peli())
        elif vastaus.endswith("b"):
            aloita_peli(Pelitehdas.luo_tekoaly_peli())
        elif vastaus.endswith("c"):
            aloita_peli(Pelitehdas.luo_parempi_tekoaly_peli())
        else:
            print("Hei hei!")
            break


if __name__ == "__main__":
    main()
