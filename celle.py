class Celle:
    teller = 0
    def __init__(self):
        self.status = "død"
        self.nr = Celle.teller #BRUKT I DEBUGGINGEN
        Celle.teller += 1 #BRUKT I DEBUGGINGEN

    def settDoed(self):
        self.status = "død"

    def settLevende(self):
        self.status = "levende"

    def erLevende(self):
        if self.status == "død":
            return False
        else:
            return True

    def signOfLife(self):
        if self.status == "død":
            return "." # str(self.nr)
        else:
            return "O" #+ str(self.nr)

    def __repr__(self):
        return self.signOfLife() #BRUKT I DEBUGGINGEN
