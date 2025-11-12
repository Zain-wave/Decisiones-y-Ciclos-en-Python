data_base = {
    "usuario": "zainax",
    "clave": "Plitx90."
}

intentos_actuales = 0
acceso_exitoso = False

print("Intentos limitados")
print("Tienes 3 intentos para ingresar correctamente")

while intentos_actuales < 3 and not acceso_exitoso:
    print(f"\nIntento {intentos_actuales + 1} de 3")
    
    if not (usuario_ingresado := input("Usuario: ").strip()) or not (clave_ingresada := input("Clave: ").strip()):
        print("Debe ingresar algo")
        continue 
        
    usuario_ok = (usuario_ingresado == data_base["usuario"])
    clave_ok = (clave_ingresada == data_base["clave"])

    if usuario_ok and clave_ok:
        print("Acceso concedido")
        acceso_exitoso = True
    else:
        intentos_actuales += 1
        
        if not usuario_ok and not clave_ok:
            print("Usuario y Clave incorrectos")
        elif not usuario_ok:
            print("Usuario incorrecto")
        elif not clave_ok:
            print("Clave incorrecta")

if not acceso_exitoso and intentos_actuales == 3:
    print("Intentos insuficientes. Acceso bloqueado")