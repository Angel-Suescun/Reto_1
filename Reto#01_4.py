"""
Esta función recibe una lista de números y retorna una lista que contiene los
números con los que se realizó la suma y el resultado de la suma entre ellos.

Utiliza un ciclo 'for' para iterar sobre la lista de números y sumar dos números
consecutivos. Cuando esta suma es mayor a la suma máxima registrada previamente,
la reemplaza con la nueva suma y los números correspondientes.
"""

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
