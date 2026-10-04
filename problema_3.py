import csv
import multiprocessing as mp
import os
from contextlib import redirect_stdout
from time import perf_counter

import matplotlib.pyplot as plt


def function_problem_3(n):
    """
    Complejidad temporal: O(n²).
    """
    for i in range(1, n // 3 + 1):
        for j in range(1, n + 1, 4):
            print("Sequence")


def medir_tiempo(n, conexion):
    """Mide la función descartando su salida."""
    with open(os.devnull, "w", encoding="utf-8") as salida:
        with redirect_stdout(salida):
            inicio = perf_counter()

            function_problem_3(n)
            salida.flush()

            tiempo = perf_counter() - inicio

    conexion.send(tiempo)
    conexion.close()


def ejecutar_prueba(n, limite):
    """Detiene la prueba si supera el tiempo permitido."""
    receptor, emisor = mp.Pipe(duplex=False)

    proceso = mp.Process(
        target=medir_tiempo,
        args=(n, emisor),
    )

    proceso.start()
    emisor.close()
    proceso.join(timeout=limite)

    if proceso.is_alive():
        proceso.terminate()
        proceso.join()
        receptor.close()
        proceso.close()
        return None

    if proceso.exitcode != 0 or not receptor.poll():
        receptor.close()
        proceso.close()
        raise RuntimeError(f"La prueba con n={n} falló.")

    tiempo = receptor.recv()
    receptor.close()
    proceso.close()

    return tiempo


def main():
    valores_n = [1, 10, 100, 1000, 10000, 100000, 1000000]
    limite_segundos = 30
    resultados = []

    # 1. Medir tiempos y mostrar la tabla.
    print(f"{'Tamaño de input (n)':<22} | Tiempo de ejecución")
    print("-" * 70)

    for n in valores_n:
        tiempo = ejecutar_prueba(n, limite_segundos)
        resultados.append((n, tiempo))

        if tiempo is None:
            texto = f"No terminó en el límite de {limite_segundos} s"
        else:
            texto = f"{tiempo:.9f} s"

        print(f"{n:<22} | {texto}", flush=True)

    # 2. Guardar los resultados en CSV.
    with open(
        "tabla_problema_3.csv",
        "w",
        newline="",
        encoding="utf-8",
    ) as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["n", "tiempo_segundos", "estado"])

        for n, tiempo in resultados:
            if tiempo is None:
                escritor.writerow([
                    n,
                    "",
                    f"No terminó en el límite de {limite_segundos} s",
                ])
            else:
                escritor.writerow([n, tiempo, "Completado"])

    # 3. Graficar únicamente las pruebas completadas.
    completados = [
        (n, tiempo)
        for n, tiempo in resultados
        if tiempo is not None
    ]

    fig, ax = plt.subplots(figsize=(9, 5))

    if completados:
        entradas, tiempos = zip(*completados)
        ax.plot(entradas, tiempos, marker="o", color="green")

    ax.set_title("Problema 3: tamaño de input vs. tiempo")
    ax.set_xlabel("Tamaño de input (n)")
    ax.set_ylabel("Tiempo de ejecución (segundos)")
    ax.grid(True, alpha=0.3)
    ax.ticklabel_format(style="plain", axis="x")

    fig.text(
        0.5,
        0.02,
        "Solo se muestran pruebas completadas. "
        "Salida descartada mediante os.devnull.",
        ha="center",
        fontsize=9,
    )

    fig.tight_layout(rect=(0, 0.06, 1, 1))
    fig.savefig("grafica_problema_3.png", dpi=200)
    plt.close(fig)

    print("\nArchivos generados:")
    print("- tabla_problema_3.csv")
    print("- grafica_problema_3.png")


if __name__ == "__main__":
    mp.freeze_support()
    main()