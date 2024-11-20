texto ="""Voce classificara o texto com somente um token que vai de c1 ate c11, 
        dado as seguintes classificações: 
        c1 - Como documento eletrônico (ex: O problema aconteceu por conta de um erro em um arquivo DAT); 
        c2 - Como conjunto de documentos (ex: Arquivos que contiverem informações sobre crimes cometidos fora do período englobado pela Lei de Anistia (1947 a 1985) terão suas investigações também abertas pelo governo); 
        c3 - Como documento em papel, documento fisico (ex: Por favor, coloque esse documento no arquivo correspondente à categoria Finanças.); 
        c4 - Como instituição arquivística(ex: ARQUIVO PÚBLICO MUNICIPAL VITÓRIA na década de 50 O MAIOR TERREMOTO já ocorrido foi no Chile); 
        c5 - Como nome de um produto (ex.: um produto cultural como um programa de TV); 
        c6 - Como fonte (ex: Fonte: Arquivo A Tribuna; ex: ARQUIVO /AT ); 
        c7 - Como encerramento de um processo jurídico (ex.: arquivou-se o caso); 
        c8 - Como móvel de armazenamento e acondicionamento; 
        c9 - Como testemunha (ex.: no assassinato de uma testemunha em potencial usa-se a expressão queima de arquivo); 
        c10 - Como setor de uma empresa (ex: CONTRATA-SE:Técnico de arquivo com experiência); 
        c11 - Como memória (ex.: no sentido conotativo ligado a relato de evento não esquecido). 

        Vou inserir um novo texto e você devera classificar com somente uma tag de c1 a c11
        Exemplo1: 
        User: Cópia de todos os papéis ficará no Arquivo Nacional do Rio 
        assistant: c4 
        Exemplo2: 
        User: abriu o arquivo utilizando o Micro-soft PowerPoint2010, clicou na guia Ferramentas e, em seguida, clicou naopção Converter 
        assistant: c1   """

import csv
import time
from openai import OpenAI

client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key="sua_chave",
)

def display_chat_history(messages):
    for message in messages:
        print(f"{message['role'].capitalize()}: {message['content']}")

def get_assistant_response(messages):
    r = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": m["role"], "content": m["content"]} for m in messages],
        temperature=0.5,
        max_tokens=5,
        top_p=1
    )
    response = r.choices[0].message.content
    return response

def adicionar_ao_csv(classificacao, texto, nome_arquivo):
    # Abre o arquivo em modo de escrita, criando-o se não existir
    with open(nome_arquivo, 'a', newline='') as arquivo_csv:
        # Cria um objeto de escrita CSV com delimitador ponto e vírgula
        escritor_csv = csv.writer(arquivo_csv, delimiter=';')
        # Adiciona os resultados ao arquivo CSV
        escritor_csv.writerow([classificacao, texto])

messages = [{"role": "assistant", "content": texto}]

nome_arquivo = "saida3.csv"
with open(nome_arquivo, 'r') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)
        # Iterar sobre cada linha do CSV
        for linha in leitor_csv:
            linha = ', '.join(map(str, linha))
            txt = linha.replace(';','.')
            # Verifica se ambas as palavras "ARQUIVO" e "/AT" estão na string
            #if "ARQUIVO" in linha and "/AT" in linha:
             #   adicionar_ao_csv("c6", txt, "csv_aline.csv")
            #elif "ARQUIVO" in linha and "AT" in linha:
             #   adicionar_ao_csv("c6", txt, "csv_aline.csv")
           # elif "ARQUIVO/" in linha and "AT" in linha:
             #   adicionar_ao_csv("c6", txt, "csv_aline.csv")
           # else:
            print(linha)
            display_chat_history(messages)

            user_input = f" {linha}"
            messages.append({"role": "user", "content": user_input})

            assistant_response = get_assistant_response(messages)
                
                #print(f"\n {messages}")
                
            messages.clear()
            messages = [{"role": "assistant", "content": texto}]

                #salva no csv
                # Mapeamento entre os strings e as respostas desejadas
            mapping = {"c11": "c11", "c2": "c2", "c3": "c3", "c4": "c4", "c5": "c5",
                        "c6": "c6", "c7": "c7", "c8": "c8", "c9": "c9", "c10": "c10", "c1": "c1"}
                # Inicializa a resposta como vazia
            resp = ""
                # Verifica se algum dos strings mapeados está em assistant_response
            encontrou = False
            for key in mapping:
                    if key in assistant_response:
                        resp = mapping[key]
                        adicionar_ao_csv(resp, txt, "csv_aline3.csv")
                        encontrou = True
                        break  # Sai do loop assim que encontrar a correspondência
            if encontrou == False:
                    resp = "c13"       
                    adicionar_ao_csv(resp, txt, "csv_aline3.csv")
                
            time.sleep(1)
