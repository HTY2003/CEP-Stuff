#define p(x) Serial.print(x)
#define pl(x) Serial.println(x)
#define sb Serial.begin(9600)
#define in(x) pinMode(x, INPUT)
#define rd(x) analogRead(x)
#define aw(x,y) analogWrite(x, y)
#define d(x) delay(x*1000)

int data_l, data_r, lb_max, rb_max;
int lw_final, rw_final, lb_final, rb_final, state = 0;

void setup() {
  sb;
  in(A0); in(A1);
  pl("Initialised LDR");
}

void loop() {
  int cmd = Serial.read();
  switch (cmd) {
    case 103: //forward
      if (state == 0) {
        Serial.println("Put the left and right sensors on white terrain. Press G to continue...");
        state = 1;
      }
      else if (state == 1) {
        Serial.println("Collecting data...");
        for (int i = 0; i < 10; i++) {
          data_l = rd(A0);
          data_r = rd(A1);
          lw_final += data_l;
          rw_final += data_r;
          p("left: ");
          p(data_l);
          p(", right: ");
          pl(data_r);
        }
        state = 0;
      }

      break;
    case 104:
      if (state == 0) {
        Serial.println("Put the left and right sensors on black terrain. Press H to continue...");
        state = 1;
      }
      else if (state == 1) {
        Serial.println("Collecting data...");
        for (int i = 0; i < 10; i++) {
          data_l = rd(A0);
          data_r = rd(A1);
          lb_final += data_l;
          rb_final += data_r;
          p("left: ");
          p(data_l);
          p(", right: ");
          pl(data_r);
        }
        state = 0;
      }
      break;
    case 106: //forward
      if (state == 0) {
        Serial.println("Put the left and right sensors on black and white terrain respectively. Press J to continue...");
        state = 1;
      }
      else if (state == 1) {
        Serial.println("Collecting data...");
        for (int i = 0; i < 10; i++) {
          data_l = rd(A0);
          data_r = rd(A1);
          lb_final += data_l;
          rw_final += data_r;
          p("left: ");
          p(data_l);
          p(", right: ");
          pl(data_r);
        }
        state = 0;
      }
      break;
    case 107: //forward
      if (state == 0) {
        Serial.println("Put the left and right sensors on white and black terrain respectively. Press K to continue...");
        state = 1;
      }
      else if (state == 1) {
        Serial.println("Collecting data...");
        for (int i = 0; i < 10; i++) {
          data_l = rd(A0);
          data_r = rd(A1);
          lw_final += data_l;
          rb_final += data_r;
          p("left: ");
          p(data_l);
          p(", right: ");
          pl(data_r);
        }
        state = 0;
      }
      break;
    case 120:
      Serial.println("X!");
      lb_final /= 20;
      lw_final /= 20;
      rb_final /= 20;
      rw_final /= 20;
      lb_max = lb_final + (lw_final - lb_final) / 2 ;
      rb_max = rb_final + (rw_final - rb_final) / 2 ;
      p("Left Black Max:");
      p(lb_max);
      p("Right Black Max:");
      p(rb_max);
      break;
      
    default:
      break;
  }

}

