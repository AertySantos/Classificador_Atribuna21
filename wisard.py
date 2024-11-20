import os
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.preprocessing import OneHotEncoder
import wisardpkg as wsd  # Importa a biblioteca WiSARD

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
pasta_dados = 'csv_c015q300/'

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

# Divide os dados em conjuntos de treino e teste (por exemplo, 80% treino, 20% teste)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Criação do modelo WiSARD com 3 RAMs (Random Access Memory)
model = wsd.Wisard(5)

# Treinamento do modelo com os dados de treino
model.train(X_train, y_train)

# Realiza previsões no conjunto de teste
y_pred = model.classify(X_test)

# Avalia as métricas do modelo
acuracia = accuracy_score(y_test, y_pred)
precision_micro = precision_score(
    y_test, y_pred, average='micro', zero_division=1)
precision_macro = precision_score(
    y_test, y_pred, average='macro', zero_division=1)
recall_micro = recall_score(y_test, y_pred, average='micro', zero_division=1)
recall_macro = recall_score(y_test, y_pred, average='macro', zero_division=1)
f1_micro = f1_score(y_test, y_pred, average='micro', zero_division=1)
f1_macro = f1_score(y_test, y_pred, average='macro', zero_division=1)

# Exibe as métricas
print(f'Acurácia do modelo WiSARD: {acuracia * 100:.2f}%')
print(f'Precisão do modelo WiSARD (Micro): {precision_micro * 100:.2f}%')
print(f'Precisão do modelo WiSARD (Macro): {precision_macro * 100:.2f}%')
print(
    f'Sensibilidade (Recall) do modelo WiSARD (Micro): {recall_micro * 100:.2f}%')
print(
    f'Sensibilidade (Recall) do modelo WiSARD (Macro): {recall_macro * 100:.2f}%')
print(f'Pontuação F1 do modelo WiSARD (Micro): {f1_micro * 100:.2f}%')
print(f'Pontuação F1 do modelo WiSARD (Macro): {f1_macro * 100:.2f}%')
