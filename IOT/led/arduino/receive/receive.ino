void setup() {
  // definindo a entrada 10 do arduino
  pinMode(10, OUTPUT);
  //definindo o Baud Rate
  Serial.begin(115200);
}

void loop() {
  // criando a variavel para receber o conteudo da porta serial
  int valor_recebido;

  //se houver uma serial
  if(Serial.available()){
    
    //Lendo o conteudo da porta serial
    valor_recebido = Serial.read();

    //Se for 0 desliga o led, diferente disso liga o LED
    if(valor_recebido=='0'){
    digitalWrite(10, LOW);
  }else{
    digitalWrite(10, HIGH);
  }
  }
}
