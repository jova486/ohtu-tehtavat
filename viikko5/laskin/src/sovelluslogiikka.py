class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.edellinen = []
        self.tulos = tulos

    def miinus(self, arvo):
        self.edellinen.append(self.tulos)
        self.tulos = self.tulos - arvo

    def plus(self, arvo):
        self.edellinen.append(self.tulos)
        self.tulos = self.tulos + arvo

    def nollaa(self):
        self.edellinen.append(self.tulos)
        self.tulos = 0

    def aseta_arvo(self, arvo):
        self.edellinen.append(self.tulos)
        self.tulos = arvo

    def kumoa(self):
        if len(self.edellinen) != 0:
            self.tulos = self.edellinen[-1]
            self.edellinen.pop()
        else: self.tulos = 0
