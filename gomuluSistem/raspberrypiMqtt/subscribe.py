import paho.mqtt.client as mqtt

import httplib, urllib
import time

from BrickPi import *   
import math

MQTT_BROKER = "192.168.43.209"
MQTT_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 45
MQTT_TOPIC = "hello/world"

def tarti(deger):
      
          
                                         
                        params = urllib.urlencode({'field1': deger, 'key':'V762AB4ASZUMQIUB'})   
                        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
                        conn = httplib.HTTPConnection("api.thingspeak.com:80")
                        
                        try:
                                conn.request("POST", "/update", params, headers)
                                response = conn.getresponse()
                                
                                conn.close()
                        except:
                                print "connection failed"
               


def on_connect(mosq,obj,rc):
    mqttc.subscribe(MQTT_TOPIC, 0)

def on_subscribe(mosq, obj, mid, granted_qos):
    print "Subscribed to MQTT Topic"

def on_message(mosq,obj,msg):
    print msg.payload #deger
    tarti(msg.payload)


mqttc = mqtt.Client()

mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe

mqttc.connect(MQTT_BROKER, MQTT_PORT,MQTT_KEEPALIVE_INTERVAL)

mqttc.loop_forever()
