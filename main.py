import requests
import json

#url a consultar"

url = "https://api.bencinaenlinea.cl/api/estaciones/precios_combustibles/2,10/reporte_comunal?cod_region%5B%5D=13"

#el token que te proporcionan

token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOi8vYXBpLmNuZS5jbC9hcGkvbG9naW4iLCJpYXQiOjE3MzY2MjM0MzQsImV4cCI6MTczNjYyNzAzNCwibmJmIjoxNzM2NjIzNDM0LCJqdGkiOiJibWpoTWM5OHN6U3h4R1ZTIiwic3ViIjoiMjU0MyIsInBydiI6IjIzYmQ1Yzg5NDlmNjAwYWRiMzllNzAxYzQwMDg3MmRiN2E1OTc2ZjcifQ.A4SYmhnSqMY1aU4u83lxxls_y2rrhsyOjAOuXgJcW6g"

#configurar encabezados para el token

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}


#realizar solicitudes de la api

response = requests.get(url, headers=headers)

#verificar si la solicitud fue buena

if response.status_code == 200:
    print("solicitud exitosa")
    data = response.json()
    with open('data.json', 'w') as f:
        json.dump(data,f)
        
    print(data)

else:
    print("error")


