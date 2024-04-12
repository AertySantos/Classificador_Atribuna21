import csv
import os
import numpy as np
from sklearn.neighbors import NearestCentroid
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.preprocessing import OneHotEncoder

# Função para ler os dados de um arquivo CSV com rótulos em formato de strings


def ler_dados_arquivo(arquivo_csv):
    print(f"{arquivo_csv}")
    # Lê os dados do arquivo CSV
    dados = np.genfromtxt(arquivo_csv, delimiter=',', skip_header=1, dtype=str)

    # Extrai os rótulos da primeira coluna como strings
    y = dados[:, 0]  # Rótulos (primeira coluna) como strings

    # Extrai os recursos do restante das colunas
    # Recursos (todas as colunas, exceto a primeira) como números
    X = dados[:, 1:].astype(int)

    return X, y


# Pasta onde os arquivos CSV estão localizados
pasta_dados = 'csv/'

# Lista para armazenar os dados de todos os arquivos CSV
todos_X = []
todos_y = []

# Itera sobre os arquivos na pasta de dados
for arquivo in os.listdir(pasta_dados):
    if arquivo.endswith(".csv"):
        X, y = ler_dados_arquivo(os.path.join(pasta_dados, arquivo))
        todos_X.append(X)
        todos_y.append(y)

# Concatena todos os dados em uma matriz única
X = np.concatenate(todos_X)
y = np.concatenate(todos_y)

# Crie um objeto OneHotEncoder
onehot_encoder = OneHotEncoder(sparse_output=False)

# Ajuste e transforme os rótulos categóricos em codificação one-hot
y_encoded = onehot_encoder.fit_transform(y.reshape(-1, 1))

# Divisão dos dados em conjunto de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(
    X, y_encoded, test_size=0.1, random_state=53)

tamanho_X_train = X_train.shape[0]
print(f'O tamanho de X_train é: {tamanho_X_train} amostras')
tamanho_y = y_train.shape[0]
print(f'O tamanho de y é: {tamanho_y} amostras')

# --------------------------------

# Criação do modelo Centroid-Based Classification (CBC)
cbc = NearestCentroid()

# Treinamento em lotes
cbc.fit(X_train, y_train.argmax(axis=1))

# --------------------------------
# Realiza previsões no conjunto de teste
y_pred = cbc.predict(X_test)

# Avalia a acurácia do modelo
acuracia = accuracy_score(y_test.argmax(axis=1), y_pred)
print(f'Acurácia do modelo CBC: {acuracia * 100:.2f}%')

# Avaliação da precisão do modelo
precision_micro = precision_score(y_test.argmax(
    axis=1), y_pred, average='weighted', zero_division=1)
precision_macro = precision_score(y_test.argmax(
    axis=1), y_pred, average='macro', zero_division=1)
print(f'Precisão do modelo CBC (Micro): {precision_micro * 100:.2f}%')
print(f'Precisão do modelo CBC (Macro): {precision_macro * 100:.2f}%')

# Avaliação da sensibilidade (recall) do modelo
recall_micro = recall_score(y_test.argmax(
    axis=1), y_pred, average='weighted', zero_division=1)
recall_macro = recall_score(y_test.argmax(
    axis=1), y_pred, average='macro', zero_division=1)
print(
    f'Sensibilidade (Recall) do modelo CBC (Micro): {recall_micro * 100:.2f}%')
print(
    f'Sensibilidade (Recall) do modelo CBC (Macro): {recall_macro * 100:.2f}%')

# Avaliação da pontuação F1 do modelo
f1_micro = f1_score(y_test.argmax(axis=1), y_pred,
                    average='weighted', zero_division=1)
f1_macro = f1_score(y_test.argmax(axis=1), y_pred,
                    average='macro', zero_division=1)
print(f'Pontuação F1 do modelo CBC (Micro): {f1_micro * 100:.2f}%')
print(f'Pontuação F1 do modelo CBC (Macro): {f1_macro * 100:.2f}%')

# Arredondando os valores para quatro casas decimais
acuracia = round(acuracia, 4)
precision_macro = round(precision_macro, 4)
recall_macro = round(recall_macro, 4)
f1_macro = round(f1_macro, 4)

# Nome do arquivo CSV a ser criado
nome_arquivo = 'resultados/m-1NN.csv'

# Escrevendo os valores no arquivo CSV usando ponto e vírgula como separador
with open(nome_arquivo, 'w', newline='') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv, delimiter=';')
    escritor_csv.writerow(
        [acuracia, precision_micro, recall_micro, f1_micro])

nome_arquivo = 'resultados/M-1NN.csv'

# Escrevendo os valores no arquivo CSV usando ponto e vírgula como separador
with open(nome_arquivo, 'w', newline='') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv, delimiter=';')
    escritor_csv.writerow([acuracia, precision_macro, recall_macro, f1_macro])
