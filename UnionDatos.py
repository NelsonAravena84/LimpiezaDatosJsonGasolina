import json 
import pandas as pd 
import openpyxl

def LeyendoArchivos(NombreArchivo, NumeroArchivo):
    f = open(f'Datos\{NombreArchivo}{NumeroArchivo}.json', 'r')
    data = json.load(f)
    df = pd.json_normalize(data, record_path=["data"])
    return df

#Datos Gasolina 93
RegionMetropolitana93 = LeyendoArchivos("Metropolitana",93)
RegionMagallanes93 = LeyendoArchivos("Magallanes",93)
RegionValparaiso93 = LeyendoArchivos("Valparaiso",93)
RegionArica93 = LeyendoArchivos("Arica",93)

#Datos Gasolina 95
RegionMetropolitana95 = LeyendoArchivos("Metropolitana",95)
RegionMagallanes95 = LeyendoArchivos("Magallanes",95)
RegionValparaiso95 = LeyendoArchivos("Valparaiso",95)
RegionArica95 = LeyendoArchivos("Arica",95)

#Datos Gasolina 97
RegionMetropolitana97 = LeyendoArchivos("Metropolitana",97)
RegionMagallanes97 = LeyendoArchivos("Magallanes",97)
RegionValparaiso97 = LeyendoArchivos("Valparaiso",97)
RegionArica97 = LeyendoArchivos("Arica",97)

#Datos Diesel 
RegionMetropolitanaDiesel = LeyendoArchivos("Metropolitana","Diesel")
RegionMagallanesDiesel = LeyendoArchivos("Magallanes","Diesel")
RegionValparaisoDiesel = LeyendoArchivos("Valparaiso","Diesel")
RegionAricaDiesel = LeyendoArchivos("Arica","Diesel")

#print(RegionAricaDiesel)

def JuntandoDatos(Number,RegionMetropolitana,RegionMagallanes,RegionValparaiso,RegionArica):
    df = [RegionMetropolitana, RegionMagallanes,RegionValparaiso, RegionArica]
    tipoCombustible = (f'Gasolina {Number}')
    dataframeFinal= pd.concat(df)
    dataframeFinal['Tipo_combustible'] = tipoCombustible
    return dataframeFinal

dataframeGasolina93 = JuntandoDatos(93,RegionMetropolitana93,RegionMagallanes93,RegionValparaiso93,RegionArica93)
dataframeGasolina95 = JuntandoDatos(95,RegionMetropolitana95,RegionMagallanes95,RegionValparaiso95,RegionArica95)
dataframeGasolina97 = JuntandoDatos(97,RegionMetropolitana97,RegionMagallanes97,RegionValparaiso97,RegionArica97)
dataframeGasolinaDiesel = JuntandoDatos("Diesel",RegionMetropolitanaDiesel,RegionMagallanesDiesel,RegionValparaisoDiesel,RegionAricaDiesel)

#Funcion para juntar todos los dataframe 
def juntandoDataframe():
    DataframeFinal2 = [dataframeGasolina93,dataframeGasolina95,dataframeGasolina97,dataframeGasolinaDiesel]
    finalmente1 = pd.concat(DataframeFinal2)
    return finalmente1

FinalmenteDataframe = juntandoDataframe()
print(FinalmenteDataframe.tail())

FinalmenteDataframe.to_excel("Autput.xlsx")