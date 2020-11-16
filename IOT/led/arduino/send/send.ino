void setup()
{
  // definindo a entrada 10 do arduino
  pinMode(10, OUTPUT);
  //definindo o Baud Rate
  Serial.begin(115200);
}

void loop() {
  // Variavel para controlar o intervalo
  int intervalo_pisca;
  intervalo_pisca=4000;

  // Desligando o led
  digitalWrite(10, LOW);
  // por meio da função write escrevemos na porta serial o numero 0 que será lido pelo python
  Serial.write('0');

  // fazendo um delay/pausa 
  delay(intervalo_pisca);

  // Ligando o led
  digitalWrite(10, HIGH);
  // por meio da função write escrevemos na porta serial o numero 1 que será lido pelo python
  Serial.write('1');

  // fazendo um delay/pausa 
  delay(intervalo_pisca);
}
