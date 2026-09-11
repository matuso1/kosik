#kategorie
ovocie = ["jablko", "hruska", "banan", "mango"]
mliecne = ["mlieko", "jogurt"]
sladkosti = ["cukor", "cokolada"]


#kosik
nakupny_kosik = ["jablko", "mlieko", "cukor", "cokolada", "jogurt", "banan", "mango"]



while True:
    print ("co chcete pridat do kosika?")
    vstup = input()
    if vstup == "uz nic" or vstup == "koniec":
        break
    else:
     nakupny_kosik.append(vstup)

print("--------------------------")

for polozka in nakupny_kosik:
    if polozka in ovocie:
        print (f"{polozka} je ovocie")
    if  polozka in mliecne: 
            print (f"{polozka} je mliecny vyrobok")
    else:
     print(f"{polozka} je nieco ine ")



                   


