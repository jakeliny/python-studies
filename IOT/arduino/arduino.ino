void setup() {
  pinMode(10, OUTPUT);
  Serial.begin(115200);
}

void loop() {
  int valor_recebido;
  if(Serial.available()){
    valor_recebido = Serial.read();
    if(valor_recebido=='0'){
    digitalWrite(10, LOW);
  }else{
    digitalWrite(10, HIGH);
  }
  }
}
