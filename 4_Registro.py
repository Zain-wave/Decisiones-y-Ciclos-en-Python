nombres_ingresados = []
entrada = ""

print("Registro de asistentes")
print("Ingresa nombres y escribe 'FIN' cuando termines")

while entrada != "fin":
    entrada = input("Ingresa un nombre: ").strip().lower()
    
    if entrada == "fin":
        continue
    
    if not entrada:
        print("Debe ingresar un nombre")
        continue
    
    nombres_ingresados.append(entrada)  
    print(f"Nombre '{entrada}' registrado")


hay_repetidos = len(nombres_ingresados) != len(set(nombres_ingresados))

total_nombres = len(nombres_ingresados)

print(f"\nTotal de nombres que ingresaste: {total_nombres}")

if total_nombres == 0:
    print("No hay nombres")
elif hay_repetidos:
    print("Hay nombres repetidos")
else:
    print("No hay nombres repetidos")