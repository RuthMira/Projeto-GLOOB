import glob
import os

def verificar_arquivo_nao_processados(arquivos_processados : dict, caminho_arquivo : str):
    if caminho_arquivo in arquivos_processados.keys():
        datahora_ultima_modificacao = arquivos_processados[caminho_arquivo]
        if os.path.getmtime(caminho_arquivo) == datahora_ultima_modificacao:
            print("o arquivo já foi inserido, porém não foi modificado.")
            return False # o arquivo será processado novamente
        else:
            print("o arquivo já foi inserido e modificado.")
    return True

def listar_arquivos_recursivamente(diretorio : str, ext : str) -> [str]:
    caminhos_arquivos_encontrados = glob.glob(diretorio + f'/**/*.{ext}', recursive=True)
    # remover para produção / deixar como documentação
    for indice, caminho_arquivo in enumerate(caminhos_arquivos_encontrados):
        print(f'{indice} -> caminho do arquivo: {caminho_arquivo}')
    return caminhos_arquivos_encontrados

diretorio = 'C:/Users/ruth.silva/Desktop/testes/testando-glob/raiz'
ext = 'txt'

# dicionario[chave] -> valor
arquivos_processados = {}
#arquivos_processados[caminho_arquivo_temp] = os.path.getmtime(caminho_arquivo_temp)


caminho_arquivo_temp = "C:/Users/ruth.silva/Desktop/testes/testando-glob/raiz\\arquivo-raiz.txt"
arquivos_processados[caminho_arquivo_temp] = 1702469169.751809


# C:/Users/ruth.silva/Desktop/testes/testando-glob/raiz\arquivo-raiz.txt
# print(arquivos_processados)
arquivos_encontrados = listar_arquivos_recursivamente(diretorio, ext)

# vamos checar os arquivos encontrados
for indice, caminho_arquivo in enumerate(arquivos_encontrados):
    precisa_processar = verificar_arquivo_nao_processados(arquivos_processados, caminho_arquivo=caminho_arquivo) # a passagem de valor para a função pode ocorrer de duas formas
    if precisa_processar:
        print(f'processando: {caminho_arquivo} ...') # substituir pela extração e gravação do resultado
        arquivos_processados[caminho_arquivo] = os.path.getmtime(caminho_arquivo)
    else:
        print(f'o arquivo não foi reprocessado: {caminho_arquivo} ...') # substituir pela extração e gravação do resultado


print(arquivos_processados)

# os.path.isfile(arquivo)
# os.path.getmtime(x)
# arquivo.lower().endswith('.pdf')