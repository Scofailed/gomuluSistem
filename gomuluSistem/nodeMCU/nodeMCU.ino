#include <ESP8266WiFi.h>
#include <MQTTClient.h>
#include <SoftwareSerial.h>
#include <Servo.h>
// Wifi info
const char *ssid = "MyASUS";
const char *pass = "batu1234";

Servo myservomotor; 

SoftwareSerial NodeSerial(D7,D8);


WiFiClient net;
MQTTClient client;
float val = 0;

void setup()
{
  
  Serial.begin(9600);
  
  pinMode(D7, INPUT);
  pinMode(D8, OUTPUT);
  
  NodeSerial.begin(4800);

  myservomotor.attach(D5);  
  myservomotor.write(0);

  WiFi.begin(ssid, pass);
  
  // Use your Broker ip address
  client.begin("192.168.43.209", net); // Begin client with broker Ip and wifi client
 
  connect();
}
 char temp[50];
 int aci = 0;
void connect()
{
  // Connect to wifi
  Serial.print("checking wifi...");
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    delay(1000);
  }
 
  // Connect to broker
  Serial.print("\nconnecting...");
  while (!client.connect("ESP8266Sub", "try", "try")) {
    Serial.print(".");
    delay(1000);
  }
  
  Serial.println("\nconnected!");
  client.subscribe("/hello/eklemeMiktari");
}
 

void loop() {
  
  if(NodeSerial.available()>0){
    val = NodeSerial.parseFloat();
    Serial.println(val);
    int a = val;
    
    sprintf(temp,"%d", a);
    client.publish("/hello/world",temp);
 
  }

  delay(200);
  client.loop();
  delay(10); //wifi stability

}
 
// Send incoming topic messages over uart
void messageReceived(String topic, String payload, char * bytes, unsigned int length) {
  
  Serial.println(payload);
  int sefer = 0; 
  if(payload == "50"){
    sefer = 1;
  }else if(payload == "100"){
    sefer = 2;
  }else if (payload == "150"){
    sefer = 3;
  }else if(payload == "200"){
    sefer = 4;
  }else if(payload == "250"){
    sefer = 5;
  }else{
    Serial.print("Hatalı veri geldi");
  }

  for(int i = 0; i < sefer ; i++){
    for(aci = 0; aci<=180;aci++){
       myservomotor.write(aci);
       delay(30);
    }
    delay(100);
    myservomotor.write(120);
    delay(100);
    myservomotor.write(180);
    delay(1000);
    for(aci = 180; aci>=0; aci=aci-1){
        myservomotor.write(aci);
        delay(10);
    }

  delay(1000); 
  
  }
}
