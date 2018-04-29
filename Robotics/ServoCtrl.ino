void setup() {
                  pinMode(13, OUTPUT);  //Arduino LED
                  pinMode(4, OUTPUT);  //Blue LED
                }
                void loop() {
                   digitalWrite(13,HIGH); //turn on the Arduino LED
                   digitalWrite(4,HIGH); //turn on the Blue LED
                   delay(150);
                   digitalWrite(13,LOW); //turn off the Arduino LED
                   digitalWrite(4,LOW); //turn off the Blue LED
                   delay(150);
                }

