pan_vendido = int(input("Cantidad de pan vendido (no fresco): "))

Precio_barra_pan = 3.49
pan_desc = round((pan_vendido * (Precio_barra_pan *0.6)) , 2)
coste_total = round((pan_vendido * (Precio_barra_pan - Precio_barra_pan * 0.6)) , 2)

print(f"""
El precio de la barra de pan fresco es de: {Precio_barra_pan} euros

El descuento de la barra de pan (no fresco) es de: {pan_desc} euros

El costo total a pagar es de: {coste_total} euros """)
