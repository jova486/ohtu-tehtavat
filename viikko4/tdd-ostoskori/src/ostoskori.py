from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.__ostokset = []
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        maara = 0
        for ostos in self.__ostokset:
            maara += ostos.lukumaara()

        return maara
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2

    def hinta(self):
        hinta = 0
        for ostos in self.__ostokset:
            hinta += ostos.tuote.hinta()*ostos.lukumaara()

        return hinta
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        for ostos in self.__ostokset:
            if ostos.tuote.nimi() == lisattava.nimi():
                ostos.muuta_lukumaaraa(1)
                return
        self.__ostokset.append(Ostos(lisattava))

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        pass

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        return self.__ostokset
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
