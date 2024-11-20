
import os
import string
import sys

def similaridade(pasta, arquivo):

    diretorio_p = f"real/{pasta}"
    # Inicialize uma lista vazia
    vetor = []
    # Crie a pasta se ela ainda não existir
    if not os.path.exists(diretorio_p):
        os.makedirs(diretorio_p)

    nome_arquivo = os.path.basename(arquivo)  # Obtém o nome do arquivo
    # Salva as frequências de palavras em arquivos
    caminho = os.path.join(diretorio_p, nome_arquivo)

    with open(arquivo, "r", encoding="iso-8859-1") as arquivo:
         coluna = arquivo.read().lower()
         

nome_arquivo = "classes.txt"  # aquivo de entrada com o arquivo inicial 

# Percorre os arquivos no diretório e conta as palavras
with open(nome_arquivo, "r", encoding="iso-8859-1") as arquivo:
        texto = arquivo.read().lower()
        texto = texto.translate(str.maketrans('', '', string.punctuation))
        palavras = texto.split()  # Divide o texto em palavras (separadas por espaço em branco)

        for pasta in palavras:
                max = 0
                diretorio = f"arq_pesos/{pasta}"
                tam = os.listdir(diretorio)
                for arq2 in os.listdir(diretorio):
                    max += 1
                    if max > 1000:
                        break

                    if arq2.endswith('.txt'):
                        caminho_arq = os.path.join(diretorio, arq2)
                        #peso_arq(pasta, caminho_arq2, freq_inv)
                        similaridade(pasta, caminho_arq)

                    sys.stdout.write('\r'+f'[✔] Processando {pasta}: '+str(max)+'/'+str(
                        len(tam))+' ' + '{:.2f}'.format(max/len(tam)*100)+'%')
                    sys.stdout.flush()