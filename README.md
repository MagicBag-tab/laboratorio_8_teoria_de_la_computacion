# Laboratorio 8 — Teoría de la Computación

**Estudiante:** Sarah Rachel Estrada Bonilla

## Descripción

Este laboratorio analiza la complejidad temporal de algoritmos mediante
procedimientos matemáticos y mediciones de tiempo de ejecución en Python.

Incluye:

- Problemas 1, 2 y 3: implementación, análisis de complejidad y medición
  de tiempos con tablas y gráficas.
- Problema 4: análisis del mejor caso, caso promedio y peor caso de
  búsqueda lineal, búsqueda binaria y Quick Sort.
- Problema 5: justificación de enunciados sobre notación asintótica
  y análisis de un programa que construye subtuplas.

## Organización del repositorio

La estructura utilizada es:

    Laboratorio_8/
    ├── README.md
    ├── requirements.txt
    ├── problema_1.py
    ├── problema_2.py
    ├── problema_3.py
    ├── respuestas/
    │   └── respuestas.pdf
    └── resultados/
        ├── tabla_problema_1.csv
        ├── grafica_problema_1.png
        ├── tabla_problema_2.csv
        ├── grafica_problema_2.png
        ├── tabla_problema_3.csv
        └── grafica_problema_3.png

## Requisitos

- Python 3.
- Matplotlib.

El archivo `requirements.txt` debe contener:

    matplotlib

## Instalación y ejecución

1. Descargar o clonar este repositorio.
2. Abrir una terminal en la carpeta del proyecto.
3. Instalar las dependencias:

       python -m pip install -r requirements.txt

4. Ejecutar cada programa por separado:

       python problema_1.py
       python problema_2.py
       python problema_3.py

Si el sistema utiliza el comando `python3`, sustituir `python` por
`python3` en las instrucciones anteriores.

Los programas se ejecutan como archivos `.py` desde la terminal.
Los problemas 1 y 3 utilizan procesos separados para controlar
la duración de las pruebas.

## Medición de tiempos

Los tamaños de entrada solicitados son:

    n = 1, 10, 100, 1000, 10000, 100000, 1000000

Se utiliza `time.perf_counter()` para medir el tiempo transcurrido
durante la ejecución de cada función. La generación de tablas y
gráficas queda fuera de la medición.

Cada programa genera una tabla CSV y una gráfica PNG en la carpeta
desde donde se ejecuta. Para mantener la organización del repositorio,
estos archivos se pueden mover posteriormente a `resultados/`.

### Problema 1

El programa contiene dos ciclos con crecimiento lineal y un ciclo
interno que duplica su variable en cada iteración.

**Complejidad temporal:** O(n² log n).

Las entradas grandes requieren una cantidad considerable de operaciones.
La versión con límite de tiempo registra las pruebas interrumpidas
sin asignarles un tiempo de ejecución completo.

### Problema 2

El ciclo interno termina después de su primera iteración debido
a la instrucción `break`.

**Complejidad temporal:** O(n).

Las impresiones se redirigen a `salida_problema_2.txt` para evitar
saturar la terminal. La medición incluye las escrituras y el vaciado
del búfer mediante `flush()`.

Para `n = 1`, la función retorna inmediatamente sin imprimir.

### Problema 3

El ciclo externo realiza aproximadamente n/3 iteraciones y el interno
aproximadamente n/4.

**Complejidad temporal:** O(n²).

Las impresiones se redirigen a `os.devnull`, que descarta la salida
sin almacenarla en un archivo. Se ejecuta cada llamada a `print`,
pero no se mide la visualización de texto en la terminal.

El código permite configurar un límite por prueba mediante
`limite_segundos`. Si una ejecución no termina dentro del límite,
se registra como interrumpida y se excluye de la gráfica.

Para `n = 1`, el ciclo externo no se ejecuta.

### Interpretación de resultados

- Los tiempos dependen del equipo y de su carga de trabajo.
- Las pruebas interrumpidas no representan mediciones completas.
- Las gráficas muestran únicamente ejecuciones completadas.
- Los problemas 2 y 3 utilizan destinos de salida diferentes;
  sus tiempos no deben compararse como si las condiciones fueran iguales.
- Las estimaciones teóricas deben distinguirse de los tiempos medidos.

## Respuestas escritas

El documento [respuestas.pdf](respuestas/respuestas.pdf) contiene:

- Los procedimientos de complejidad de los problemas 1, 2 y 3.
- Las tablas, gráficas y observaciones de las mediciones.
- El análisis de los casos de búsqueda lineal, búsqueda binaria
  y Quick Sort del problema 4.
- Las respuestas y justificaciones del problema 5.

## Video de presentación

[Ver el video del Laboratorio 8 en YouTube](https://youtu.be/CW-OJ-NstBA)