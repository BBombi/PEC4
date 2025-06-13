# Primero, importaremos las librerias de pandas, matplotlib,
# os y spicy.
import pandas as pd
import matplotlib.pyplot as plt
import os
# En este caso, también aprovecharemos la función smooth_curve creada en el
# apartado anterior:
from modules.smoothing import smooth_curve


# Definiremos una función que nos devuelva una lista con los periodos de sequía
# que se hayan dado en los últimos años.
def period_calc(df: pd.DataFrame, threshold: float = 60.0) -> list:
    """
    Detect drought periods based on whether the smoothed signal is below a
    threshold. Returns a list of periods as [start, end] in decimal format.

    Args:
        df: Pandas DataFrame
        threshold: float (0.0 to 1.0) to set up the threshold to consider the
        date as a drought period.

    Returns:
        Saves the plot into '/img'.
    """
    y, y_smooth = smooth_curve(df)

    # Creamos una copia del DataFrame para tener una variable local y no
    # alterar el original.
    df_temp = df.copy()
    # Ahora, le podemos añadir la variable y_smooth en el DF.
    df_temp["smoothed"] = y_smooth
    # Añadiremos también la columna "is_drought", que nos indicará si es sequía
    # o no. Lo haremos mediante la condición de que si la tendéncia es inferior
    # al 60% de la capacidad, se considerará como sequía (valor booleano True).
    df_temp["is_drought"] = df_temp["smoothed"] < threshold

    # Definimos variables locales
    periods = []
    period = False
    start = None

    # Y ahora, para cada periodo de sequía, determinaremos su inicio y su final
    for i in range(len(df_temp)):
        if df_temp.iloc[i]["is_drought"] and not period:
            start = df_temp.iloc[i]["dia_decimal"]
            period = True
        elif not df_temp.iloc[i]["is_drought"] and period:
            end = df_temp.iloc[i]["dia_decimal"]
            periods.append([round(start, 2), round(end, 2)])
            period = False

    # En caso que los datos muestren que sigue en periodo de sequía:
    if period:
        end = df_temp.iloc[-1]["dia_decimal"]
        periods.append([round(start, 2), round(end, 2)])

    return periods


# Por último, nos faltará crear el gráfico y guardarlo nuevamente.
def plot_drought(df: pd.DataFrame, periods: list = None):
    """
    Plotting and saving a graph showing both tendence and the original values,
    and also adding red shadding for the drought periods.

    Args:
        df: Pandas DataFrame
        periods: list of drought periods (starting and ending dates).

    Returns:
        Saves the plot into '/img'.
    """
    # Primero, definimos las variables que vamos a introducir en el gráfico:
    y, y_smooth = smooth_curve(df)

    # Ahora, especificamos el mismo tamaño que el anterior gráfico:
    plt.figure(figsize=(12, 8))
    # Mostramos los valores originales del volúmen de agua. Esta vez, deberemos
    # utilizar la fecha en formato decimal, pues los periodos de sequía están
    # expresados en dicho formato:
    plt.plot(df["dia_decimal"], y, color="blue", linewidth=1)
    # Creamos la linea de tendéncia suavizada.
    plt.plot(df["dia_decimal"],
             y_smooth,
             label="smoothed",
             color="orange",
             linewidth=5
             )

    # Obtenemos los periodos de sequía con la función period_calc():
    periods = period_calc(df)

    # Por último, añadimos los periodos de sequía en color rojo:
    if periods:
        for start, end in periods:
            # La función axvspan sombrea una franja vertical en un gráfico.
            # En este caso, en los periodos de sequía.
            plt.axvspan(start,
                        end,
                        color='red',
                        alpha=0.2,
                        label='Sequía' if start == periods[0][0] else "")

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

    # Finalmente, guardaremos el archivo en la misma localización que el
    # anterior:
    output_path: str = "img/labaells_drought_Borja_Bombi.png"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path)
    plt.close()
    print(f"Gráfico guardado en: {output_path}")
