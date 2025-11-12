print("Análisis numérico")
while True:
    if not (num1_str := input("Ingresa el primer numero entero: ").strip()):
        print("Debes ingresar algo")
        continue
    
    if num1_str.lstrip('-').isdigit():
        num1 = int(num1_str)
        break
    else:
        print("Ingresa un numero entero")

while True:
    if not (num2_str := input("Ingresa el segundo numero entero: ").strip()):
        print("Debes ingresar algo")
        continue
    
    if num2_str.lstrip('-').isdigit():
        num2 = int(num2_str)
        break
    else:
        print("Ingresa un numero entero")

while True:
    if not (num3_str := input("Ingresa el tercer numero entero: ").strip()):
        print("Debes ingresar algo")
        continue
    
    if num3_str.lstrip('-').isdigit():
        num3 = int(num3_str)
        break
    else:
        print("Ingresa un numero entero")

p1 = num1 > 0
p2 = num2 > 0
p3 = num3 > 0

n1 = num1 < 0
n2 = num2 < 0
n3 = num3 < 0

c1 = num1 == 0
c2 = num2 == 0
c3 = num3 == 0

if p1 and p2 and p3:
    print("Todos 3 son positivos")
elif n1 or n2 or n3:
    print("Uno de los numeros es negativo")
elif (c1 and not c2 and not c3) or (c2 and not c1 and not c3) or (c3 and not c1 and not c2):
    print("Uno de los numeros es 0")
else:
    print("La combinación no cumple con las condiciones específicas (los tres positivos, al menos un negativo, o exactamente un cero)")