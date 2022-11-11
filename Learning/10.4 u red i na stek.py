# pretstavlja listu elemenata sa minimalnom logikom
class Kontener:

    def __init__(self):
        self._niz = []

    def __str__(self):
        txt = [str(x) for x in self._niz]
        return ','.join(txt)

    def je_prazan(self):
        return len(self._niz) == 0

    def koliko(self):
        return len(self._niz)

    def izbaci(self):
        if self.je_prezan:
            return None
        else:
            return self._niz.pop()

# predstavlja Fifo strukturu (prvi unutra, prvi napolje)
class Red(Kontejner):
    def __init__(self):
        super().__init__()

    def ubaci(self, el):
        self._niz.insert(0, el)
        return self # omogućava ulančavanje za ubaci

# predstavlja Lifo strukturu (poslednji unutra, prvi napolje)
class Stek(Kontejner):
    def __init__(self):
        super().__init__()

    def ubaci(self, el):
        self._niz.append(el)
        return self # omogućava ulančavanje za ubaci
