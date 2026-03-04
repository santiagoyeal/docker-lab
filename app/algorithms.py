"""Conjunto de implementaciones de ejercicios de "pwro" en Python.

Incluye Fibonacci, primos, factorial, combinaciones y algunos
algoritmos de ordenación. Este módulo se puede ejecutar como script
y también importarse desde otros ficheros.
"""

import random
import time


def fib_iterative(n):
    """Devuelve una lista con los primeros n términos de Fibonacci."""
    if n <= 0:
        return []
    seq = [0]
    if n == 1:
        return seq
    seq.append(1)
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq


def fib_recursive(n):
    """Calcula el n-ésimo término de Fibonacci de forma recursiva."""
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fib_recursive(n - 1) + fib_recursive(n - 2)


def is_prime(num):
    """Devuelve True si num es primo."""
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True


def sieve_primes(limit):
    """Genera todos los primos menores que limit usando la criba de Eratóstenes."""
    if limit <= 2:
        return []
    sieve = [True] * limit
    sieve[0] = sieve[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, limit, i):
                sieve[j] = False
    return [i for i, ispr in enumerate(sieve) if ispr]


def factorial(n):
    """Calcula el factorial de n de forma recursiva."""
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos")
    if n == 0:
        return 1
    return n * factorial(n - 1)


def combinations(n, k):
    """Calcula C(n, k) = n! / (k! * (n-k)!)."""
    if k < 0 or k > n:
        return 0
    return factorial(n) // (factorial(k) * factorial(n - k))


def bubble_sort(arr):
    a = arr.copy()
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


def insertion_sort(arr):
    a = arr.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


def selection_sort(arr):
    a = arr.copy()
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a


def random_list(size, maxval=1000):
    return [random.randint(0, maxval) for _ in range(size)]


def main_menu():
    """Menú interactivo simple por consola."""
    while True:
        print("\n--- Menú de algoritmos ---")
        print("1. Fibonacci iterativo")
        print("2. Fibonacci recursivo")
        print("3. Es primo?")
        print("4. Primos hasta límite (criba)")
        print("5. Factorial")
        print("6. Combinaciones")
        print("7. Ordenar lista aleatoria")
        print("0. Salir")
        choice = input("Elige una opción: ").strip()
        if choice == "0":
            break
        if choice == "1":
            n = int(input("n = "))
            print(fib_iterative(n))
        elif choice == "2":
            n = int(input("n = "))
            print(fib_recursive(n))
        elif choice == "3":
            num = int(input("n = "))
            print(is_prime(num))
        elif choice == "4":
            lim = int(input("límite = "))
            print(sieve_primes(lim))
        elif choice == "5":
            n = int(input("n = "))
            print(factorial(n))
        elif choice == "6":
            n = int(input("n = "))
            k = int(input("k = "))
            print(combinations(n, k))
        elif choice == "7":
            size = int(input("tamaño = "))
            arr = random_list(size)
            print("Lista original:", arr)
            print("Burbuja:", bubble_sort(arr))
            print("Inserción:", insertion_sort(arr))
            print("Selección:", selection_sort(arr))
        else:
            print("Opción no válida")


if __name__ == "__main__":
    main_menu()
