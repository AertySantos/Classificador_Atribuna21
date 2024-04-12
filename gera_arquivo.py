import os
import pandas as pd

def criar_pastas_e_textos(csv_path):
    # Leitura do arquivo CSV com ";" como separador
    try:
        df = pd.read_csv(csv_path, header=None, names=['Nome da Pasta', 'Conteúdo do Texto'], sep=';')
    except FileNotFoundError:
        print(f"Arquivo {csv_path} não encontrado.")
        return
    except pd.errors.EmptyDataError:
        print(f"O arquivo {csv_path} está vazio.")
        return

    # Iteração sobre cada linha do DataFrame
    for index, row in df.iterrows():
        # Obtendo o nome da pasta e o conteúdo do texto
        nome_da_pasta = str(row[0]).strip()
        conteudo_do_texto = str(row[1]).strip()

        # Criando a pasta, se não existir
        if not os.path.exists(nome_da_pasta):
            os.makedirs(nome_da_pasta)

        # Criando um nome de arquivo único
        nome_do_arquivo = f'Texto_{index + 1}.txt'
        texto_file_path = os.path.join(nome_da_pasta, nome_do_arquivo)

        # Criando o arquivo de texto dentro da pasta
        with open(texto_file_path, 'w') as texto_file:
            texto_file.write(conteudo_do_texto)

        print(f'Pasta "{nome_da_pasta}" e arquivo de texto "{nome_do_arquivo}" criados.')

# Substitua 'caminho/do/seu/arquivo.csv' pelo caminho real do seu arquivo CSV
caminho_do_arquivo_csv = 'csv_aline3.csv'

# Chamando a função para criar pastas e textos
criar_pastas_e_textos(caminho_do_arquivo_csv)

