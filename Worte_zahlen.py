def worte_zahlen():
    satz = input("Schreiben Sie einen Satz: ")
    # Teilen den Satz in Wörter
    worte = satz.split()
    # Zahlen die Woerte
    anzahl_worte = len(worte)

    return anzahl_worte


print(f"Anzahl wörte= {worte_zahlen()}")
