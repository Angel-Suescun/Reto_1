# Reto_1 (Angel Suescun)
Programación Orientada a Objetos - UNAL-Reto #01

## Punto 1

- Desarrollé el ejercicio creando una función que reciba como argumentos los números y la operación que se desea realizar. Se utiliza la estructura de control 'match', la cual permite evaluar el valor de una variable y ejecutar el bloque de código correspondiente sin necesidad de utilizar una cadena de sentencias 'if'.

- Además, se manejan posibles errores en el código, como entradas inválidas o intentos de dividir por cero.
```python

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





```

## Punto 2
- Creé una función que recibe una palabra y retorna un valor booleano
que indica si la palabra es un palíndromo o no. La función convierte
la palabra a minúsculas para evitar errores al comparar letras
mayúsculas y minúsculas. Luego, utiliza un ciclo 'for' para iterar
sobre la primera mitad de la palabra, comparando cada letra con la
letra correspondiente de la segunda mitad (empezando desde el final).
Si alguna letra no coincide, la función retorna 'False'. Si todo el
ciclo se ejecuta sin encontrar diferencias, la palabra es un palíndromo
y la función retorna 'True'.

```python


def palindromo(palabra: str) -> bool:
    palabra = palabra.lower()
    for i in range(len(palabra) // 2):
        if palabra[i] != palabra[-i - 1]:
            return False
    return True


palabra = input("Ingrese una palabra: ")
if palindromo(palabra):
    print(f"{palabra} es un palíndromo")
else:
    print(f"{palabra} no es un palíndromo")




```

## Punto 3
- Hice una función la cual recibe una lista de números y retorna una lista
de números primos. Un ciclo 'for' itera cada número de la lista hacia
otro 'for', el cual analiza los números anteriores a él. Si su residuo
es 0, no es primo. Si no es divisible, se agrega a la lista de primos.

```python



def primos(numero: list) -> list:
    primos = []

    for i in numero:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            primos.append(i)

    if not primos:
        return "No hay números primos en la lista"

    if 1 in numero:
        primos.remove(1)  # El 1 no se considera primo

    return primos


lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
primos_en_lista = primos(lista_numeros)
print(f"Los números primos de la lista {lista_numeros} son: {primos_en_lista}")



```

## Punto 4
- Esta función recibe una lista de números y retorna una lista que contiene los
números con los que se realizó la suma y el resultado de la suma entre ellos.

- Utiliza un ciclo 'for' para iterar sobre la lista de números y sumar dos números
consecutivos. Cuando esta suma es mayor a la suma máxima registrada previamente,
la reemplaza con la nueva suma y los números correspondien

```python


def sumatoria_mayor(numeros: list) -> list:

    suma_mayor = 0
    numeros_mayor = []

    for i in range(len(numeros) - 1):
        suma = numeros[i] + numeros[i + 1]
        if suma > suma_mayor:
            suma_mayor = suma
            numeros_mayor = [numeros[i], numeros[i + 1], suma_mayor]

    return numeros_mayor


lista_numeros = [11, 22, 35, 39, 5, 5600, 71, 81, 99, 105, 110, 1]
lista_mayor = sumatoria_mayor(lista_numeros)

print(
    f"La suma entre dos números consecutivos de {lista_numeros} es: "
    f"{lista_mayor[0]} + {lista_mayor[1]} = {lista_mayor[2]}"
)




```
## Punto 5
- La función ingresa una lista de palabras y verifica si hay anagramas
entre ellas. Para evitar confusión, convierte todas las palabras a
minúsculas. Luego, en un primer 'for', itera sobre una palabra para que
en el siguiente 'for' se puedan comparar con el resto de palabras. Cada
letra se ordena por medio del código ASCII. Si las palabras son iguales
después de ordenarlas, son anagramas. Se utiliza una variable booleana para
saber si hay anagramas o no y luego imprimir el mensaje correspondiente.
```python

def anagrama(palabras: list) -> list:

    hay_anagrama = False
    lista_minuscula = [palabra.lower() for palabra in palabras]

    for i in range(len(lista_minuscula)):
        for j in range(i + 1, len(lista_minuscula)):
            if sorted(lista_minuscula[i]) == sorted(lista_minuscula[j]):
                print(f"{palabras[i]} y {palabras[j]} son anagramas")
                hay_anagrama = True

    if not hay_anagrama:
        print("No hay anagramas")


lista_palabras = ["amor", "roma", "perro"]
anagrama(lista_palabras)


```
