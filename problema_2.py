import csv
from contextlib import redirect_stdout
from time import perf_counter

import matplotlib.pyplot as plt


def function_problem_2(n):
    """
    Complejidad temporal: O(n).
    """
    if n <= 1:
        return

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print("Sequence")
            break


def main():
    valores_n = [1, 10, 100, 1000, 10000, 100000, 1000000]
    resultados = []

    # 1. Ejecutar el programa y medir sus tiempos.
    # Las impresiones se guardan en un archivo.
    with open("salida_problema_2.txt", "w", encoding="utf-8") as salida:
        for n in valores_n:
            salida.write(f"--- Ejecución con n = {n} ---\n")
            salida.flush()

            with redirect_stdout(salida):
                inicio = perf_counter()

                function_problem_2(n)
                salida.flush()

                tiempo = perf_counter() - inicio

            resultados.append((n, tiempo))

    # 2. Mostrar la tabla en la terminal.
    print(f"{'Tamaño de input (n)':<22} | {'Tiempo (segundos)':>18}")
    print("-" * 45)

    for n, tiempo in resultados:
        print(f"{n:<22} | {tiempo:>18.9f}")

    # 3. Guardar la tabla en un archivo CSV.
    with open(
        "tabla_problema_2.csv",
        "w",
        newline="",
        encoding="utf-8",
    ) as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["n", "tiempo_segundos"])
        escritor.writerows(resultados)

    # 4. Crear y guardar la gráfica.
    entradas = [n for n, tiempo in resultados]
    tiempos = [tiempo for n, tiempo in resultados]

    fig, ax = plt.subplots(figsize=(9, 5))

    ax.plot(entradas, tiempos, marker="o", color="blue")
    ax.set_title("Problema 2: tamaño de input vs. tiempo")
    ax.set_xlabel("Tamaño de input (n)")
    ax.set_ylabel("Tiempo de ejecución (segundos)")
    ax.grid(True, alpha=0.3)
    ax.ticklabel_format(style="plain", axis="x")

    fig.tight_layout()
    fig.savefig("grafica_problema_2.png", dpi=200)
    plt.close(fig)

    print("\nArchivos generados:")
    print("- salida_problema_2.txt")
    print("- tabla_problema_2.csv")
    print("- grafica_problema_2.png")


if __name__ == "__main__":
    main()