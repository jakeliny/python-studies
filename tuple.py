#tuplas na key de um dicionario
tupla[chave, secondChave] = [valores]

#pegando as keys
for key in tupla.keys():
    print(key[0] "." ip[key])


##Example
#Criando um dicionario varzio
varUsuarios = {}
#Criando uma lista de emails
emails = ["jakeliny.gr@gmail.com", "thasfin@gmail.com"]

#criando uma tupla
#list vai criar uma tupla com cada item da variavel email
#enumerate enumera cada item da variavel emails
varTupla = list(enumerate(emails))

#rodar um for no tamanho da tupla len()
for key in range(0,len(varTupla)):
		#varTupla[key][1] é que o email está sempre na posição 2
		# e o key está sendo pego do contador
    print("Email: ", varTupla[key][1])

		# estamos colocando no dicioanrio varUsuarios
		# uma key que é a tupla (0, "jakeliny.gr@gmail.com")
		# e como value estamos inserindo uma lista de duas posições com nome e nivel
    varUsuarios[varTupla[key]]=[input("Digite o nome"), input("Digite o nível")]

#Aqui vamos exibir todos os dados desse dicionario varusuarios
for key, value in varUsuarios.items():
    print("Usuario.:", key[0])
    print("Email...: ",key[1])
    print("Nome....: ", value[0])
    print("Nível...: ", value[1])