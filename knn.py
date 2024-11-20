import os
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import GridSearchCV

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
    #print(X)
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
    X, y_encoded, test_size=0.1, random_state=29)#7#23#29

tamanho_X_train = X_train.shape[0]
print(f'O tamanho de X_train é: {tamanho_X_train} amostras')
tamanho_y = y_train.shape[0]
print(f'O tamanho de y é: {tamanho_y} amostras')


# Criação do modelo KNN
knn = KNeighborsClassifier(n_neighbors=3, metric='cosine')

# Treinamento do modelo
knn.fit(X_train, y_train)

# Realiza previsões no conjunto de teste
y_pred = knn.predict(X_test)

# Avalia a acurácia do modelo
acuracia = accuracy_score(y_test, y_pred)
print(f'Acurácia do modelo KNN: {acuracia * 100:.2f}%')

# Avaliação da precisão do modelo
precision_micro = precision_score(
    y_test, y_pred, average='weighted', zero_division=1)
precision_macro = precision_score(
    y_test, y_pred, average='macro', zero_division=1)
print(f'Precisão do modelo KNN (Micro): {precision_micro * 100:.2f}%')
print(f'Precisão do modelo KNN (Macro): {precision_macro * 100:.2f}%')

# Avaliação da sensibilidade (recall) do modelo
recall_micro = recall_score(
    y_test, y_pred, average='weighted', zero_division=1)
recall_macro = recall_score(y_test, y_pred, average='macro', zero_division=1)
print(
    f'Sensibilidade (Recall) do modelo KNN (Micro): {recall_micro * 100:.2f}%')
print(
    f'Sensibilidade (Recall) do modelo KNN (Macro): {recall_macro * 100:.2f}%')

# Avaliação da pontuação F1 do modelo
f1_micro = f1_score(y_test, y_pred, average='weighted', zero_division=1)
f1_macro = f1_score(y_test, y_pred, average='macro', zero_division=1)
print(f'Pontuação F1 do modelo KNN (Micro): {f1_micro * 100:.2f}%')
print(f'Pontuação F1 do modelo KNN (Macro): {f1_macro * 100:.2f}%')


# No modo "macro", as métricas são calculadas para cada classe e, em seguida, a média é tomada. Cada classe é tratada igualmente, independentemente do número de amostras em cada classe.
# No modo "micro", as métricas são calculadas globalmente contando o total de verdadeiros positivos, falsos positivos e falsos negativos para todas as classes. Isso leva em consideração o desequilíbrio de classes. O "weighted" é uma variação do "micro" que leva em conta o desequilíbrio de classes, atribuindo pesos de acordo com o suporte de cada classe.
