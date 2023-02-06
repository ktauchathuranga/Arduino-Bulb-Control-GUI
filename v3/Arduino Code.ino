const unsigned int maxMessageLength = 12;

void setup() {
  for (int i=2; i<=13 ; i++){
    pinMode(i, OUTPUT);
  }
  Serial.begin(76800);
  Serial.println("Connection Success!");
  // put your setup code here, to run once:

}

void loop() {
  while (Serial.available() > 0) {
    static char message[maxMessageLength];
    static unsigned int messagePos = 0;

    char inByte = Serial.read();
    if (inByte != '\n' && (messagePos < maxMessageLength - 1)) {
      message[messagePos] = inByte;
      messagePos++;
    }
    else {
      message[messagePos] = '\0';
      Serial.println(message);
      String myString(message);
      messagePos = 0;

      if (myString == "2") {
        digitalWrite(2, HIGH);
      }
      else if (myString == "22") {
        digitalWrite(2, LOW);
      }
      else if (myString == "3") {
        digitalWrite(3, HIGH);
      }
      else if (myString == "33") {
        digitalWrite(3, LOW);
      }
      else if (myString == "4") {
        digitalWrite(4, HIGH);
      }
      else if (myString == "44") {
        digitalWrite(4, LOW);
      }
      else if (myString == "5") {
        digitalWrite(5, HIGH);
      }
      else if (myString == "55") {
        digitalWrite(5, LOW);
      }
      else if (myString == "6") {
        digitalWrite(6, HIGH);
      }
      else if (myString == "66") {
        digitalWrite(6, LOW);
      }
      else if (myString == "7") {
        digitalWrite(7, HIGH);
      }
      else if (myString == "77") {
        digitalWrite(7, LOW);
      }
      else if (myString == "8") {
        digitalWrite(8, HIGH);
      }
      else if (myString == "88") {
        digitalWrite(8, LOW);
      }
      else if (myString == "9") {
        digitalWrite(9, HIGH);
      }
      else if (myString == "99") {
        digitalWrite(9, LOW);
      }
      else if (myString == "10") {
        digitalWrite(10, HIGH);
      }
      else if (myString == "1010") {
        digitalWrite(10, LOW);
      }
      else if (myString == "11") {
        digitalWrite(11, HIGH);
      }
      else if (myString == "1111") {
        digitalWrite(11, LOW);
      }
      else if (myString == "12") {
        digitalWrite(12, HIGH);
      }
      else if (myString == "1212") {
        digitalWrite(12, LOW);
      }
      else if (myString == "13") {
        digitalWrite(13, HIGH);
      }
      else if (myString == "1313") {
        digitalWrite(13, LOW);
      }

      
    }
  }
}
