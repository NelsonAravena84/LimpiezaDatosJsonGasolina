import json
import pandas as pd 
import openpyxl 

f = open('data.json', 'r')
data = json.load(f)
#print(data)

df = pd.json_normalize(data, record_path=["data"])
#contarCopec = df['marca_nombre'].value_counts().get('ARAMCO', 0)
#print(contarCopec)

#unique_names = df['marca_nombre'].unique()
#print(unique_names)

#limpieza de Datos para COPEC considerar que se esta usando combustible: Gasolina 97
#ademas que este dataset contiene los elementos de la región metropolitana 
#dfCopec = df.drop(['estacion_servicio_id','tipo_atencion','estacion_servicio_codigo','en_mantencion','comuna_nombre','comuna_id','estacion_direccion','region_nombre','region_id'], axis = 1)
#dfCopec = dfCopec[dfCopec['marca_nombre'] == 'COPEC']
#dfCopec = dfCopec.reset_index(drop=True) #importante que se actualice el indice del dataset


#limpieza de Datos para SHELL 
#dfShell = df.drop(['estacion_servicio_id','tipo_atencion','estacion_servicio_codigo','en_mantencion','comuna_nombre','comuna_id','estacion_direccion','region_nombre','region_id'], axis = 1)
#dfShell = dfShell[dfShell['marca_nombre'] == 'SHELL']
#dfShell = dfShell.reset_index(drop=True)


#limpieza de Datos para Petrobras 
#dfPetrobras = df.drop(['estacion_servicio_id','tipo_atencion','estacion_servicio_codigo','en_mantencion','comuna_nombre','comuna_id','estacion_direccion','region_nombre','region_id'], axis = 1)
#dfPetrobras = dfPetrobras[dfPetrobras['marca_nombre'] == 'PETROBRAS']
#dfPetrobras = dfPetrobras.reset_index(drop=True)


#limpieza de datos para JLC
#dfJLC = df.drop(['estacion_servicio_id','tipo_atencion','estacion_servicio_codigo','en_mantencion','comuna_nombre','comuna_id','estacion_direccion','region_nombre','region_id'], axis = 1)
#dfJLC = dfJLC[dfJLC['marca_nombre'] == 'JLC']
#dfJLC = dfJLC.reset_index(drop=True)

#frames = [dfCopec, dfJLC, dfPetrobras, dfShell]
#nuevodata = pd.concat(frames)
#nuevodata = nuevodata.reset_index(drop=True)

def LimpiezaDatos(dataframe, marca):
    eliminandocolumnas = dataframe.drop(['estacion_servicio_id','tipo_atencion','estacion_servicio_codigo','en_mantencion','comuna_nombre','comuna_id','estacion_direccion','region_nombre','region_id'], axis = 1)
    dataframemarca = eliminandocolumnas[eliminandocolumnas['marca_nombre'] == marca]
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
DataframeNuevoFinal.to_excel('output.xlsx', index=False)

print(DataframeNuevoFinal);




