from socket import *

servidor="127.0.0.1"

porta=43210

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

# No listen definimos a quantidade maxima de clientes que 
# vamos atender simultaneamente
obj_socket.listen(2)

print("Aguardando cliente....")

# 1 while = aguarda a chamada do cliente por meio do accept()
# recebe uma tupla, guardando a identificação da cnecão na var con
# e a identificação do cliente na var cliente
while True:
    con, cliente = obj_socket.accept()
    print("Conectado com: ", cliente)

    # 2 while = aguarda a solicitação do cliente que pode ser transmitida em 
    # pacote 1024 bytes atraves da recv()
    ## Exibi a mensagem recebida e em seguida geramos uma 
    # mensagem em bytes usando o b no inicio fora da string
    ## Então a mensagem pe enviada atraves do send()
    while True:
        msg_recebida = str(con.recv(1024))

        # transform a resposta em string e faz um slice pegando
        # o segundo caracter ate o ultimo, para retirar o b que vem na frente
        print("Recebemos: ", str(msg_recebida)[2:-1])

        #Cria a mensagem para enviar em bytes
        msg_enviada = bytes(input('Resposta: '), 'utf-8')

        #Envia a mensagem atraves do send()
        con.send(msg_enviada)
        break
    
    #Fecha a conexão
    con.close()


# Todos os dados transmitidos pelo socket devem estar em bytes, ele não envia
# nem recebe dados em outros formatos, exemplo, string