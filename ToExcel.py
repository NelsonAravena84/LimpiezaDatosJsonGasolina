import json
import pandas as pd 
import openpyxl 

f = open('data.json', 'r')
data = json.load(f)
#print(data)

df = pd.json_normalize(data, record_path=["data"])


def LimpiezaDatos(dataframe, marca):
    #eliminación de columnas no deseadas
    eliminandocolumnas = dataframe.drop(['estacion_servicio_id','tipo_atencion','estacion_servicio_codigo','en_mantencion','comuna_nombre','comuna_id','estacion_direccion','region_nombre','region_id','combustible_id','zona_geografica_id'], axis = 1)
    dataframemarca = eliminandocolumnas[eliminandocolumnas['marca_nombre'] == marca].copy()

    #conversión del tipo de dato
    dataframemarca['zonas_geografica_nombre'] = dataframemarca['zonas_geografica_nombre'].convert_dtypes()
    dataframemarca['marca_nombre'] = dataframemarca['marca_nombre'].convert_dtypes()
    dataframemarca['combustible_precio'] = dataframemarca['combustible_precio'].astype(float)


    #OPERACIONES ARITMETICAS 
    Valores_sumados = dataframemarca['combustible_precio'].sum()

    #división por la cantidad de datos 
    Media_promedio = Valores_sumados // len(dataframemarca)

    #asignar al dataframe
    dataframemarca['combustible_precio'] = Media_promedio
    dataframemarca = dataframemarca.iloc[:1]

    #se resetea el index
    dataframemarca = dataframemarca.reset_index(drop=True)

    return (dataframemarca)


def unionDatos(DatosShell, DatosCopec, DatosPetrobras, DatosJLC):
    frames = [DatosShell,DatosCopec, DatosPetrobras, DatosJLC]
    dataframefinal = pd.concat(frames)
    dataframefinal = dataframefinal.reset_index(drop=True)

    return (dataframefinal);


#PRIMERA FUNCIÓN
DatosShell = LimpiezaDatos(df, "SHELL");
DatosCopec = LimpiezaDatos(df, "COPEC"); 
DatosPetrobras = LimpiezaDatos (df, "PETROBRAS");
DatosJLC = LimpiezaDatos (df, "JLC");


#SEGUNDA FUNCIÓN
DataframeNuevoFinal = unionDatos(DatosShell, DatosCopec, DatosPetrobras, DatosJLC);
DataframeNuevoFinal.to_csv('GasolinaData.csv', index=False)

print(DataframeNuevoFinal.dtypes)

print(DataframeNuevoFinal.head());




