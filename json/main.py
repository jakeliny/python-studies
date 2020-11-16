from functions import *

arquivo = "../files/inventario_json.json"
inventario = lerArquivo(arquivo)
opcao = chamarMenu()

while opcao > 0 and opcao < 4:
    if opcao==1:
        print(registrar(inventario, arquivo))

    elif opcao==2:        
        exibir(arquivo)

    elif opcao ==3:
        exit()

    opcao = chamarMenu()
