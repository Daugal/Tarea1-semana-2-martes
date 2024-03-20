inversion = int(input("Digite la cantidad de dinero a depositar: "))

anio1 = round((inversion + inversion * 0.04) ,2)
anio2 = round((anio1 + anio1 * 0.04) ,2)
anio3 = round((anio2 + anio2 * 0.04) ,2)

print(f"""El ahorro a invertir es de {inversion}
       El ahorro del primer año será de {anio1}
       El ahorro del segundo año será de {anio2}
       El ahorro del tercer año será de {anio3}""")
