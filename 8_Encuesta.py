respuestas_si = 0
respuestas_no = 0
edad = 1

print("Encuesta de preferencias")
print("Dime tu edad y si te gusta programar. Ingresa 0 o menos en la edad para terminar")

while edad > 0:
    edad_input_valida = False
    while not edad_input_valida:
        if not (edad_str := input("\n¿Cuántos años tienes?: ").strip()):
            print("Debes ingresar algo")
            continue
        
        if edad_str.lstrip('-').isdigit():
            edad = int(edad_str)
            if edad <= 0:
                edad_input_valida = True
                break
            if edad >= 1 and edad <= 120:
                edad_input_valida = True
                break
            else:
                print("Esa edad no es válida para la pregunta")
        else:
            print("Necesito un número entero")
            
    if edad <= 0:
        break

    respuesta_input_valida = False
    while not respuesta_input_valida:
        if not (respuesta := input("¿Te gusta programar? (si/no): ").strip().lower()):
            print("Debes responder algo")
            continue
        
        if respuesta in ["si", "sí"]:
            respuestas_si += 1
            respuesta_input_valida = True
        elif respuesta == "no":
            respuestas_no += 1
            respuesta_input_valida = True
        else:
            print("Responde solo 'si' o 'no'")

print(f"Respuestas afirmativas (Sí): {respuestas_si}")
print(f"Respuestas negativas (No): {respuestas_no}")