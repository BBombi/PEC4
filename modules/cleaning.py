"""
Module for cleaning and filtering data from dataset.
"""
# De nuevo, importamos Pandas y también re (expresiones regulares)
import pandas as pd
import re

# Establecemos un diccionario con los nombres de las columnas que queremos
# cambiar, siendo el nombre de la columna antigua la clave, y la de la
# nueva el valor.
col_rename_dict = {
    "Dia": "dia",
    "Estació": "estacio",
    "Nivell absolut (msnm)": "nivell_msnm",
    "Percentatge volum embassat (%)": "nivell_perc",
    "Volum embassat (hm3)": "volum"
}


# Definiremos una función para que haga el cambio de nombre de las columnas:
def rename_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Rename the column name from the original DataFrame.

    Args:
        Pandas DataFrame.

    Returns:
        Renames DataFrame columns.
    """
    return df.rename(columns=col_rename_dict)


# Mostramos todos los nombres de los embalses:
def show_unique_swamps(df: pd.DataFrame):
    """
    Show the unique names from the swamps.

    Args:
        Pandas DataFrame.

    Returns:
        Prints unique swamps names.
    """
    print(df["estacio"].unique())


# Renombramos el pantano de Darnius Boadella:
def clean_darnius_name(df: pd.DataFrame) -> pd.DataFrame:
    """
    Rename Darnius Boadella swamp by removing all the brackets,
    and getting rid of 'Embassament de' from the name.

    Args:
        Pandas DataFrame

    Returns:
        Returns DataFrame with modified value for 'Darnius
        Boadella' name.
    """
    def clean(name):
        # Primero eliminamos "Embassament de"
        name = re.sub(r"Embassament de", "", name)
        # Ahora, de "(Darnius)", pero lo deberemos hacer de
        # una vez para no tener "Darnius" por duplicado.
        name = re.sub(r"\s*\(Darnius\)", "", name)
        # Por último, eliminamos los espacios que puedan haber
        # al principio y al final.
        return name.strip()

    # Para poder filtrar únicamente por el de Darnius Boadella,
    # creamos una "máscara"
    mask = df['estacio'].str.contains('Darnius Boadella')

    # Aplicando esta máscara, únicamente haremos los cambios en
    # el pantano objetivo.
    df.loc[mask, "estacio"] = df.loc[mask, "estacio"].apply(clean)
    return df


# Por último, definiremos una función para filtrar únicamente
# los datos del pantà de la Baells.
def baells_filter(df: pd.DataFrame) -> pd.DataFrame:
    """
    Filter the DataFrame to keep only the data from La Baells' swamp.

    Args:
        Pandas DataFrame

    Returns:
        New DataFrame containing only 'La Baells' swamp data.
    """
    return df[df["estacio"] == "Embassament de la Baells (Cercs)"].copy()
