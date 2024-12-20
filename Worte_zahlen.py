def worte_zahlen():
    satz = input("Schreiben Sie einen Satz: ")
    worte = satz.split()
    anzahl_worte = len(worte)

    return anzahl_worte


print(f"Anzahl wörte= {worte_zahlen()}")
