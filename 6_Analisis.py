print("Análisis numérico")

num1_valido = False
while not num1_valido:
    if not (num1_str := input("Ingresa el primer numero entero: ").strip()):
        print("Debes ingresar algo")
        continue
    
    if num1_str.lstrip('-').isdigit():
        num1 = int(num1_str)
        num1_valido = True
    else:
        print("Ingresa un numero entero")

num2_valido = False
while not num2_valido:
    if not (num2_str := input("Ingresa el segundo numero entero: ").strip()):
        print("Debes ingresar algo")
        continue
    
    if num2_str.lstrip('-').isdigit():
        num2 = int(num2_str)
        num2_valido = True
    else:
        print("Ingresa un numero entero")

num3_valido = False
while not num3_valido:
    if not (num3_str := input("Ingresa el tercer numero entero: ").strip()):
        print("Debes ingresar algo")
        continue
    
    if num3_str.lstrip('-').isdigit():
        num3 = int(num3_str)
        num3_valido = True
    else:
        print("Ingresa un numero entero")

conteo_ceros = (num1 == 0) + (num2 == 0) + (num3 == 0)


if (num1 > 0) and (num2 > 0) and (num3 > 0):
    print("Todos 3 son positivos")
elif (num1 < 0) or (num2 < 0) or (num3 < 0):
    print("Uno de los numeros es negativo")
elif conteo_ceros == 1:
    print("Uno de los numeros es 0")
else:
    print("La combinación no cumple con las condiciones específicas (los tres positivos, al menos un negativo, o exactamente un cero)")