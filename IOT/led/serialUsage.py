import serial

# primeiro parametro = saida serial do arduino
## no win COM1, COM2
## no linux /dev/ttyUSB0 /dev/ttyUSB1
# segundo paramento = Baud Rate = capacidade de transmissão de bits por segundo
## os dispositivos conectados devem estar na mesma faixa de transmissão
conexao = serial.Serial('COM3', 115200)