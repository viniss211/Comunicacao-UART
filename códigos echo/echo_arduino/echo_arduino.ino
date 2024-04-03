String receivedMessage = ""; // Variável para armazenar a mensagem recebida

void setup() {
  Serial.begin(9600); // Inicia a comunicação serial
  while (!Serial) {
    ; // Aguarda até que a porta serial esteja pronta
  }
}

void loop() {
  // Se houver dados disponíveis para leitura na porta serial
  if (Serial.available() > 0) {
    receivedMessage = Serial.readStringUntil('\n'); // Lê a mensagem recebida
    Serial.println("Recebi sua mensagem: '" + receivedMessage + "'"); // Mostra a mensagem recebida
    // Envia uma resposta para o Python
    
    
    receivedMessage = ""; // Limpa a mensagem recebida
  }
}
