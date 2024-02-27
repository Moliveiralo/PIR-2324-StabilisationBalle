/**
*@brief This program permits to receive a [3x1] array from Simulink and write the values to 3 servos
*@see https://github.com/leomariga/Simulink-Arduino-Serial
**/
#include <Servo.h>
#define SIMULINK_DELAY 200 // Same delay as the Zero order hold in Simulink
Servo servo1;  // Define servo objects
Servo servo2;
Servo servo3;
// Create a union to easily convert float to byte
typedef union {
  float number;
  uint8_t bytes[4];
} FLOATUNION_t;

// Create the variable you want to send
FLOATUNION_t S1;
FLOATUNION_t S2;
FLOATUNION_t S3;

void setup() {
  // initialize serial, use the same boudrate in the Simulink Config block
  Serial.begin(115200);
  servo1.attach(3);  // Attach servo objects to pins
  servo2.attach(4);
  servo3.attach(5);
}
void loop() {
  S1.number = getFloat();
  S2.number = getFloat();
  S3.number = getFloat();
  servo1.write((int)S1.number);
  servo2.write((int)S2.number);
  servo3.write((int)S3.number);
  delay(SIMULINK_DELAY);
}


int getFloat(){
  int cont = 0;
  FLOATUNION_t f;
  while (cont < 4 ){
    f.bytes[cont] = Serial.read() ;
    cont++;  
  }
  return f.number;
}
