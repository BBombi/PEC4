# Primero, importaremos las librerias de pandas, matplotlib,
# os y spicy.
import pandas as pd
import matplotlib.pyplot as plt
import os
from scipy.signal import savgol_filter
import numpy as np


# Primero, definimos la función para suavizar la curva de tendéncia:
def smooth_curve(df: pd.DataFrame) -> np.ndarray:
    """
    Calculates and smooths volume's trend signal and return both
    original and new smoother arrays.

    Args:
        df: Pandas DataFrame

    Returns:
        array 1: Original values.
        array 2: Smoothed trend signal.
    """
    # Definimos los valores que queremos suavizar.
    y = df["nivell_perc"].values

    # Nos aseguramos de que window_length sea mayor que el tamaño de la
    # variable:
    window_length = 1500 if len(y) > 1500 else len(y)

    # Hacemos que la función savgol_filter() nos suavice la linea de
    # tendéncia, y en caso de no poderse aplicar, nos devuelva un error:
    try:
        y_smooth = savgol_filter(y, window_length=window_length, polyorder=3)
    except ValueError as e:
        print(f"Unable to smooth: {e}")
        return
    return y, y_smooth


# Ahora creamos la función que nos devuelva el gráfico:
def plot_graph(df: pd.DataFrame):
    """
    Plotting and saving a graph showing both tendence and the original values.

    Args:
        df: Pandas DataFrame

    Returns:
        Saves the plot into '/img'.
    """
    # Primero, definimos las variables que vamos a introducir en el gráfico:
    y, y_smooth = smooth_curve(df)

    # Ahora, especificamos el mismo tamaño que el anterior gráfico:
    plt.figure(figsize=(12, 8))
    # Mostramos los valores originales del volúmen de agua:
    plt.plot(df["dia"], y, color="blue", linewidth=1)
    # Y ahora creamos la linea de tendéncia suavizada. En este caso, añadiremos
    # una etiqueta y aumentaremos el grosor del trazado.
    plt.plot(df["dia"],
             y_smooth,
             label="smoothed",
             color="orange",
             linewidth=5
             )
    # Agregamos una etiqueta al eje de las X:
    plt.xlabel("Tiempo")
    # Y ahora al de las Y:
    plt.ylabel("Porcentaje")
    # Agregamos el título al gráfico:
    plt.title("Embassament de La Baells")
    # Y añadimos el subtítulo con mi nombre:
    plt.suptitle("Alumno: Borja Bombí", fontsize=10, y=0.91)
    # Colocamos la etiqueta de "smooth" al centro y abajo del gráfico:
    plt.legend(loc='lower center')
    # Ajustamos el gráfico automáticamente usando tight_layout()
    plt.tight_layout()

    # Finalmente, guardaremos el gráfico en la misma localización que el
    # anterior:
    output_path: str = "img/labaells_smoothed_Borja_Bombi.png"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path)
    plt.close()
    print(f"Gráfico guardado en: {output_path}")
