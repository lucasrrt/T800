#include<Servo.h>

Servo servo1;
Servo servo3;
Servo servo4;
Servo servo5;
Servo servo6;

int angle1 = 0;
int angle3 = 0;
int angle4 = 0;
int angle5 = 0;
int angle6 = 0;
String string;

bool closedHand = false;

void setup() {
  // put your setup code here, to run once:
  Ciao.begin(); 
  
  servo1.attach(10);
  servo3.attach(11);
  servo4.attach(9);
  servo5.attach(12);
  servo6.attach(13);
  
  Serial.begin(9600);
  Serial.println("Lendo dados do sensor...");
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available()){
    angle1 = Serial.readStringUntil(';');
    angle4 = Serial.readStringUntil(';');
    angle5 = Serial.readStringUntil(';');
    closeHand = Serial.readStringUntil(';');
    
    //angle6 = closedHand?90:0;
  }
//  servo1.write(angle1);
//  servo3.write(angle3);
//  servo4.write(angle4);
//  servo5.write(angle5);
//  servo6.write(angle6);


  
  delay(1000);
}
