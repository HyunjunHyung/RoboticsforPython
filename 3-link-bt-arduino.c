#include "SoftwareSerial.h"
#include "DynamixelMotor.h"

// defin Rx, Tx number
int Tx=11;   
int Rx=10;  

// define id of the motor
const uint8_t id1 = 1;
const uint8_t id2 = 2;
const uint8_t id3 = 3;
// define speed, between 0 and 1023
int16_t speed=10;
// define communication baudrate
const long unsigned int baudrate = 1000000;

SoftwareSerial BT(Tx, Rx);

HardwareDynamixelInterface interface(Serial);

DynamixelMotor motor1(interface, id1);
DynamixelMotor motor2(interface, id2);
DynamixelMotor motor3(interface, id3);

 

void setup()  
{
  interface.begin(baudrate);
  delay(100);
  
  uint8_t status=motor1.init();
  
  if(status!=DYN_STATUS_OK)
  {
    pinMode(LED_BUILTIN, OUTPUT);
    digitalWrite(LED_BUILTIN, HIGH);
    while(1);
  }
  
  motor1.enableTorque();
  motor2.enableTorque();
  motor3.enableTorque(); 

  // set to joint mode, with a 180° angle range
  // see robotis doc to compute angle values
  motor1.jointMode(204, 820);
  motor1.speed(speed);
  motor2.jointMode(204, 820);
  motor2.speed(speed);
  motor3.jointMode(204, 820);
  motor3.speed(speed);
  
  BT.begin(9600);
  BT.println("Conneted up to Arduino");
}

 

char master_input; 
void loop() 
{
  if (BT.available())
  {
    master_input=(BT.read());
    if (master_input=='1')
    {
      motor1.goalPosition(480);
      motor2.goalPosition(450);
      motor3.goalPosition(400);
      BT.println("Move Right");
      delay(500);
    }
    if (master_input=='2')
    {
      motor1.goalPosition(512);
      motor2.goalPosition(512);
      motor3.goalPosition(512);
      BT.println("Move Center");
      delay(500);
      
    }
    if (master_input=='3')
    {
      motor1.goalPosition(530);
      motor2.goalPosition(580);
      motor3.goalPosition(630);
      BT.println("Move Left");
      delay(500);
    }
  }
}
