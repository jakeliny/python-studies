#modulo para a manipulação de json
import json

#modulo para acessar objetos e funções do SO
import os

def chamarMenu():
    return int(input("Digite: \n<1> para registrar ativo \n<2> para exibir ativos armazenados \n<3> para sair: "))


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


def registrar(dicionario, arquivo):
    resp = "S"
    while resp == "S":
        dicionario[input("Digite o código: ")] = [
            input("Digite a data da atualização: "),
            input("Digite a tarefa: "),
            input("Digite o local: ")]
        resp = input("Digite <S> para continuar.").upper()
        gravarArquivo(dicionario, arquivo)
    return "JSON gerado!!!!"


def exibir(arquivo):
    dicionario = lerArquivo(arquivo)
    #Fazemos um foreach em items que são os dados no json
    for chave, dado in dicionario.items():
        print("Código........: ", chave)
        print("Data..........: ", dado[0])
        print("Tarefa........: ", dado[1])
        print("Local.........: ", dado[2])
