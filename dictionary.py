variavel = {} #declarando um dicionario

variavel= {
	"Chaves":["Chaves Silva","17/06/2017","Recep_01"],
    "Quico":["Enrico Flores","03/06/2017","Raiox_02"]
}

#populando um unico dicionario
variavel["Florinda"]=["Florinda Flores", "26/11/2017", "Recep_01"]

#para pegar o valor
print(variavel.geT()) #mostra tudo que há no dicionario
print(variavel.get("Chaves")) #mostra tudo na chave "Chaves"

#criand um dicionario vazio
usuarios={}

chave=input("Digite o login: ").upper()
nome=input("Digite o nome: ").upper()
data=input("Digite a última data de acesso: ")
estacao=input("Qual a última estação acessada: ").upper()
usuarios[chave]=[nome, data, estacao]

#melhorando
chave=input("Digite o login: ").upper()
usuarios[chave]=[input("Digite o nome: ").upper(),
                 input("Digite a última data de acesso: "),
                 input("Qual a última estação acessada: ").upper()]


#del a key and key's value
del dicionario[chave]

#get all dictionary
for chave, valor in dicionario.items():
	print("Objeto......")
  print("Login: ", chave)
  print("Dados: ", valor)


##Others function

#Retorna o dicionario em uma lista divido por tuplas, ex:
.items()
[("chaves",["login", "data", "estacao"]),("chaves",["login", "data", "estacao"])]

#Retorna o dicionario em lista apenas com os dados
.values()
[["login", "data", "estacao"],["login", "data", "estacao"]]

#Retorna apenas as chaves
.keys()
["chaves","kiko"l]

#Retorna um boleano se a chave passada existe ou não
.has_key()

#Limpa completamente um dicionario
clear()

#Exibe item a item do dicionario e logo apos exlui do dicionario
.popitem()
