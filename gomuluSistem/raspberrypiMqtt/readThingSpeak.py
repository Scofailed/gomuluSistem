#!/usr/bin/env python

import urllib2,json
import paho.mqtt.client as mqtt
import httplib, urllib
import time

from BrickPi import *  


READ_API_KEY='GVK26Z5OPZLFO8HB'
CHANNEL_ID=265493

MQTT_BROKER = "192.168.43.209"
MQTT_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 45
MQTT_TOPIC = "hello/button"
MQTT_TOPIC2 = "hello/eklemeMiktari"
MQTT_MSG = "1"

def main():
   
    while(1):
         conn = urllib2.urlopen("http://api.thingspeak.com/channels/%s/feeds/last.json?api_key=%s" \
                           % (CHANNEL_ID,READ_API_KEY))
         response = conn.read()
         data=json.loads(response)
         if data['field2'] == '1':
             print "button basıldı"
             mqttc = mqtt.Client()
             mqttc.connect(MQTT_BROKER, MQTT_PORT,MQTT_KEEPALIVE_INTERVAL)
             mqttc.publish(MQTT_TOPIC, MQTT_MSG)          
             mqttc.disconnect()
             mqttc = mqtt.Client()
             mqttc.connect(MQTT_BROKER, MQTT_PORT,MQTT_KEEPALIVE_INTERVAL)
             veri = data['field3']
             print veri
             mqttc.publish(MQTT_TOPIC2, veri)
             mqttc.disconnect()
                   
             print "veri gönderildi"
             time.sleep(16)
             params = urllib.urlencode({'field2': 0, 'key':'V762AB4ASZUMQIUB'})
             headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
             conn = httplib.HTTPConnection("api.thingspeak.com:80")
                        
             try:
                 conn.request("POST", "/update", params, headers)
                 response = conn.getresponse()
                 conn.close()
                 print "button sıfırlandı"
             except:
                  print "connection failed"
                               
         
         conn.close()


if __name__ == '__main__':
    main()
