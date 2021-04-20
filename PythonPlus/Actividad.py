import csv
from collections import Counter
import operator

#PUNTO 1
def lista_esp():
    gratis_esp = []
    with open ('appstore_games.csv','r',encoding= 'UTF-8') as archivo:
        reader= csv.reader(archivo, delimiter= ',')
        reader.__next__()
        for line in reader:
            if line[7] == '0':
                lista_idioma = line[12].replace(' ', ',').split(',')
                if 'ES' in lista_idioma:
                    gratis_esp.append(line[2])
    return gratis_esp


#PUNTO 2
def diez_mejores():
    lista_diez = []
    with open ('appstore_games.csv','r',encoding= 'UTF-8') as archivo:
        reader= csv.reader(archivo, delimiter= ',')
        reader.__next__()
        dicc= {}
        for line in reader:
            if (line [6] != ''):
                dicc[line[4]] = int(line[6])
        dicc = sorted(dicc.items(), key=operator.itemgetter(1))
    cont = 0
    for i in reversed(range(len(dicc))):
        if cont == 10:
            break
        lista_diez.append(dicc[i])
        cont += 1
    
    
    return lista_diez

print('PUNTO 1')
print('-'*260)
print(lista_esp())
print('-'*260)
print('PUNTO 2')
print('-'*260)
print(diez_mejores())       