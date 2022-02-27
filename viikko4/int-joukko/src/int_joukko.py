KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko
        self.ljono = [None] * self.kapasiteetti
        self.alkioiden_lkm = 0

    def kuuluu(self, n):
        return n in self.ljono

    def lisaa(self, lisattava):

        if lisattava in self.ljono:
            return False

        if self.alkioiden_lkm == self.kapasiteetti:
            self.kapasiteetti += self.kasvatuskoko
            self.ljono = self.ljono + ([0] * self.kasvatuskoko)

        self.ljono[self.alkioiden_lkm] = lisattava
        self.alkioiden_lkm += 1
        return True

    def poista(self, poistettava):
        if not self.kuuluu(poistettava):
            return False

        for i in range(self.ljono.index(poistettava), self.alkioiden_lkm-1):
            self.ljono[i] = self.ljono[i+1]

        self.ljono[self.alkioiden_lkm-1] = None
        self.alkioiden_lkm -= 1

        return True

    def kopioi_taulukko(self, a, b):
        b = a[:]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        return list(filter(lambda x: x != None, self.ljono))

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in (a_taulu+b_taulu):
            x.lisaa(i)

        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in (b_taulu):
            if i in a_taulu:
                y.lisaa(i)

        return y

    @staticmethod
    def erotus(a, b):
        d = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in (a_taulu):
            if i not in b_taulu:
                d.lisaa(i)

        return d

    def __str__(self):
        return "{"+f'{", ".join(map(lambda x: str(x), self.to_int_list()))}'+"}"
