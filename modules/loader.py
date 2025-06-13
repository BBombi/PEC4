"""
Module for loading and showing info from dataset (embalses).
"""
# Primero, importamos las librerias de Pandas i de os
import pandas as pd

# establecemos la URL de donde exportaremos el dataset.
data_url = "https://analisi.transparenciacatalunya.cat/api/views/gn9e-3qhr/rows.csv?accessType=DOWNLOAD"


# Creamos la función que cargue dicho Dataset en un pd.DataFrame:
def load_dataset() -> pd.DataFrame:
    """
    Load the dataset from la URL as a Pandas DataFrame.

    Args:
        None

    Returns:
        df: Pandas DataFrame
    """
    df = pd.read_csv(data_url)
    return df


# Creamos la función que muestre las 5 primeras filas del df:
def show_head(df: pd.DataFrame):
    """
    Showing first rows from the DataFrame.

    Args:
        df: Pandas DataFrame

    Returns:
        Prints first 5 rows from the DataFrame
    """
    # Al contrario de en los Jupyter Notebooks, deberemos
    # especificar el "print()" para que lo muestre en pantalla.
    print(df.head())


# Ahora, mostraremos el nombre de las columnas:
def show_columns(df: pd.DataFrame):
    """
    Showing column names from DataFrame.

    Args:
        df: Pandas DataFrame

    Returns:
        Prints name of DataFrame's columns.
    """
    print(df.columns)


# Mostraremos la información del DF:
def show_info(df):
    """
    Showing info from DataFrame.

    Args:
        df: Pandas DataFrame

    Returns:
        Prints information from DataFrame
    """
    df.info()
