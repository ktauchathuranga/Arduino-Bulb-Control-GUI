int value = 0;
int ledPin = 13;

void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
  Serial.println("Connection Success!");
}

void loop() {
  while (Serial.available()) {
    value = Serial.read();
  }
  if (value == '1')
    digitalWrite(ledPin, HIGH);
  else if (value == '0')
    digitalWrite(ledPin, LOW);
}