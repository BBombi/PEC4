"""
In this module, we'll convert and sort dates, along with plotting the evolution
of the water level through time.
"""
# Importamos Pandas, matplotlib, os y datetimme:
import pandas as pd
import matplotlib.pyplot as plt
import os
import datetime as dt


# Primero, convertimos la columna "dia" en formato Datetime
def convert_to_datetime(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert column 'dia' into datetime64.

    Args:
        df: Pandas DataFrame

    Returns:
        DataFrame: Convert column into a 'datetime' format.
    """
    df["dia"] = pd.to_datetime(df["dia"], errors="coerce", dayfirst=True)
    return df


def get_row_info(df: pd.DataFrame):
    """
    Get the number of rows in the DataFrame.

    Args:
        df: Pandas DataFrame

    Returns:
        Prints number of rows at the DataFrame.
    """
    # Mostramos el número de filas del DataFrame:
    print(f"\nNúmero de filas: {len(df)}")


# Ordenamos
def sort_date(df: pd.DataFrame) -> pd.DataFrame:
    """
    Sort and then show date info.

    Args:
        df: Pandas DataFrame

    Returns:
        Prints most recent and oldest dates.
        DataFrame: Sorted by date in ascending order.
    """
    # Primero, ordenamos las fechas de forma ascendente.
    df = df.sort_values(by="dia", ascending=True)
    # Mostramos las fechas más antigua y más reciente del DF:
    print(f"Fecha más antigua: {df['dia'].min().date()}")
    print(f"Fecha más reciente: {df['dia'].max().date()}")
    return df


# Definimos la función toYearFraction:
def toYearFraction(date: dt) -> float:
    """
    Convert a 'datetime' date to its decimal year equivalent.

    Args:
        date: Date on a 'datetime' format.

    Returns:
        float: Date as a fraction of the year's format.
    """
    # Primero extraemos el número ordinal de año de estudio:
    start_of_year = dt.date(date.year, 1, 1).toordinal()
    # Después calculamos el número de días que tiene el año de estudio:
    year_length = dt.date(date.year + 1, 1, 1).toordinal() - start_of_year
    # Y por último, devolvemos el valor en tipo float de la suma del año
    # de estudio, más la fracción que representan los días que han pasado
    # desde el uno de enero hasta la fecha de estudio.
    return round(date.year + float(date.toordinal() - start_of_year) / year_length, 2)


# Aplicamos la función toYearFraction para crear una nueva columna:
def add_fraction_column(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create a column named 'dia_decimal' from column 'dia',
    where we express the date as a float number.

    Args:
        df: Pandas DataFrame

    Returns:
        DataFrame: creates a new column with date expressed as fraction of
        the year.
    """
    df["dia_decimal"] = df["dia"].apply(toYearFraction)
    return df


# Creamos una nueva función que genere un gráfico del volúmen del embalse
# de La Baells en función del tiempo, y lo guardamos en la carpeta "img"
def plot_vol(df: pd.DataFrame):
    """
    Generate and save a plot of the reservoir volume as a function of time.

    Args:
        df: Pandas DataFrame

    Returns:
        Saves the plot into '/img'.
    """
    # Primero, definiremos el tamaño del gráfico.
    plt.figure(figsize=(12, 8))
    # Le pedimos que nos muestre la evolución del volumen del embalse
    # en función del tiempo.
    plt.plot(df["dia"], df["nivell_perc"], label="volum", color="blue")
    # Agregamos una etiqueta al eje de las X:
    plt.xlabel("Tiempo")
    # Y ahora al de las Y:
    plt.ylabel("Porcentaje")
    # Agregamos el título al gráfico:
    plt.title("Embassament de La Baells")
    # Y añadimos el subtítulo con mi nombre:
    plt.suptitle("Alumno: Borja Bombí", fontsize=10, y=0.91)
    # Ajustamos el gráfico automáticamente usando tight_layout()
    plt.tight_layout()

    # Por último, utilizaremos la biblioteca "os" para crear una carpeta
    # llamada "img" en caso de que sea necesario.
    # Primero, determinamos el path, y el nombre del archivo:
    output_path = "img/"
    file_name = "labaells_Borja_Bombi.png"
    # Creamos la carpeta.
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    # Y por último, guardamos el archivo.
    plt.savefig(os.path.join(output_path, file_name))
    plt.close()
    print(f"Gráfico guardado en la carpeta: {output_path}")
