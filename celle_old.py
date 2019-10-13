import random
class Celle:
    def __init__(self, id, status):
        self.status = status
        self.id = id


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
            return "."
        else:
            return "O"
