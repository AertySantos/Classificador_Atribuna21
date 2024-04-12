import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Lista de caminhos para os arquivos CSV
caminhos_csv = ["resultados/r1_revisado/M-WiSARD.csv", "resultados/r2/M-WiSARD.csv", "resultados/r3/M-WiSARD.csv"]

# Lista de métricas a serem plotadas
metricas = ['Acuracia', 'Precisao', 'Recall', 'F1']

# Configurar cores para cada CSV
cores = ['blue', 'orange', 'green']

# Criar um gráfico de barras agrupadas
fig, ax = plt.subplots()

largura_barra = 0.2
ind = np.arange(len(metricas))
print("teste")
for i, caminho_do_csv in enumerate(caminhos_csv):
    dados = pd.read_csv(caminho_do_csv, header=None, sep=';')
    
    for j, metrica in enumerate(metricas):
        valores = dados.iloc[:, j]  # Obtém a coluna pelo índice j
        barras = ax.bar(ind + i * largura_barra, valores, largura_barra, label=f'{caminho_do_csv} - {metrica}', color=cores[i])

# Adicionar rótulos e legendas
ax.set_xlabel('Métricas')
ax.set_ylabel('Valores')
ax.set_title('Métricas por CSV')
ax.set_xticks(ind + largura_barra * (len(caminhos_csv) - 1) / 2)
ax.set_xticklabels(metricas)
ax.legend()

# Exibir o gráfico
plt.show()
