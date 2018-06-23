int state = 0;
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
  Serial.println("ready");
}

void left1(int del) //turns right
  {   digitalWrite(10, HIGH);
      digitalWrite(9, LOW);
      digitalWrite(5,HIGH);
      digitalWrite(6,LOW);
      delay(del);
      digitalWrite(9,LOW);
      digitalWrite(10,LOW);
      digitalWrite(5,LOW);
      digitalWrite(6,LOW);
      delay(10);
  }
void left2(int del) //moves forward
  {   digitalWrite(9,HIGH);
      digitalWrite(10,LOW);
      digitalWrite(5,HIGH);
      digitalWrite(6,LOW);
      delay(del);
      digitalWrite(9,LOW);
      digitalWrite(10,LOW);
      digitalWrite(5,LOW);
      digitalWrite(6,LOW);
      delay(10);
  }
void right1(int del) //turns left
  {   digitalWrite(10, LOW);
      digitalWrite(9, HIGH);
      digitalWrite(5,LOW);
      digitalWrite(6,HIGH);
      delay(del);
      digitalWrite(9,LOW);
      digitalWrite(10,LOW);
      digitalWrite(5,LOW);
      digitalWrite(6,LOW);
      delay(10);
  }
void right2(int del) //moves forward
  {   digitalWrite(9,HIGH);
      digitalWrite(10,LOW);
      digitalWrite(5,HIGH);
      digitalWrite(6,LOW);
      delay(del);
      digitalWrite(9,LOW);
      digitalWrite(10,LOW);
      digitalWrite(5,LOW);
      digitalWrite(6,LOW);
      delay(10);
  }

void loop() {
  int cmd = Serial.read();
  switch(cmd) {
    case 119: //forward
      Serial.println("W");
      digitalWrite(9,HIGH);
      digitalWrite(10,LOW);
      digitalWrite(5,HIGH);
      digitalWrite(6,LOW);
      break;
    case 97: //left
      Serial.println("A");
      digitalWrite(9,HIGH);
      digitalWrite(10,LOW);
      digitalWrite(6,HIGH);
      digitalWrite(5,LOW);
      break;
    case 115: //back
      Serial.println("S");
      digitalWrite(10,HIGH);
      digitalWrite(9,LOW);
      digitalWrite(6,HIGH);
      digitalWrite(5,LOW);
      break;
    case 100: //right
      Serial.println("D");
      digitalWrite(10, HIGH);
      digitalWrite(9, LOW);
      digitalWrite(5,HIGH);
      digitalWrite(6,LOW);
      break;
    case 120: //stop
      Serial.println("X");
      digitalWrite(9,LOW);
      digitalWrite(10,LOW);
      digitalWrite(5,LOW);
      digitalWrite(6,LOW);
      break;
    case 48: //special
      Serial.println("0");
      if (state == 0)
      {
          left1(500);
          left2(1600);
          right1(800);
          right2(3100);
      }
      
      break;
    
    default:
      break;
  }
}
