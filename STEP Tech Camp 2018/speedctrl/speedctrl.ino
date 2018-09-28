void setup() { 
  Serial.begin(9600);
  // Note: Using 8,9,10 and 4,5,6 as 5,6,9,10 support analogWrite (PWM)
  pinMode(8, OUTPUT); // sets pin 8 to OUTPUT
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
  digitalWrite(8, HIGH); // ENABLE always on
  // second set
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  digitalWrite(4,HIGH);
  
  digitalWrite(10,LOW); // both pins low since both motors moving one way only
  digitalWrite(6,LOW);
  Serial.println("ready");
}

void loop() {
  int cmd = Serial.read();
  switch(cmd) {
    case 103: //forward
      Serial.println("G");
      analogWrite(9,100);
      analogWrite(5,100);
      break;
    case 104: //forward
      Serial.println("H");
      analogWrite(9,150);
      analogWrite(5,150);
      break;
    case 106: //forward
      Serial.println("J");
      analogWrite(9,200);
      analogWrite(5,200);
      break;
    case 107: //forward
      Serial.println("K");
      analogWrite(9,250);
      analogWrite(5,250);
      break;
    case 120:
      Serial.println("Helloworld!");
      digitalWrite(9,LOW);
      digitalWrite(10,LOW);
      digitalWrite(5,LOW);
      digitalWrite(6,LOW);
      break;
    default:
      break;
  }
  
}
