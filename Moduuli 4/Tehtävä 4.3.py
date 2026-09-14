syote = input("Anna luku ( tyhjä lopettaa): ")

pienin = syote
suurin = syote

while syote != "":
    luku =int(syote)
    if pienin == syote or luku  < pienin:
        pienin = luku
    if suurin == syote or luku > suurin:
        suurin = luku
    syote = input("Anna luku ( tyhjä lopettaa): ")
print("Pienin luku on:", pienin)
print("Suurin luku on:", suurin)
