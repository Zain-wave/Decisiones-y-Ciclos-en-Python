while True:
    if not (edad_str := input("Ingresa tu edad: ").strip()):
        print("Debes ingresar algo")
        continue
    
    if edad_str.isdigit():
        edad = int(edad_str)
        if edad < 0 or edad > 120: 
            print("Ingresa una edad valida")
            continue
        break
    else:
        print("Ingresa un numero entero")


while True:
    if not (nivel := input("¿Actualmente estudias, trabajas o ninguna? ").strip().lower()):
        print("Debes ingresar algo")
        continue
    
    if nivel in ["estudia", "trabaja", "ninguna"]:
        nivel = nivel.capitalize()
        break
    else:
        print("Responde solo con: Estudia, Trabaja o Ninguna")

if edad < 6:
    etapa = "Infante"

elif (edad >= 6 and edad <= 17) and (nivel == "Estudia"):
    etapa = "Estudiante Escolar"

elif (edad >= 18 and edad <= 25) and (nivel == "Estudia"):
    etapa = "Universitario"

elif (edad > 25) and (nivel == "Trabaja"):
    etapa = "Adulto activo"

elif (edad > 60) and (nivel == "Ninguna"):
    etapa = "Adulto mayor jubilado"

else:
    etapa = "No determinado"

print(f"Edad: {edad} años")
print(f"Situación actual: {nivel}")
print(f"Etapa de vida: {etapa}")