## Problema 1 Parte b

import csv
import multiprocessing as mp
from time import perf_counter

import matplotlib.pyplot as plt


def function_problem_1(n):
    """
    Complejidad temporal: O(n² log n).
    """
    counter = 0

    for i in range(n // 2, n + 1):
        for j in range(1, n - n // 2 + 1):
            k = 1

            while k <= n:
                counter += 1
                k *= 2


def medir_tiempo(n, conexion):
    """Mide únicamente la ejecución de la función."""
    inicio = perf_counter()

    function_problem_1(n)

    tiempo = perf_counter() - inicio
    conexion.send(tiempo)
    conexion.close()


def ejecutar_prueba(n, limite):
    """Ejecuta la medición en un proceso que podemos detener."""
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

    print(f"{'Tamaño de input (n)':<22} | Tiempo de ejecución")
    print("-" * 65)

    for n in valores_n:
        tiempo = ejecutar_prueba(n, limite_segundos)
        resultados.append((n, tiempo))

        if tiempo is None:
            texto = f"No terminó en el límite de {limite_segundos} s"
        else:
            texto = f"{tiempo:.9f} s"

        print(f"{n:<22} | {texto}", flush=True)

    with open(
        "tabla_problema_1.csv",
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

    completados = [
        (n, tiempo)
        for n, tiempo in resultados
        if tiempo is not None
    ]

    fig, ax = plt.subplots(figsize=(9, 5))

    if completados:
        entradas, tiempos = zip(*completados)
        ax.plot(entradas, tiempos, marker="o")

        ax.set_xscale("log")
        ax.set_yscale("log")

    ax.set_title("Problema 1: tamaño de input vs. tiempo")
    ax.set_xlabel("Tamaño de input (n), escala logarítmica")
    ax.set_ylabel("Tiempo (segundos), escala logarítmica")
    ax.grid(True, which="both", alpha=0.3)

    fig.text(
        0.5,
        0.02,
        "Solo se muestran pruebas completadas. "
        "Las interrumpidas se registran en la tabla.",
        ha="center",
        fontsize=9,
    )

    fig.tight_layout(rect=(0, 0.06, 1, 1))
    fig.savefig("grafica_problema_1.png", dpi=200)
    plt.close(fig)

    print("\nArchivos generados:")
    print("- tabla_problema_1.csv")
    print("- grafica_problema_1.png")


if __name__ == "__main__":
    mp.freeze_support()
    main()