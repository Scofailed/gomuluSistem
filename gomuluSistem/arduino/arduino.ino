#include <SoftwareSerial.h>

#include "hx711.h"

SoftwareSerial ArduinoSerial(15,14);


Hx711 scale(A1, A0);


float offset= -24.5;
int weight = 0;


void setup()  
{
  Serial.begin(9600);
  ArduinoSerial.begin(4800);

  scale.setOffset(8366402);
  scale.setScale(83.457f);
  delay(500);
}

void loop()
{

  weight = offset - scale.getGram();
  if(weight<0)
    weight = 0;
  
  ArduinoSerial.print(weight);
  
  Serial.print(weight);
  Serial.println(" gram");
  delay(50);
}
