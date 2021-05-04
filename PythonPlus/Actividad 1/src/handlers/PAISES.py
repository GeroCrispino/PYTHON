import csv
import os
import json

def archivo_Paises():
    paises = []
    if os.path.exists('src/csv/Paises del Mundo.csv') == True:
        with open('src/csv/Paises del Mundo.csv','r',encoding= 'UTF-8') as csv_file:
            reader = csv.DictReader(csv_file)
            for linea in reader:
                if linea['Region'] == 'LATIN AMER. & CARIB    ':
                    dic_paises = {'Nombre': linea['Country'], 'Poblacion': int(linea['Population'])}
                    paises.append(dic_paises)
            paises = list(sorted(paises,key= lambda p: p['Poblacion'], reverse= True))
            paises = paises[:20]
        with open('Top20_Paises_Sud_Car.json', 'w') as json_file:
            json_file.write(json.dumps(paises, indent= 2))