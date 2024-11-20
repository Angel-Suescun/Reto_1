"""
La función ingresa una lista de palabras y verifica si hay anagramas
entre ellas. Para evitar confusión, convierte todas las palabras a
minúsculas. Luego, en un primer 'for', itera sobre una palabra para que
en el siguiente 'for' se puedan comparar con el resto de palabras. Cada
letra se ordena por medio del código ASCII. Si las palabras son iguales
después de ordenarlas, son anagramas. Se utiliza una variable booleana para
saber si hay anagramas o no y luego imprimir el mensaje correspondiente.
"""
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
