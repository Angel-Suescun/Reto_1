"""
Hice una función la cual recibe una lista de números y retorna una lista
de números primos. Un ciclo 'for' itera cada número de la lista hacia
otro 'for', el cual analiza los números anteriores a él. Si su residuo
es 0, no es primo. Si no es divisible, se agrega a la lista de primos.
"""

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
