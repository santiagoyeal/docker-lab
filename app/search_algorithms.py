"""Algoritmos de búsqueda básicos.

Contiene implementaciones de búsquedas lineal y binaria, así como
una pequeña función de demostración. Este módulo puede ejecutarse
como script para probarlos o importarse desde otros programas.
"""


def linear_search(arr, target):
    """Devuelve el índice del primer elemento igual a target o -1 si no existe."""
    for idx, val in enumerate(arr):
        if val == target:
            return idx
    return -1


def binary_search(arr, target):
    """Busca un elemento en una lista ordenada usando búsqueda binaria.

    Devuelve el índice si se encuentra, o -1 si no está presente.
    """
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def demonstration():
    data = [1, 3, 5, 7, 9, 11, 13]
    print("Datos:", data)
    for t in [5, 6, 11]:
        print(f"Buscando {t} con linear_search: índice = {linear_search(data, t)}")
        print(f"Buscando {t} con binary_search: índice = {binary_search(data, t)}")


if __name__ == "__main__":
    demonstration()
