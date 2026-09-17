
# Tvoje pôvodné zoznamy kategórií
ovocie = ["jablko", "hruska", "banan", "mango"]
mliecne = ["mlieko", "jogurt"]

# NOVINKA: Slovník cien (kľúč = názov, hodnota = cena v eurách)
ceny = {
    "jablko": 0.50,
    "hruska": 0.70,
    "banan": 0.40,
    "mango": 1.50,
    "mlieko": 1.20,
    "jogurt": 0.80,
    "cukor": 1.10,
    "cokolada": 1.30
}

# Tvoj pôvodný košík
nakupny_kosik = ["jablko", "mlieko", "cukor", "cokolada", "jogurt", "banan", "mango"]

# Tvoj pôvodný cyklus na pridávanie
while True:
    print("co chcete pridat do kosika?")
    vstup = input()
    if vstup == "uz nic" or vstup == "koniec":
        break
    else:
        nakupny_kosik.append(vstup)

print("--------------------------")

# Premenná na spočítanie celkovej ceny
celkova_cena = 0

# Tvoj opravený cyklus na výpis
for polozka in nakupny_kosik:
    # Zistíme cenu zo slovníka (ak položka v slovníku nie je, dáme cenu 0)
    cena = ceny.get(polozka, 0)
    celkova_cena += cena

    # Dôležitá oprava: použi 'elif', aby pri ovocí nevypisovalo aj "nieco ine"
    if polozka in ovocie:
        print(f"{polozka} je ovocie ({cena} €)")
    elif polozka in mliecne:
        print(f"{polozka} je mliecny vyrobok ({cena} €)")
    else:
        print(f"{polozka} je nieco ine ({cena} €)")

print("--------------------------")
print(f"Celková cena nákupu je: {celkova_cena} €")


                   


