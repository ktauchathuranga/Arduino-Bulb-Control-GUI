const unsigned int maxMessageLength = 12;

void setup() {

  // should use this when relay logic reversed and for avoid bootup ON OFF mess
  // digitalWrite(7, HIGH);
  
  for (int i=2; i<=13 ; i++){
    pinMode(i, OUTPUT);
  }
  Serial.begin(115200);
  Serial.println("Connection Success!");

}

// reverse the gui button state (change LOW to HIGH and so on)
void pinHigh(int pin) {
  digitalWrite(pin, HIGH);
}

void pinLow(int pin) {
  digitalWrite(pin, LOW);  
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
        pinHigh(2);
      }
      else if (myString == "22") {
        pinLow(2);
      }
      else if (myString == "3") {
        pinHigh(3);
      }
      else if (myString == "33") {
        pinLow(3);
      }
      else if (myString == "4") {
        pinHigh(4);
      }
      else if (myString == "44") {
        pinLow(4);
      }
      else if (myString == "5") {
        pinHigh(5);
      }
      else if (myString == "55") {
        pinLow(5);
      }
      else if (myString == "6") {
        pinHigh(6);
      }
      else if (myString == "66") {
        pinLow(6);
      }
      else if (myString == "7") {
        pinHigh(7);
      }
      else if (myString == "77") {
        pinLow(7);
      }
      else if (myString == "8") {
        pinHigh(8);
      }
      else if (myString == "88") {
        pinLow(8);
      }
      else if (myString == "9") {
        pinHigh(9);
      }
      else if (myString == "99") {
        pinLow(9);
      }
      else if (myString == "10") {
        pinHigh(10);
      }
      else if (myString == "1010") {
        pinLow(10);
      }
      else if (myString == "11") {
        pinHigh(11);
      }
      else if (myString == "1111") {
        pinLow(11);
      }
      else if (myString == "12") {
        pinHigh(12);
      }
      else if (myString == "1212") {
        pinLow(12);
      }
      else if (myString == "13") {
        pinHigh(13);
      }
      else if (myString == "1313") {
        pinLow(13);
      }

      
    }
  }
}
