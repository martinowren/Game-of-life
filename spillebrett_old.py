import random
from celle import Celle

class Spillebrett:
    def __init__(self, rader, kolonner):
        self.rader = rader
        self.kolonner = kolonner
        self.generasjon = 0
        self.naboListen = []
        self.brett = [["." for _ in range(self.kolonner)] for _ in range(self.rader)] #LAGER BRETT
        self.celler = []
        self.maxbrikker = (self.kolonner * self.rader)

        for i in range(self.kolonner):
            for j in range(self.rader):
                for e in range(self.maxbrikker):
                    self.celler.append(Celle(e, "død"))


    def finnNabo(self, x, y):
        self.naboListen = []
        naboListen.append("a")
        naboListen.append(self.brett[x-1][y-1])
        retun self.naboListen

        #self.brett[0][0] = "o" #POSISJON SOM ER LEVENDE

    def tegnBrett(self):
        print("\n".join("".join(row) for row in self.brett)) #PRINTER BRETTET
        #print(Celle(0).signOfLife())
    def oppdatering(self):
        self.generasjon += 1

    def generer(self): # Generer første sett med celler
        for i in range(len(self.brett)):
            for j in range(len(self.brett[i])):
                for e in range(self.maxbrikker):
                    if random.randint(0,2) == 1:
                        self.brett[i][j] = Celle(e, "levende").signOfLife()
                    else:
                        self.brett[i][j] = Celle(e, "død").signOfLife()
                    #self.brett[i][j] = Celle(e).signOfLife()
                    #self.brett[i][j] = "O"
