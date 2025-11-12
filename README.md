# Actividad: Decisiones y Ciclos en Python

**Propósito:**
Aplicar estructuras condicionales (`if`, `elif`, `else`), operadores lógicos (`and`, `or`, `not`) y bucles `while` para resolver situaciones que requieren análisis y control del flujo de ejecución.

Cada punto debe resolverse de forma individual, con código claro, validación de entradas y sin ejemplos predefinidos.

---

## P1. Etapa vital y formativa

Solicita la edad y el nivel educativo de una persona.
Clasifica su etapa según las siguientes reglas:

- Menor de 6 años → **Infante**
- Entre 6 y 17 años y estudia → **Estudiante escolar**
- Entre 18 y 25 años y estudia → **Universitario**
- Mayor de 25 años y trabaja → **Adulto activo**
- Mayor de 60 años y no trabaja → **Adulto mayor jubilado**
- En cualquier otro caso → **No determinado**

Valida que la edad sea coherente y utiliza condiciones encadenadas con operadores lógicos.

---

## P2. Participante elegible

Solicita la edad, si tiene licencia de conducción y si posee vehículo propio.
Determina si la persona puede participar en una competencia, aplicando las siguientes condiciones:

- Edad mínima de 18 años.
- Licencia vigente.
- Vehículo propio **o** préstamo autorizado.

Evalúa con combinaciones de `and` y `or` para determinar si es **Apto** o **No apto**.

---

## P3. Control de acceso

Pide un nombre de usuario y un código numérico.
Permite el ingreso solo si el usuario **no** está en la lista restringida y su código cumple al menos una de las siguientes condiciones:

- Es múltiplo de 2.
- Termina en 7.

Debe mostrar un mensaje distinto según el motivo del rechazo.
Elabora un **diagrama de flujo** que represente la decisión principal.

---

## P4. Registro de asistentes

Crea un ciclo que solicite nombres hasta que se escriba “FIN”.
Al finalizar, muestra:

- El total de nombres ingresados.
- Si hay nombres repetidos.

El programa debe ignorar entradas vacías y evitar estructuras automáticas de comparación.

---

## P5. Intentos limitados

Simula un inicio de sesión con usuario y contraseña predefinidos.
Permite hasta tres intentos.
Si ambos campos están vacíos, el intento no cuenta.
Finaliza al alcanzar el máximo o lograr acceso exitoso.
Evalúa cada combinación con operadores lógicos y muestra el motivo del fallo.

---

## P6. Análisis numérico

Solicita tres números enteros y determina:

- Si los tres son positivos.
- Si al menos uno es negativo.
- Si exactamente uno es cero.

Debe analizar todas las combinaciones mediante condiciones encadenadas.

---

## P7. Clasificación de cliente

Pide el valor total de una compra y el tipo de membresía.
Clasifica al cliente como:

- **Premium** → monto alto y membresía activa.
- **Frecuente** → monto medio **o** membresía temporal.
- **Regular** → cualquier otro caso.

Si el monto es inválido, muestra un mensaje de error.

---

## P8. Encuesta de preferencias

Solicita edad y respuesta a la pregunta: “¿Te gusta programar?” (sí/no).
El programa debe repetirse mientras la edad ingresada sea mayor a cero.
Al finalizar, muestra cuántas respuestas fueron afirmativas y cuántas negativas.
Controla respuestas vacías o incorrectas dentro del ciclo.

---

## P9. Investigación sobre bucles

Crea un archivo llamado **`investigacion_bucles.md`** donde respondas:

1. Diferencias entre un **bucle controlado por contador** y un **bucle controlado por condición**.
2. Ejemplos cotidianos que representen el uso de cada tipo de bucle.
3. Cuándo es más apropiado usar `while` en lugar de `for`.
4. Qué es un **bucle infinito**, cómo prevenirlo y cómo detectarlo durante la ejecución.
5. Qué función cumplen las sentencias `break` y `continue` dentro de un ciclo.
6. Explica el error lógico más común al usar `while` y cómo evitarlo.

El archivo debe incluir títulos, subtítulos y ejemplos descriptivos en formato Markdown.

---

## P10. Panel de control doméstico

Desarrolla un sistema por consola que simule el control de una vivienda:

- Menú con opciones para encender luces, activar calefacción, ver estado o salir.
- Las luces solo pueden encenderse si es de noche.
- La calefacción solo puede activarse si la temperatura es menor a 18 °C y las luces están encendidas.
- El sistema debe conservar el estado entre acciones y validar combinaciones imposibles.

Incluye un diagrama de flujo que muestre la lógica de las condiciones principales.

---
