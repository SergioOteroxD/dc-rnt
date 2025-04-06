import pandas as pd

def leer_negocios(archivo_csv):
    try:
        # Leer el archivo CSV
        df = pd.read_csv(archivo_csv)
        
        # Mostrar los primeros registros
        print("\nPrimeros registros del archivo:")
        print(df.head())
        
        # Mostrar información básica del dataset
        print("\nInformación del dataset:")
        print(df.info())
        
        return df
    
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {archivo_csv}")
    except Exception as e:
        print(f"Error al leer el archivo: {str(e)}")
def filtrar_por_ubicacion(df, departamento=None, municipio=None, categorias=None):
    df_filtrado = df.copy()
    
    if departamento:
        df_filtrado = df_filtrado[df_filtrado['DEPARTAMENTO'].str.upper() == departamento.upper()] # BOLIVAR
    
    if municipio:
        df_filtrado = df_filtrado[df_filtrado['MUNICIPIO'].str.upper() == municipio.upper()] # CARTAGENA
    
    if categorias:
        df_filtrado = df_filtrado[df_filtrado['CATEGORIA'].str.upper().isin([cat.upper() for cat in categorias])] # ESTABLECIMIENTOS DE ALOJAMIENTO TURÍSTICO, VIVIENDAS TURÍSTICAS
    
    return df_filtrado
if __name__ == "__main__":
    # Reemplaza 'negocios.csv' con el nombre de tu archivo CSV
    archivo_csv = "./Registro_Nacional_de_Turismo_-_RNT_20250328.csv"
    df_negocios = leer_negocios(archivo_csv)
    departamento = input("Ingrese el departamento (o presione Enter para ver todos): ")
    municipio = input("Ingrese el municipio (o presione Enter para ver todos): ")

    # Input multiple categories
    print("\nIngrese las categorías separadas por coma (o presione Enter para ver todas)")
    print("Ejemplo: HOTEL, HOSTAL, APARTAHOTEL")
    categorias_input = input("Categorías: ")
    
    categorias = [cat.strip() for cat in categorias_input.split(',')] if categorias_input else None
    
    resultados = filtrar_por_ubicacion(df_negocios, departamento, municipio,categorias)
    print("\nResultados del filtro:")
    print(
    resultados
    [
        [
            'RAZON_SOCIAL_ESTABLECIMIENTO', 
            'DEPARTAMENTO', 
            'MUNICIPIO', 
            'CATEGORIA', 
            'SUB_CATEGORIA', 
            'CORREO_ESTABLECIMIENTO',
            'HABITACIONES',
            'CAMAS',
        ]
    ])