luces_encendidas = False
calefaccion_encendida = False
temperatura_ambiente = 20
es_de_noche = False

print("Panel de control doméstico\n")

while True:
    print(f"\nTemperatura actual: {temperatura_ambiente}°C")
    
    estado_luz = "Encendidas" if luces_encendidas else "Apagadas"
    estado_calefaccion = "Encendida" if calefaccion_encendida else "Apagada"
    estado_tiempo = "Si" if es_de_noche else "No"
    
    print(f"Estado de luces: {estado_luz}")
    print(f"Estado de calefacción: {estado_calefaccion}")
    print(f"¿Es de noche?: {estado_tiempo}")
    
    print("\nOpciones:")
    print("1: Encender/Apagar luces")
    print("2: Activar/Desactivar calefacción")
    print("3: Cambiar hora (Día/Noche)")
    print("4: Cambiar temperatura (Simulación)")
    print("0: Salir")
    
    if not (opcion_str := input("Elige una opción: ").strip()):
        print("Debes ingresar algo")
        continue

    if not opcion_str.isdigit():
        print("Ingresa un número de opción válido")
        continue
        
    opcion = int(opcion_str)

    match opcion:
        case 0:
            print("Bye bye")
            break
        
        case 1:
            if not luces_encendidas:
                if es_de_noche:
                    luces_encendidas = True
                    print("Luces encendidas")
                else:
                    print("No puedes encender las luces de día")
            else:
                luces_encendidas = False
                calefaccion_encendida = False
                print("Luces y calefacción apagadas")

        case 2:
            if not calefaccion_encendida:
                if (temperatura_ambiente < 18) and luces_encendidas:
                    calefaccion_encendida = True
                    print("Calefacción activada")
                elif not luces_encendidas:
                    print("Debes encender las luces primero para la calefacción")
                else:
                    print("La temperatura ya es agradable (18°C o más)")
            else:
                calefaccion_encendida = False
                print("Calefacción desactivada")
            
        case 3:
            es_de_noche = not es_de_noche
            print(f"Ahora es {"de noche" if es_de_noche else "de dia"}")
        
        case 4:
            while True:
                if not (temp_nueva_str := input("Nueva temperatura (ej 15): ").strip()):
                    print("Debes ingresar algun valor valor")
                    continue
                
                if temp_nueva_str.lstrip('-').isdigit():
                    temperatura_ambiente = int(temp_nueva_str)
                    print(f"Temperatura ajustada a {temperatura_ambiente}°C")
                    break
                else:
                    print("Ingresa solo números enteros")
                    
        case _:
            print("Opción no válida")