inventario={}
opcao=int(input("Digite: \n<1> para registrar ativo \n<2> para persistir em arquivo \n<3> para exibir ativos armazenados: "))
while opcao>0 and opcao<4:
    if opcao==1:
        resp="S"
        while resp=="S":
            inventario[input("Digite o número patrimonial: ")]=[
            input("Digite a data da última atualização: "),
            input("Digite a descrição: "),
            input("Digite o departamento: ")]
            resp=input("Digite <S> para continuar.").upper()
    elif opcao==2:
        with open("./files/inventario.csv", "a") as inv:
            for chave, valor in inventario.items():
                inv.write(chave + ";" + valor[0] + ";" + 
					valor[1] + ";" +valor[2] + "\n")
                print("Persistido com sucesso!")
    elif opcao==3:
        with open("./files/inventario.csv", "r") as inv:
            print(inv.readlines())
    opcao=int(input("Digite: \n<1> para registrar ativo \n<2> para persistir em arquivo \n<3> para exibir ativos armazenados: "))