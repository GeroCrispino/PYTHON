import matplotlib.pyplot as plt
import pandas as pd
from wordcloud import WordCloud, wordcloud

def palabras():
    archivo_csv = 'PES.csv'
    dataframe = pd.read_csv(archivo_csv,encoding='UTF-8')
    new_df = dataframe[(dataframe['Team Name'] == 'Free Agents') & (dataframe['Overall Rating'] >= 80)]
    return new_df['Player Name']

texto = str(palabras())

print(texto)
wordcloud = WordCloud(width = 500, height = 300,background_color='black', colormap='inferno', collocations=True).generate(texto)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()