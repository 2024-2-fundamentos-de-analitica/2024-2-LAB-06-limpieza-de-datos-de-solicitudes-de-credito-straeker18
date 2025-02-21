"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""
import os
import pandas as pd

def pregunta_01():
    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"

    """

    archivo_entrada = "files/input/solicitudes_de_credito.csv"
    archivo_salida = "files/output/solicitudes_de_credito.csv"

    # Cargar el archivo de entrada
    datos = pd.read_csv(archivo_entrada, sep=";", index_col=0)

    # Eliminar valores nulos
    datos.dropna(inplace=True)

    # Normalización de la columna 'sexo'
    datos["sexo"] = datos["sexo"].str.lower()

    # Normalización de la columna 'tipo_de_emprendimiento'
    datos["tipo_de_emprendimiento"] = datos["tipo_de_emprendimiento"].str.lower().str.strip()

    # Normalización y limpieza de 'barrio'
    datos["barrio"] = datos["barrio"].str.lower().str.replace("_", " ").str.replace("-", " ")

    # Normalización y limpieza de 'idea_negocio'
    datos["idea_negocio"] = datos["idea_negocio"].str.lower().str.replace("_", " ").str.replace("-", " ").str.strip()

    # Limpieza y conversión de 'monto_del_credito'
    datos["monto_del_credito"] = (
        datos["monto_del_credito"]
        .str.strip()
        .str.replace("$", "")
        .str.replace(",", "")
        .str.replace(".00", "")
    )
    datos["monto_del_credito"] = pd.to_numeric(datos["monto_del_credito"], errors="coerce")

    # Normalización y limpieza de 'línea_credito'
    datos["línea_credito"] = datos["línea_credito"].str.lower().str.replace("_", " ").str.replace("-", " ").str.strip()

    # Conversión de 'fecha_de_beneficio'
    datos["fecha_de_beneficio"] = pd.to_datetime(
        datos["fecha_de_beneficio"], format="%d/%m/%Y", errors="coerce"
    ).combine_first(pd.to_datetime(datos["fecha_de_beneficio"], format="%Y/%m/%d", errors="coerce"))

    # Conversión de 'comuna_ciudadano' a tipo entero
    datos["comuna_ciudadano"] = datos["comuna_ciudadano"].astype(int)

    # Eliminación de registros duplicados y nulos
    datos.drop_duplicates(inplace=True)
    datos.dropna(inplace=True)

    # Creación del directorio de salida si no existe
    os.makedirs(os.path.dirname(archivo_salida), exist_ok=True)

    # Guardar el archivo limpio
    datos.to_csv(archivo_salida, sep=";", index=False)