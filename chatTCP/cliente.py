from socket import *

#defininfo ip e porta
servidor="127.0.0.1"
porta=43210

while True:

    ## Criamos nosso obj socket
    ## Primeiro paramento é a familia responsavel por identificar 
    # os pacotes, AF_INET = emissor/receptor do pacote via DNS ou IP
    # poderiamos usar AF_UNIX que muda a forma de identificação
    ## Segundo parametro é o transporte do pacote
    # SOCK_STREAM = TCP
    # SOCK_DGRAM = UDP
    obj_socket = socket(AF_INET, SOCK_STREAM)

    # Fazemos a associação com o servidor e porta
    obj_socket.bind((servidor,porta))

    #Criando a mensagem em bytes
    msg = bytes(input("Digite algo: "), 'utf-8')

    #envia a mensagem pelo send()
    obj_socket.send(msg)

    #receber a resposta pelo recv() limitando a 1024 bytes
    resposta=obj_socket.recv(1024)

    # transform a resposta em string e faz um slice pegando
    # o segundo caracter ate o ultimo, para retirar o b que vem na frente
    print("Resposta: ", str(resposta)[2:-1])

#Fecha a conexão
obj_socket.close()