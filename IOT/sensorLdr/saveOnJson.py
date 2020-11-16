import serial
import json
import time
from datetime import datetime

conexao = serial.Serial("COM3", 115200)

dicionario={}
cont=0
while cont<10:
    resposta = conexao.readline()
    dicionario[str(datetime.now())]=[resposta.decode('utf-8')[0:3]]
    print(resposta.decode('utf-8')[0:3])
    cont+=1
    
with open('Temperatura.json', "w") as arq:
    json.dump(dicionario, arq)

#Fecha a conexão
conexao.close()
print("Conexão encerrada")