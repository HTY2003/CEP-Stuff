#define p(x) Serial.print(x)
#define pl(x) Serial.println(x)
#define sb Serial.begin(9600)
#define out(x) pinMode(x, OUTPUT)
#define in(x) pinMode(x, INPUT)
#define low(x) digitalWrite(x, LOW)
#define high(x) digitalWrite(x, HIGH)
#define rd(x) analogRead(x)
#define aw(x,y) analogWrite(x, y)
#define d(x) delay(x*1000)
#define fl(v) high(4); aw(5, 255-v); // left motor forward
#define bl(v) low(4); aw(5, v); //left motor back
#define fr(v) high(8); aw(9, 255-v*1.01); //right motor forward
#define br(v) low(8); aw(9, v); //right motor back
#define f(v) fl(v); fr(v); //move forward (sort of)
#define b(v) bl(v); br(v); //move backwards
#define rr(v) fl(v); br(v); //turn right
#define rl(v) fr(v); bl(v); //turn left
#define frl(v) high(4); high(8); aw(5, 255-v); aw(9, 255-1.4*v); // forward + rotate left
#define frr(v) high(4); high(8); aw(5, 255-1.4*v); aw(9, 255-v); //forward + rotate right
#define brl(v) low(4); low(8); aw(5, v); aw(9, 1.1*v); //backward + rotate left
#define brr(v) low(4); low(8); aw(5, 1.1*v); aw(9, v); //backward + rotate right
#define black_l (data_l < 752) //put left black max here
#define black_r (data_r < 791) //put right black max here
#define st_r fr(0);
#define st_l fl(0);
#define st() f(0); // stop both motor

int data_l, data_r, state;

void setup() {
  sb;
  out(4); out(5); // left
  pl("Initialised left motor...");
  out(8); out(9); // right
  pl("Initialised right motor...");
  in(A0); in(A1);
  pl("Initialised LDR sensors...");
}

void loop() {
  data_l = rd(A0);
  data_r = rd(A1);
  p(data_l);
  pl(data_r);
  if (!black_l && !black_r) { //state 0: LWBW
    fl(195);
    d(0.1);
    st();
    d(0.01);
    state = 0;
  }
  else if (!black_l && black_r) { //state 1: LWBR
    if (state != 1) {
      fl(190);
      d(0.3);
      st();
      d(0.01);
      state = 1;
    }
    else {
      fl(195);
      d(0.1);
      st();
      d(0.01);
    }
  }
  else if (black_l && !black_r) { //state 2: LBRW
    if (state != 2) {
      fr(190);
      d(0.4);
      st();
      d(0.01);
      state = 2;
    }
    else {
      fr(195);
      d(0.1);
      st();
      d(0.01);
    }
  }
  else if (black_l && black_r) { //state 3(not input as a state since it's "recovery mode" :LBRB
    if (state == 0) {
      fr(200);
      d(0.1);
      st();
      d(0.01);
    }
    else if (state == 1) {
      fl(195);
      d(0.1);
      st();
      d(0.01);
    }
    else if (state == 2) {
      fr(195);
      d(0.1);
      st();
      d(0.01);
    }
  }
}
