edad_valida = False
while not edad_valida:
    if not (edad_str := input("Ingresa tu edad: ").strip()):
        print("Debes ingresar algo")
        continue
    
    if edad_str.lstrip('-').isdigit(): 
        edad = int(edad_str)
        if edad < 0 or edad > 120: 
            print("Ingresa una edad valida")
            continue
        edad_valida = True
    else:
        print("Ingresa un numero entero")

#hola

nivel_valido = False
while not nivel_valido:
    if not (nivel := input("¿Actualmente estudias, trabajas o ninguna? ").strip().lower()):
        print("Debes ingresar algo")
        continue
    
    if nivel in ["estudia", "trabaja", "ninguna"]:
        nivel = nivel.capitalize()
        nivel_valido = True
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