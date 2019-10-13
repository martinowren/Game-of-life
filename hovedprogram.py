import os
from spillebrett import Spillebrett
def hovedprogram():
    kolonner = int(input("Hvor mange kolonner ønsker du? "))
    rader = int(input("Hvor mange rader ønsker du? "))
    første_brett = Spillebrett(kolonner, rader)

    valgEn = int(input("Ønsker du å gjøre simuleringen manuelt, eller se animasjonen frem til 100? Skriv 1 eller 2 for å velge: "))
    if valgEn == 2: # Denne koden kjører hvis du velger animasjonssimulering
        tall = 1
        første_brett.generer()
        første_brett.tegnBrett()
        while tall < 100:
            os.system("clear")
            første_brett.oppdatering()
            første_brett.tegnBrett()
            tall += 1
    else: # Denne koden kjøres hvis du velger manuel simulering
        første_brett.generer()
        første_brett.tegnBrett()
        innTast = ""


        while innTast != "q":
            innTast = input("Press enter for å fortsette. Skriv in q og trykk enter for å avslutte:\n")

            if innTast == "":
                os.system("clear")
                # print(første_brett.brett[1][0]) Brukt i debug
                # print(første_brett.finnNabo(1,0)) Brukt i debug
                første_brett.oppdatering()
                første_brett.tegnBrett()
            elif innTast == "q":
                break

    print("Programmet er avsluttet")


hovedprogram()
