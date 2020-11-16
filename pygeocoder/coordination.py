from pygeocoder import Geocoder

from functions import *

#Ler um arquivo com endereço
dicionario = lerArquivo("../files/entrada.json")

lista = dicionario["endereco"]

endereco = lista[0] + "," + lista[1] + " " + lista[2] + " " + lista[3]

#Faz a busca de coordenadas
saida = {"coordenadas":Geocoder('YOUR_API_KEY').geocode(endereco).coordinates}

#Grava as coordenadas em um arquivo json
gravarArquivo(saida,"../files/saida.json")