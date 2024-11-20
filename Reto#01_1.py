"""
Desarrolle el ejercicio creando una función que reciba como argumentos
los números y la operación que se desea realizar. Se utiliza la estructura
de control 'match', la cual permite evaluar el valor de una variable y
ejecutar el bloque de código correspondiente sin necesidad de utilizar
una cadena de sentencias 'if'.

Además, se manejan posibles errores en el código, como entradas inválidas
o intentos de dividir por cero.
"""

def calculator(number1: int, number2: int, operation: str) -> float:
    match operation:
        case '+':
            return number1 + number2
        case '-':
            return number1 - number2
        case '*':
            return number1 * number2
        case '/':
            if number2 == 0:
                return "No se puede dividir por cero"
            return number1 / number2
        case _:
            return "Operación inválida"


number1 = int(input("Ingrese el primer número: "))
number2 = int(input("Ingrese el segundo número: "))
operation = input(
    "Ingrese la operación (Suma: +, Resta: -, Multiplicación: *, División: /): "
)

if operation not in ["+", "-", "*", "/"]:
    print("Operación no válida")
else:
    print(
        f"La operación {number1}{operation}{number2} da como resultado: "
        f"{calculator(number1, number2, operation)}"
    )



