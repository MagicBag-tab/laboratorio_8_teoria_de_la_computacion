## LABORATORIO 8

## Función del Problema 1

def function_problem_1(n):
    """
    Su complejidad es: O(n² log n).
    Ver procedimiento en la carpeta de respuestas.
    """
    counter = 0

    for i in range(n // 2, n + 1):
        for j in range(1, n - n // 2 + 1):
            k = 1
            while k <= n:
                counter += 1
                k *= 2


## Función del Problema 2

def function_problem_2(n):
    """
    Su complejidad es: O(n).
    Ver procedimiento en la carpeta de respuestas.
    """
    if n <= 1:
        return

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print("Sequence")
            break


## Función del Problema 3

def function_problem_3(n):
    """
    Su complejidad es: O(n²).
    Ver procedimiento en la carpeta de respuestas.
    """
    for i in range(1, n // 3 + 1):
        for j in range(1, n + 1, 4):
            print("Sequence")