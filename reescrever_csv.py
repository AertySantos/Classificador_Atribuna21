import csv

classe_anterior = ""

def adicionar_espaco(texto):
    global classe_anterior

    if classe_anterior == "c6":
        classe_anterior = ""
        return fonte(texto)
    
    classe_anterior = texto
    return espaco(texto)
    

def espaco(texto):
    texto_low = texto.lower()
    print(texto)
    
    if 'arquivo' in texto_low:
        # Iterar sobre cada caractere do texto
        for i in range(len(texto)):
            # Verificar se o caractere atual é 'a' (início de "arquivo")
            if texto_low[i] == 'a':
                # Verificar se os próximos caracteres formam "arquivo"
                if texto_low[i:i+7] == 'arquivo':

                     # Verificar se há uma palavra após "arquivo"
                    if i+7 < len(texto) and not texto[i+7].isspace():
                        # Inserir um espaço após "arquivo" se a próxima palavra não for um espaço
                        texto = texto[:i+7] + ' ' + texto[i+7:]
                    # Verificar se há uma palavra antes de "arquivo"
                    if i-1 >= 0 and not texto[i-1].isspace():
                        # Inserir um espaço antes de "arquivo" se a palavra anterior não for um espaço
                        texto = texto[:i] + ' ' + texto[i:]
                    break
    return texto

def fonte(texto):
    texto_low = texto.lower()
    # Encontra a posição da string "arquivo" em texto_low
    pos_arquivo = texto_low.find("arquivo")

    # Verifica se "arquivo" está presente e se "at" ocorre nos próximos 4 caracteres após "arquivo"
    if pos_arquivo != -1 and "a t" in texto_low[pos_arquivo + len("arquivo"):pos_arquivo + len("arquivo") + 4]:
        index_arquivo = texto_low.index("arquivo")
        return espaco(texto[index_arquivo:index_arquivo + len("arquivo") + 4])
    elif pos_arquivo != -1 and "at" in texto_low[pos_arquivo + len("arquivo"):pos_arquivo + len("arquivo") + 4]:
        index_arquivo = texto_low.index("arquivo")
        return espaco(texto[index_arquivo:index_arquivo + len("arquivo") + 4])
    else:
     return espaco(texto)
    
# Abra o arquivo CSV de entrada
with open('saida.csv', newline='', encoding='utf-8') as csvfile:
    # Leia o arquivo CSV usando o delimitador ';'
    reader = csv.reader(csvfile, delimiter=';')
    
    # Abra o arquivo de saída para escrita
    with open('saida2.csv', 'w', newline='', encoding='utf-8') as newfile:
        writer = csv.writer(newfile, delimiter=';')
        
        # Itere sobre as linhas do arquivo CSV de entrada
        for row in reader:
            # Para cada item na linha, adicione espaço se necessário
            modified_row = [adicionar_espaco(item) for item in row]
            # Escreva a linha modificada no novo arquivo CSV
            writer.writerow(modified_row)

print("Processo concluído. Verifique o novo arquivo CSV gerado.")

