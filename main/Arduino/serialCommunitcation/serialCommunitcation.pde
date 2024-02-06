void setup() {
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    String receivedMessage = Serial.readStringUntil('\n');
    Serial.println("Boom- Roasted");
    
    if (receivedMessage == "Hello Arduino!") {
      Serial.println("GOOD!");
    }
    
    // Print the received message
    Serial.println("GOOD!");
  }
}