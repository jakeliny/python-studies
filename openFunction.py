## open(">caminhoArquivo><nomeArquivo>", "w")
# w -  write, se o arquivo ja existir, sobreescreve
# r - read
# a - append - write and read, ler o que existe e adicionar algo novo
# x - excluisive, cria um arquivo de forma excluida, se for um arquivo que ja exite retorna falha
# t - text, retorna o conteudo como uma string 
# b - binary, retorna o conteudo como um binario

## Pode se combinar os paramentros com + "w+b" ou "wb"

## O comando with é que controla o encerrzamento do arquivo, assim não 
# precisamos usar o comando close() e nem correr o risco do arquivo ficar 
# aberto na memoria, então combinar o comando with + open() é uma  boa

with open("./files/teste.txt", "w") as arquivo:
    arquivo.write("Python is a better snake \n and programming code")

with open("./files/teste.txt", "r") as arquivo:
    conteudo1 = arquivo.readlines()
# readlines retorna em lista

with open("./files/teste.txt", "rb") as arquivo:
    conteudo2 = arquivo.read()

print("conteudo 1: ", conteudo1)
print("tipo: ", type(conteudo1))
# type() - retorna o tipo de arquivo
print("conteudo2 : ", type(conteudo2))
print("tipo: ", type(conteudo2))
