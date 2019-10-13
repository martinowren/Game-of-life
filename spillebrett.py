import random
from celle import Celle

class Spillebrett:
    def __init__(self, rader, kolonner):
        self.generasjon = 1

        self.rader = rader
        self.kolonner = kolonner
        self.brett = []

        for rad in range(self.rader): # Lager brettet med x celler i brettet
            midlertidig = []
            for kol in range(self.kolonner):
                midlertidig.append(Celle())
            self.brett.append(midlertidig)


    def tegnBrett(self):
        for rad in self.brett:
            #print([b.signOfLife() for b in i])
            print(" ".join(repr(kol.signOfLife()) for kol in rad).replace("'", "" ))
        print("Generasjon: " + str(self.generasjon) + " - Antall levende celler: " + str(self.finnAntallLevende()))

    def oppdatering(self):


        bliLevende = []
        bliDød = []

        for rad in self.brett:
            for kol in rad:

                teller = 0
                ''' Gamle versjonen
                if b.erLevende() == True: #Lever cellen
                    templiste = self.finnNabo(self.brett.index(i), i.index(b))
                    for u in templiste:
                        for k in u:
                            if u == "O":
                                teller += 1
                    if teller < 2: #Underpopulasjon
                        bliDød.append(b)
                    if teller > 3: #Overpopulasjon
                        bliDød.append(b)

                    if teller == 2 or teller == 3:
                        bliLevende.append(b)

                if b.erLevende() == False: #Er cellen død
                    templiste = self.finnNabo(self.brett.index(i), i.index(b))
                    for u in templiste:
                        for k in u:
                            if u == "O":
                                teller += 1
                    if teller == 3:
                        bliLevende.append(b)
                '''

                if kol.erLevende() == True: #Lever cellen
                    templiste = self.finnNabo(self.brett.index(rad), rad.index(kol))
                    for nabo in templiste:
                        if nabo.erLevende() == True:
                            teller += 1
                    if teller < 2: #Underpopulasjon
                        bliDød.append(kol)
                    if teller > 3: #Overpopulasjon
                        bliDød.append(kol)

                    if teller == 2 or teller == 3:
                        bliLevende.append(kol)

                if kol.erLevende() == False: #Er cellen død
                    templiste = self.finnNabo(self.brett.index(rad), rad.index(kol))
                    for nabo in templiste:
                        if nabo.erLevende() == True:
                            teller += 1
                    if teller == 3:
                        bliLevende.append(kol)

        for celle in bliDød:
            celle.settDoed()

        for celle in bliLevende:
            celle.settLevende()

        self.generasjon += 1

    def finnAntallLevende(self): #Teller alle cellene, legger til 1 levende par Levende celle
        levende = 0
        for rad in self.brett:
            for kol in rad:
                if kol.erLevende():
                    levende += 1

        return levende

    def generer(self): # Generer første sett med celler
        for rad in self.brett:
            for kol in rad:
                if random.randint(0,2) == 1:
                    kol.settLevende()
    ''' Gamle versjonen
    def finnNabo(self, x, y): # Looper igjennom alle naboen til en gitt celle

        listeNabo = []
        for rad in range(y-1, y+2):
            for kol in range(x-1, x+2):
                corr = True
                if rad == x and kol == y:
                    corr = False
                if rad < 0 or rad >= self.rader:
                    corr = False
                if kol < 0 or kol >= self.kolonner:
                    corr = False
                if corr:
                    listeNabo.append(self.brett[kol][rad].signOfLife())
        return listeNabo
    '''

    def finnNabo(self, x, y): # Looper igjennom alle naboen til en gitt celle

        listeNabo = []
        for rad in range(x-1, x+2):
            for kol in range(y-1, y+2):
                corr = True
                if rad == x and kol == y:
                    corr = False
                if rad < 0 or rad >= self.rader:
                    corr = False
                if kol < 0 or kol >= self.kolonner:
                    corr = False
                if corr:
                    listeNabo.append(self.brett[rad][kol])
        #print(listeNabo)
        return listeNabo
