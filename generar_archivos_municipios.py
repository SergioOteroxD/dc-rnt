import pandas as pd
import os

def crear_archivos_por_municipio(df, departamento):
    # Filtrar por departamento
    df_departamento = df[(df['DEPARTAMENTO'].str.upper() == departamento.upper()) & 
                    (df['CATEGORIA'] == 'ESTABLECIMIENTOS DE ALOJAMIENTO TURÍSTICO')]
    
    # Obtener lista única de municipios del departamento
    municipios = df_departamento['MUNICIPIO'].unique()
    
    # Crear directorio para los archivos si no existe
    output_dir = f"output/municipios_{departamento}"
    os.makedirs(output_dir, exist_ok=True)
    
    # Generar archivo para cada municipio
    for municipio in municipios:
        # Filtrar datos del municipio
        df_municipio = df_departamento[df_departamento['MUNICIPIO'] == municipio]
        
        # Crear nombre de archivo
        nombre_archivo = f"{departamento}-{municipio}.csv"
        ruta_archivo = os.path.join(output_dir, nombre_archivo)
        
        # Guardar archivo
        df_municipio.to_csv(ruta_archivo, index=False)
        print(f"Archivo creado: {nombre_archivo}")

if __name__ == "__main__":
    # Leer archivo principal
    archivo_csv = "./Registro_Nacional_de_Turismo_-_RNT_20250328.csv"
    df = pd.read_csv(archivo_csv)
    
    # Mostrar departamentos disponibles
    print("\nDepartamentos disponibles:")
    print(sorted(df['DEPARTAMENTO'].unique()))
    
    # Solicitar departamento
    departamento = input("\nIngrese el nombre del departamento: ")
    
    # Crear archivos
    crear_archivos_por_municipio(df, departamento)