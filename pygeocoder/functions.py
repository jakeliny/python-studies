#modulo para a manipulação de json
import json

#modulo para acessar objetos e funções do SO
import os

def lerArquivo(arquivo):
    #Verificando se o arquivo json existe
    if os.path.exists(arquivo):
        # abrimos o arquivo no modo read e adicionamos ao alias arq_json
        with open(arquivo, "r") as arq_json:
            dicionario = json.load(arq_json) #carregamos o conteudo do arquivo para a var dicionario
    else:
        #se não existir cria a variavel vazia
        dicionario={} 
    return dicionario


def gravarArquivo(dicionario, arquivo):
    #Abrimos o arquivo em modo write
    with open(arquivo, "w") as arq_json:
        json.dump(dicionario, arq_json) 
        #fazemos um dump com o dicionario atualizado