edad_valida = False
while not edad_valida:
    if not (edad_str := input("¿Cuántos años tienes?: ").strip()):
        print("Debes ingresar algo")
        continue

    if edad_str.isdigit():
        edad = int(edad_str)
        if 0 < edad < 120:
            edad_valida = True
        else:
            print("Esa edad no parece correcta")
    else:
        print("Necesito un número entero, por favor")

licencia_valida = False
while not licencia_valida:
    if not (licencia_vigente_str := input("¿Tienes tu licencia de conducir al día? (Si/No): ").strip().lower()):
        print("Debes ingresar algo")
        continue
    if licencia_vigente_str in ["si", "sí", "no"]:
        licencia_vigente = licencia_vigente_str in ["si", "sí"]
        licencia_valida = True
    else:
        print("Solo dime 'Si' o 'No'")

vehiculo_valido = False
while not vehiculo_valido:
    if not (vehiculo_propio_str := input("¿El vehículo es tuyo?: ").strip().lower()):
        print("Debes ingresar algo")
        continue
    if vehiculo_propio_str in ["si", "sí", "no"]:
        vehiculo_propio = vehiculo_propio_str in ["si", "sí"]
        vehiculo_valido = True
    else:
        print("Solo dime 'Si' o 'No'")

prestamo_autorizado = False
if not vehiculo_propio:
    prestamo_valido = False
    while not prestamo_valido:
        if not (prestamo_str := input("¿Tienes permiso para usar uno prestado?: ").strip().lower()):
            print("Debes ingresar algo")
            continue
        if prestamo_str in ["si", "sí", "no"]:
            prestamo_autorizado = prestamo_str in ["si", "sí"]
            prestamo_valido = True
        else:
            print("Solo dime 'Si' o 'No'")

condicion_edad = (edad >= 18)
condicion_licencia = licencia_vigente
condicion_vehiculo = (vehiculo_propio or prestamo_autorizado)

apto_para_competir = (condicion_edad and condicion_licencia and condicion_vehiculo)

if apto_para_competir:
    print("Eres apto")
else:
    print("No cumples con los requisitos para competir")
    
    print("\nFaltó un poquito:")
    if not condicion_edad:
        print(f" - Tienes que ser mayor de 18 (tienes {edad} años)")
    if not condicion_licencia:
        print(" - Necesitas la licencia al día")
    if not condicion_vehiculo:
        print(" - Debes tener tu propio vehículo o uno prestado con permiso")