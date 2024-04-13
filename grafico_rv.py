import csv
import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

# Nomes dos arquivos CSV
nome_arquivo1 = "csv_aline_revisado.csv"

# Lista para armazenar os nomes dos arquivos e suas respectivas cores
arquivos_cores = [(nome_arquivo1, 'b')]

# Inicialize uma lista vazia para armazenar os DataFrames
dataframes = []

# Itere sobre os arquivos e leia cada CSV
for nome_arquivo, cor in arquivos_cores:
    csv_content = ""
    
    with open(nome_arquivo, 'r') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)
        
        for linha in leitor_csv:
            csv_content += ','.join(linha) + '\n'
    
    # Converter o CSV para um DataFrame pandas, considerando apenas a primeira coluna
    df = pd.read_csv(StringIO(csv_content), delimiter=';', usecols=[0], header=None, names=['Código'])
    dataframes.append((df, cor, nome_arquivo))

# Calcular a soma das ocorrências para cada código no primeiro DataFrame
soma_ocorrencias = dataframes[0][0]['Código'].value_counts()

# Ordenar os códigos com base na soma das ocorrências
codigos_ordenados = soma_ocorrencias.index

# Selecionar apenas três arquivos para a legenda
arquivos_legenda = dataframes[:3]

# Criar o gráfico de barras combinado para todos os DataFrames
plt.figure(figsize=(12, 8))
bar_width = 0.5  # Largura das barras

# Iterar sobre os códigos ordenados
for i, codigo in enumerate(codigos_ordenados):
    # Iterar sobre os DataFrames e suas cores
    for j, (df, cor, nome_arquivo) in enumerate(arquivos_legenda):
        # Contar a ocorrência do código no DataFrame atual
        count = df[df['Código'] == codigo].shape[0]
        
        # Ajustar a posição das barras no eixo x
        posicao_barra = i + j * bar_width
        if i > 0:
            nome_arquivo = ""
        else:
            if j == 0:
                nome_arquivo = "Supervised Data"
     

        plt.bar(posicao_barra, count, width=bar_width, color=cor, alpha=0.7, label=f'{nome_arquivo}')

plt.xticks(range(len(codigos_ordenados)), codigos_ordenados)
plt.ylabel('Sentences')
plt.xlabel('Classes')
plt.title('Frequency of the term $\\mathit{archive}$')
plt.legend()
plt.show()
