import glob
import os
import json

# dicionario[chave] -> valor
# Chave == caminho_arquivo == nome do arquivo
# Valor == datahora_ultima_modificacao == data e hora que o arquivo foi modificado em float exibindo um número como " 1702491386.8530931"


#Função responsável por processar todos os arquivos. 
#recebe da f()= verificar_arquivo _nao_processado os arquivos que precisam ser processados novamente
#Função responsável por salvar as informações dos arquivos em um JSON
def processar(arquivos_encontrados : list, caminho_arquivos_processados : str):
    print('carregando arquivos processados...')
    arquivo = open(caminho_arquivos_processados,"r")
    arquivos_processados = json.load(arquivo)
    print(arquivos_processados)
    print('carregamento finalizado.')
    # vamos checar os arquivos encontrados
    for _, caminho_arquivo in enumerate(arquivos_encontrados):
        precisa_processar = verificar_arquivo_nao_processados(arquivos_processados, caminho_arquivo=caminho_arquivo) # a passagem de valor para a função pode ocorrer de duas formas
        if precisa_processar:
            print(f'processando: {caminho_arquivo} ...') # substituir pela extração e gravação do resultado
            arquivos_processados[caminho_arquivo] = os.path.getmtime(caminho_arquivo)
        else:
            print(f'o arquivo não foi reprocessado: {caminho_arquivo} ...') # substituir pela extração e gravação do resultado
    print(arquivos_processados)
    print('salvando arquivos processados...')
    arquivo = open(caminho_arquivos_processados, 'w')
    json.dump(arquivos_processados, arquivo, indent=4)
    print('gravação concluída.')


#Funçao responsável por verificar se o arquivo foi modificado e sinlaiza se precisa ser processado novamente.
def verificar_arquivo_nao_processados(arquivos_processados : dict, caminho_arquivo : str):
    if caminho_arquivo in arquivos_processados.keys():
        datahora_ultima_modificacao = arquivos_processados[caminho_arquivo]
        if os.path.getmtime(caminho_arquivo) == datahora_ultima_modificacao:
            print("o arquivo já foi inserido, porém não foi modificado.")
            return False # o arquivo será processado novamente
        else:
            print("o arquivo já foi inserido e modificado.")
    return True

#Função responsável por listar os arquivos dos diretórios de forma recursiva.
def listar_arquivos_recursivamente(diretorio : str, ext : str) -> [str]:
    caminhos_arquivos_encontrados = glob.glob(diretorio + f'/**/*.{ext}', recursive=True)
    # remover para produção print / deixar como documentação
    for indice, caminho_arquivo in enumerate(caminhos_arquivos_encontrados):
        print(f'{indice} -> caminho do arquivo: {caminho_arquivo}')
    return caminhos_arquivos_encontrados

#Utilizando um diretório Fake para testes
caminho_arquivos_processados = '/workspaces/Projeto-Gloob/resultado/arquivos_processados.json'
diretorio = '/workspaces/Projeto-Gloob/raiz'
ext = 'txt'

# Quando passar o caminho do repositório se atentar para "/r" ou caracteres especiais no path "/workspaces/Projeto-Gloob/raiz" , substituir po "//" ou "\"
# C:/Users/ruth.silva/Desktop/testes/testando-glob/raiz\arquivo-raiz.txt
# print(arquivos_processados)

arquivos_encontrados = listar_arquivos_recursivamente(diretorio, ext)
processar(arquivos_encontrados, caminho_arquivos_processados)


