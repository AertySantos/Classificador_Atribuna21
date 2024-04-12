import csv
import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

# Nomes dos arquivos CSV
nome_arquivo1 = "csv_aline_revisado.csv"
nome_arquivo2 = "csv_aline2.csv"
nome_arquivo3 = "csv_aline3.csv"

# Lista para armazenar os nomes dos arquivos e suas respectivas cores
arquivos_cores = [(nome_arquivo1, 'red'), (nome_arquivo2, 'green'), (nome_arquivo3, 'blue')]

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
    dataframes.append((df, cor))

# Criar o gráfico de barras combinado para todos os DataFrames
plt.figure(figsize=(10, 6))
for df, cor in dataframes:
    counts = df['Código'].value_counts()
    plt.bar(counts.index, counts.values, color=cor, alpha=0.7)

plt.xlabel('Código')
plt.ylabel('Quantidade')
plt.title('Frequência de Códigos em Diferentes Arquivos CSV')
plt.legend([f'{nome} ({cor})' for nome, cor in arquivos_cores])
plt.show()


