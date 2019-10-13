# Oppretter skattekart
skattekart =  []
stoerrelse = 5
for e in range(stoerrelse):
    a = []
    for e in range(stoerrelse):
        a.append("O")
    skattekart.append(a)

# Skriver ut skattekartet foer foerste gjetning
for e in skattekart:
    for f in e:
        print (f, end="")
    print("")
