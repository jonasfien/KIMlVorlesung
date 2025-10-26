# Ausgabe Ventilatorsteuerung in %
# Eingabe Temperatur in Grad Celsius
#
# 1. Fuzzifizierung
#   Preisniveau und Qualität
#   Preisniveau 0-100 Euro pro Ware:
#   0-20:   niedrig
#   40-60:  mittel
#   80-100: hoch
#
#   Qualität 1-5:
#   1:  niedrig
#   3:  mittel
#   5:  hoch
#
# 2. Regelbasis
#  Je höher die Qualität und je niedriger das Preisniveau, je besser die Eignung
#
# 3. Defuzzifizierung
#  Eignung
#  Geeignet
#  bedingt geeignet
#  nicht geeignet


def main():
    # Input holen
    qal, niv = getInput()
    print(f"Eingabe: Qualität:{qal} Preisniveau{niv}")

    # Werte für Preisniveau und Qualität ermitteln
    nivnied, nivmittel, nivgroß = ermittlePreisniveau(niv)
    qualnied, qualmittel, qualgroß = ermittleQualitaet(qal)

    print()
    print("Preisniveau Einordnung")
    print(f"Niedrig: {nivnied}")
    print(f"Mittel: {nivmittel}")
    print(f"Groß: {nivgroß}")

    print()
    print("Qualität Einordnung")
    print(f"Niedrig: {qualnied}")
    print(f"Mittel: {qualmittel}")
    print(f"Groß: {qualgroß}")

    nivArr = [nivnied, nivmittel, nivgroß]
    qualArr = [qualnied, qualmittel, qualgroß]

    eignung, eignungVal = ermittleEignung(qualitaet=qualArr, preisniveau=nivArr)

    print(f"Kalkulatorischer Wert der Eignung ist:{eignungVal}")
    print(f"Das Produkt ist {eignung}")


# returns int,int qualiteat und preisniveau als zurück
def getInput():
    qualitaet = -1
    preisniveau = -1
    while True:
        try:
            if 1 > qualitaet or 6 < qualitaet:
                qualitaet = int(input("Eingabewert Qualität(1-5):"))
            if 1 > preisniveau or 101 < preisniveau:
                preisniveau = int(input("Eingabewert Preisniveau(1-100):"))
        except ValueError:
            print("Gültige Zahl eingeben!")
        if 0 < qualitaet and qualitaet < 6 and 0 < preisniveau and preisniveau < 101:
            return qualitaet, preisniveau
        else:
            print("Gültige Zahl eingeben!")


# returns int,int,int gibt Preisniveau im format niedrig,mittel,hoch zurück
def ermittlePreisniveau(preis):
    if preis <= 20:
        return 1, 0, 0  # niedrig
    if 20 < preis < 40:
        mittel = (preis - 20) / 20
        return 1 - mittel, mittel, 0
    if 40 <= preis <= 60:
        return 0, 1, 0  # mittel
    if 60 < preis < 80:
        hoch = (preis - 60) / 20
        return 0, 1 - hoch, hoch
    if preis >= 80:
        return 0, 0, 1  # hoch
    return 0, 0, 0


# returns int,int,int gibt Qualität im format niedrig mittel hoch zurück
def ermittleQualitaet(qualitaet):
    if qualitaet == 1:
        return 1, 0, 0
    if qualitaet == 2:
        return 0.5, 0.5, 0
    if qualitaet == 3:
        return 0, 1, 0
    if qualitaet == 4:
        return 0, 0.5, 0.5
    if qualitaet == 5:
        return 0, 0, 1
    return 0, 0, 0


# Verarbeitet Qualität und Preisniveau als Listen von Integer oder Float
def ermittleEignung(qualitaet, preisniveau):
    # 0 fuer Mittel -1 fuer Niedrig 1 fuer Hoch
    qualitaetVal = 0
    preisniveauVal = 0
    # qualitaet von Niedrig nach Hoch im Array wobei hoch gut ist
    if qualitaet[0] > qualitaet[1]:
        qualitaetVal = -1
    elif qualitaet[2] > qualitaet[1]:
        qualitaetVal = 1

    if preisniveau[0] > preisniveau[1]:
        preisniveauVal = 1
    elif preisniveau[2] > preisniveau[1]:
        preisniveauVal = -1

    eignung = preisniveauVal + qualitaetVal
    if eignung == 0:
        return "bedingt geeignet.", eignung
    if eignung < 0:
        return "nicht geeignet.", eignung
    return "geeignet.", eignung


if __name__ == "__main__":
    main()
