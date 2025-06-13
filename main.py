# Primero, importaremos las funciones anteriormente creadas en los scripts
# de los distintos ejercicios:
from modules.loader import (
    load_dataset,
    show_head,
    show_columns,
    show_info
    )
from modules.cleaning import (
    rename_columns,
    show_unique_swamps,
    clean_darnius_name,
    baells_filter
)
from modules.timing import (
    convert_to_datetime,
    get_row_info,
    sort_date,
    add_fraction_column,
    plot_vol,
)
from modules.smoothing import plot_graph
from modules.drought_periods import (
    period_calc,
    plot_drought
)
# También deberemos importar la libreria argparse para poder ejecutar el
# script por módulos, así como Pandas para cargar los DF en cada paso.
import argparse


# Definimos el script ptincipal:
def main(ex: int = None):
    """
    Main script for the project, but splitting it into exercises.

    For choosing an exercise, just type '-ex' followed by the number
    of the exercise you're looking for. The script will then execute
    the program until reaches the end of the selected exercise.
    """
    # Primero, definimos un df común para todos.
    df = None

    if ex is None or ex >= 1:
        print("\nExecuting exercise 1...")

        # Primero cargamos los datos utilizando load_dataset():
        print("\nCargando datos...")
        df = load_dataset()

        # Ahora utilizamos show_head() para mostrar las primeras 5 filas:
        print("\nPrimeras 5 filas del DataFrame:")
        show_head(df)

        # Utilizamos show_columns() para mostrar las columnas:
        print("\nColumnas del DataFrame:")
        show_columns(df)

        # Mostramos la información del DataFrame con show_info():
        print("\nMostrando información del DataFrame:")
        show_info(df)

    if ex is None or ex >= 2:
        print("\nExecuting exercise 2...")

        # Ahora, renombramos las columnas:
        print("\nRenombrando columnas:")
        df = rename_columns(df)
        print(df.columns)

        # Mostramos el nombre de cada uno de los embalses
        print("\nMostrando nombres de embalses:")
        show_unique_swamps(df)

        # Cambiamos el nombre al embalse de Darnius
        print("\nLimpiando nombres de embalses:")
        df = clean_darnius_name(df)
        show_unique_swamps(df)

        # Por último, filtramos los datos para "La Baells"
        print("\nFiltrando datos para 'La Baells':")
        df_baells = baells_filter(df)
        print(df_baells.head())

    if ex is None or ex >= 3:
        print("\nExecuting exercise 3...")

        # Hacemos el cambio de la columna "dia" a tipo datetime:
        print("\nConvertimos la columna 'dia' a datetime:")
        df_baells = convert_to_datetime(df_baells)

        # Mostramos el número de filas totales.
        print("\nMostramos información del número de filas:")
        get_row_info(df_baells)

        # Ordenamos por fecha y mostramos la más antigua y la más reciente:
        print("\nOrdenando y mostramos información de fechas:")
        df_baells = sort_date(df_baells)

        # Creamos la columna "dia_decimal" utilizando la función
        # toYearFraction()
        print("\nCreamos la columna 'dia_decimal':")
        df_baells = add_fraction_column(df_baells)
        print(df_baells[["dia", "dia_decimal"]].head())

        # Y por último, generamos y guardamos el gráfico de la evolución
        # del volumen de agua de La Baells.
        print("\nGeneramos un gráfico de evolución del volumen de agua:")
        plot_vol(df_baells)

    if ex is None or ex >= 4:
        print("\nExecuting exercise 4...")

        # Creamos un nuevo gráfico comparando la tendencia con la realidad:
        print("\nGeneramos de nuevo el gráfico, añadiendo la tendéncia:")
        plot_graph(df_baells)

    if ex is None or ex >= 5:
        print("\nExecuting exercise 5...")

        print("\nCalculando periodos de sequía:\n")
        periods = period_calc(df_baells)
        for i, period in enumerate(periods):
            print(f"\tPeriodo {i+1}: desde {period[0]} a {period[1]}")

        # Generamos un nuevo gráfico, añadiendo los periodos de sequía:
        print("\nAñadiendo los periodos de sequía al gráfico.")
        plot_drought(df_baells)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="""
    Main script for the project, but splitting it into exercises.

    For choosing an exercise, just type '-ex' followed by the number
    of the exercise you're looking for. The script will then execute
    the program until reaches the end of the selected exercise.
    """)
    parser.add_argument("-ex", type=int, help="Exercices 1 to 5")
    args = parser.parse_args()
    main(args.ex)
