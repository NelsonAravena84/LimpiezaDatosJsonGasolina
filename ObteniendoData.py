import requests 
import json 

#función para obtener datos gasolina 95
def ObtenciónDatos(numeroEndpoint, nombreArchivo):
    url = (f"https://api.bencinaenlinea.cl/api/estaciones/precios_combustibles/3,11/reporte_comunal?cod_region%5B%5D={numeroEndpoint}")
    token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOi8vYXBpLmNuZS5jbC9hcGkvbG9naW4iLCJpYXQiOjE3MzY2MjM0MzQsImV4cCI6MTczNjYyNzAzNCwibmJmIjoxNzM2NjIzNDM0LCJqdGkiOiJibWpoTWM5OHN6U3h4R1ZTIiwic3ViIjoiMjU0MyIsInBydiI6IjIzYmQ1Yzg5NDlmNjAwYWRiMzllNzAxYzQwMDg3MmRiN2E1OTc2ZjcifQ.A4SYmhnSqMY1aU4u83lxxls_y2rrhsyOjAOuXgJcW6g"
    headers = {
        "Authorization":f"Bearer {token}",
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print("solicitud exitosa")
        data = response.json()
        print(data)
        with open(nombreArchivo, 'w') as f:
            json.dump(data,f)
    else:
        print("error")

    return data 

ObtenciónDatos(15,"AricaDiesel.json")
print(ObtenciónDatos)