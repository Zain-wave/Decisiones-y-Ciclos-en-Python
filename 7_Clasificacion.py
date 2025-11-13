print("Clasificación de cliente")

monto_valido = False
while not monto_valido:
    if not (monto_str := input("Valor total de la compra: ").strip()):
        print("Debes ingresar algo")
        continue

    if monto_str.count('.') <= 1 and monto_str.replace('.', '', 1).lstrip('-').isdigit():
        monto = float(monto_str)
        if monto < 0:
            print("El monto no puede ser negativo")
            continue
        monto_valido = True
    else:
        print("Ingresa un número válido")

membresia_valida = False
while not membresia_valida:
    if not (membresia := input("Tipo de membresía (activa/temporal/ninguna): ").strip().lower()):
        print("Debes ingresar algo")
        continue
    if membresia in ["activa", "temporal", "ninguna"]:
        membresia_valida = True
    else:
        print("Escribe solo: activa, temporal o ninguna")

if (monto >= 1000) and (membresia == "activa"):
    clasificacion = "Premium"
elif (monto >= 300) or (membresia == "temporal"):
    clasificacion = "Frecuente"
else:
    clasificacion = "Regular"

print(f"El cliente es: {clasificacion}")