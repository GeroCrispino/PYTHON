import pandas as pd
from matplotlib import pyplot as plt

data_set = pd.read_csv('datos de prueba.csv', encoding='utf-8')

datos_inicio = data_set[(data_set['Nombre de evento'] == 'inicio_partida')]
datos_fin = data_set[(data_set['Nombre de evento'] == 'fin')]
lista_nom = datos_fin['Usuarie - nick'].tolist()

lista_inicio = datos_inicio['Tiempo'].tolist()
lista_fin = datos_fin['Tiempo'].tolist()
lista_usuarios = []

for i in range(len(lista_inicio)):
    tiempo = lista_fin[i] - lista_inicio[i]
    dic = {'usuario':{'Nombre':lista_nom[i],'Tiempo':tiempo}}
    lista_usuarios.append(dic)

lista_usuarios.sort(key = lambda u: u['usuario']['Tiempo'], reverse= True)

top3_nom = []
top3_time = []
for i in range(3):
    top3_nom.append(lista_usuarios[i]['usuario']['Nombre'])
    top3_time.append(lista_usuarios[i]['usuario']['Tiempo'])

df = pd.DataFrame()
df['Nombre'] = top3_nom
df['Tiempo'] = top3_time

plt.pie(df['Tiempo'],labels= top3_nom,autopct="%0.1f %%")
plt.axis('equal')
plt.show()