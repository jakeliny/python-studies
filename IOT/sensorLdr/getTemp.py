import serial

#conecta na porta COM3 (usb no win) e le a porta serial 115200
conexao = serial.Serial("COM3", 115200)

while True:
    # Lemos a resposta com readline() devido a quantidade 
    # de dados ser inderteminada
    resposta = conexao.readline()

    # Exibimos o que foi lido da porta serial com decode()
    # que transforma byte em string
    print(resposta.decode())
    
#Fecha a conexão
conexao.close()
print("Conexão encerrada")