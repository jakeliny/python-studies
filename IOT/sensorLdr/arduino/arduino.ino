void setup() {
  // definindo a porta serial
  Serial.begin(115200);
}
void loop() {
  
  // Variavel luz que le a porta analogica 1 do arduino (A1)
  int luz=analogRead(1); 

  // Grava na porta serial o valor recebido do sensor conectado na A1
  // Usando println ao inves de write devido a não sabermos 
  // a quantidade de caracteres que vamos receber
  Serial.println(luz);

  //Delay/tempo
  delay(5000); 
}
