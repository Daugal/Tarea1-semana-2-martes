inversion = int(input("Cuánto desea invertir? "))
ianual = int(input("Cuanto es el interés anual? "))
cantanos = int(input("Por cuántos años desea invertir? "))

capital = round(inversion *(ianual/100 + 1)**cantanos,2)

print("El capital ganadosserá de: ", capital)