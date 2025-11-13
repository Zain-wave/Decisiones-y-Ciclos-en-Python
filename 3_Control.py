usuario_restringido = ["pepe", "meow"]
usuario_valido = False
codigo_valido = False

print("Control de acceso")

while not usuario_valido:
    if not (nombre_usuario := input("Tu nombre de usuario: ").strip().lower()):
        print("Debe digitar un usuario")
    elif nombre_usuario in usuario_restringido:
        print("Ese usuario está restringido. Ingrese otro")
    else:
        usuario_valido = True

while not codigo_valido:
    if not (codigo_str := input("Tu código numérico: ").strip()):
        print("Debes digitar algo")
        continue

    if codigo_str.isdigit():
        codigo = int(codigo_str)
        if codigo >= 0:
            codigo_valido = True
        else:
            print("El código no puede ser negativo")
    else:
        print("Debes digitar un numero")

es_multiplo_de_2 = (codigo % 2 == 0)
termina_en_7 = (codigo % 10 == 7)


if es_multiplo_de_2 or termina_en_7:
    print("\nDentro")
else:
    print("\nNo se cumplen los requisitos para entrar")
    print("Tu código debe ser par o terminar en 7")