import csv
import os
import json

def archivo_PES():
    jugadores = []
    if os.path.exists('src/csv/PES2019.csv') == True:
        with open('src/csv/PES2019.csv','r',encoding= 'UTF-8') as csv_file:
            reader = csv.DictReader(csv_file)
            for linea in reader:
                if linea['Nationality'] == 'ARGENTINA':
                    dic_jug = {'Nombre': linea['Player Name'], 'Rating': linea['Overall Rating']}
                    jugadores.append(dic_jug)
            jugadores = list(sorted(jugadores,key= lambda j: j['Rating'], reverse= True))
            jugadores = jugadores[:10]
        with open('Top10_Arg.json', 'w') as json_file:
            json_file.write(json.dumps(jugadores, indent= 2))
    