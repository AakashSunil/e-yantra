#include <Servo.h>
Servo s1;
const unsigned int mapping[4][20] = {
  {3, 10, 18, 25, 32, 40, 48, 56, 64, 71, 81, 88, 96, 104, 112, 121, 129, 138, 146, 154}, 
  {4, 14, 24, 34, 44, 54, 64, 74, 84, 96, 108, 120, 130, 140, 154, 0, 0, 0, 0, 0},
  {6, 22, 36, 52, 66, 84, 102, 120, 140, 156, 0 , 0, 0, 0, 0, 0, 0, 0, 0, 0},
  {18, 54, 96, 138, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}
};
void setup() {
  // put your setup code here, to run once:
  //Serial.begin(9600);
  s1.attach(14);
  s1.write(0);
  delay(5000);
  /*delay(1000);
  for(int i = 0; i < 20; i++)
  {
    s1.write(mapping[0][i]);
    delay(1000);
  }*/
  
  /*for(int i = 0; i < 180; i = i + 5)
  {
    s1.write(i);
    delay(100);
  }*/
  s1.write(180);
  delay(3000);
  s1.write(0);
  
  
  /*delay(500);
  s1.write(0);
  delay(500);
  for(int i = 0; i < 20; i++)
  {
    //Serial.printf("%d     %d\n", i+1, mapping[0][i]);
    s1.write(mapping[0][i]);
    delay(5000);
  }*/
}

void loop() {
}
