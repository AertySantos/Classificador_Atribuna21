import numpy as np
import matplotlib.pyplot as plt

import pandas as pd

# Lista de caminhos para os arquivos CSV
caminhos_csv = ["resultados/r1_revisado/M-WiSARD.csv", "resultados/r2/M-WiSARD.csv", "resultados/r3/M-WiSARD.csv"]
#caminhos_csv = ["resultados/r1_revisado/m-WiSARD.csv", "resultados/r2/m-WiSARD.csv", "resultados/r3/m-WiSARD.csv"]
# Vetores para armazenar os dados
vet1 = []
vet2 = []
vet3 = []

# Iterar sobre os caminhos dos arquivos CSV
for i, caminho_do_csv in enumerate(caminhos_csv):
    # Carregar o CSV usando NumPy
    # Carrega o arquivo CSV usando pandas
    dataframe = pd.read_csv(caminho_do_csv, sep=';')

    # Itera sobre as colunas e imprime os valores
    for coluna in dataframe.columns:
        valores_coluna = np.genfromtxt(caminho_do_csv, delimiter=';')

        if i == 0:
            vet1 = valores_coluna
        elif i == 1:
            vet2 = valores_coluna
        elif i == 2:
            vet3 = valores_coluna
print(f"{vet1}|{vet2}|{vet3}")
# Lista de métricas a serem plotadas
metricas = ['Acuracia', 'Precisao', 'Recall', 'F1']

# data to plot
n_groups = 4
#means_frank = (90, 55, 40, 65)
#means_guido = (85, 62, 54, 20)

# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.2
opacity = 0.7

rects1 = plt.bar(index, vet1, bar_width,
alpha=opacity,
color='b',
label='Supervised Data')

rects2 = plt.bar(index + bar_width, vet2, bar_width,
alpha=opacity,
color='g',
label='Classification Data 1')

rects3 = plt.bar(index + 2*bar_width, vet3, bar_width,
alpha=opacity,
color='r',
label='Classification Data 1')

plt.xlabel('Macro Metrics')
plt.ylabel('Scores')
plt.title('Metrics with WiSARD Classifier')
plt.xticks(index + bar_width, ('Accuracy', 'Precision', 'Recall', 'F1-Score'))
plt.legend()

plt.tight_layout()
plt.show()