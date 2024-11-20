import os
import PyPDF2
import json
import requests
import base64
import csv

def pesquisa_palavras(palavra):
    # Codifica a palavra em base64
    palavra_base64 = base64.b64encode(palavra.encode()).decode()

    # Substitua 'sua_url' pela URL real do dicionário que você deseja consultar
    url_dicionario = f'http://201.73.0.34:8000/search/?database=atribuna&query={palavra_base64}==&action=search&numResp=10000'

    try:
        # Faz a requisição GET para o dicionário
        resposta = requests.get(url_dicionario)

        # Verifica se a requisição foi bem-sucedida
        if resposta.status_code == 200:
            # Retorna a resposta do dicionário JSON
            arquivos = json.loads(resposta.text)
            i=0
            for nomearquivo,arquivo in arquivos['documents']:
                i +=1
                n = f"pagina{i}.pdf"
                print(n)
                with open(f'{diretorio_pdf}{n}', 'wb') as f:
                    f1 = requests.get(arquivo)
                    f.write(f1.content)


            return resposta.text
        else:
            # Se a requisição não for bem-sucedida, imprime o código de status
            return f"Erro na requisição - Código: {resposta.status_code}"

    except requests.exceptions.RequestException as e:
        # Trata exceções de requisição
        return f"Erro na requisição: {str(e)}"


def buscar_palavra_em_pdf(diretorio, palavra):
    resultados = []

    # Itera sobre todos os arquivos no diretório
    for filename in os.listdir(diretorio):
        #processa apenas documentos em pdf
        if filename.endswith(".pdf"):
            filepath = os.path.join(diretorio, filename)

            #abre os arquivos
            with open(filepath, "rb") as file:
                # Inicializa o leitor PDF
                pdf_reader = PyPDF2.PdfReader(file)

                # Itera sobre todas as paginas do PDF
                for page_num in range(len(pdf_reader.pages)):
                    # Obtém o texto da página
                    page = pdf_reader.pages[page_num]
                    texto = page.extract_text().replace('\n',' ')
                    # Verifica se a palavra esta presente na pagina
                    if palavra.lower() in texto.lower():
                        # Separa as frases que contêm a palavra por arquivo
                        frases = [frase.strip() for frase in texto.split('.') if palavra.lower() in frase.lower()]

                        # Armazena os resultados na matriz
                        resultados.append({
                            'arquivo': filename,
                            'frases': frases,
                            'pagina': page_num+1
                        })

    return resultados

# Função para adicionar conteúdo em linhas de um arquivo CSV
def adicionar_ao_csv(resultados, nome_arquivo):
    # Abre o arquivo em modo de escrita, criando-o se não existir
    with open(nome_arquivo, 'a', newline='') as arquivo_csv:
        # Cria um objeto de escrita CSV com delimitador ponto e vírgula
        escritor_csv = csv.writer(arquivo_csv, delimiter=';')

        # Adiciona cabeçalhos se o arquivo estiver vazio
        if arquivo_csv.tell() == 0:
            escritor_csv.writerow(['Frase'])

        # Adiciona os resultados ao arquivo CSV
        for resultado in resultados:
            for frase in resultado['frases']:
                escritor_csv.writerow([frase])

# Diretório e palavras
diretorio_pdf = 'pdfs/'

# Verifica se a pasta já existe e a cria se não existir
if not os.path.exists(diretorio_pdf):
    os.makedirs(diretorio_pdf)
    print(f'A pasta "pdf" foi criada ')
else:
    print(f'A pasta "pdf" já existe')

palavra_procurada = 'arquivo'
pesquisa_palavras(palavra_procurada)
resultados = buscar_palavra_em_pdf(diretorio_pdf, palavra_procurada)
adicionar_ao_csv(resultados, "saida.csv")
# Exibe os resultados
for resultado in resultados:
    print(f"Arquivo: {resultado['arquivo']} , página {resultado['pagina']}")
    for i, frase in enumerate(resultado['frases'], 1):
        print(f"- {frase}")
    print("\n")



