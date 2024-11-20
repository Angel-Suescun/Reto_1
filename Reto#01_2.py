"""
Crea una función que recibe una palabra y retorna un valor booleano
que indica si la palabra es un palíndromo o no. La función convierte
la palabra a minúsculas para evitar errores al comparar letras
mayúsculas y minúsculas. Luego, utiliza un ciclo 'for' para iterar
sobre la primera mitad de la palabra, comparando cada letra con la
letra correspondiente de la segunda mitad (empezando desde el final).
Si alguna letra no coincide, la función retorna 'False'. Si todo el
ciclo se ejecuta sin encontrar diferencias, la palabra es un palíndromo
y la función retorna 'True'.
"""

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


