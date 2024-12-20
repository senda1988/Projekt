def gerade_ungerade():
    number = int(input("Schreiben Sie eine Zahl: "))
    rest = number / 2
    if rest == 0:
        return print(f"Die Zahl {number} ist gerade")
    else:
        return print(f"Die Zahl {number} ist ungerade")


gerade_ungerade()
