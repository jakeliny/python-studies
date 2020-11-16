import serial

#Conecta na porta COM3 (windows)
conexao = serial.Serial("COM3", 115200, timeout=0.5)

acao=input("Digite: \n<L> para Ligar \n<D> para Desligar: ").upper()
while acao=="L" or acao=="D":
    
    if acao=="L":
        #envia 1 em bytes para o arduinno
        conexao.write(b'1')
    else:
        #envia 0 em bytes para o arduinno
        conexao.write(b'0')
    
    acao=input("Digite: \n<L> para Ligar \n<D> para Desligar: ").upper()

#Fecha a conexão
conexao.close()
print("Conexao encerrada")
