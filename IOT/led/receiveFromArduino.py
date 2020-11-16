import serial
conexao = serial.Serial("COM3", 115200)

while True:
    # Lendo o conteudo da porta serial
    resposta = conexao.read()

    /# se for 1 esta ligado, diferente disso esta desligado
    if resposta==b'1':
        print("LED Ligado")
    else:
        print("LED Desligado")

#Fecha a conexão
conexao.close()
print("Conexão encerrada")
