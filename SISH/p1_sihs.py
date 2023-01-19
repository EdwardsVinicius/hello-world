import paho.mqtt.client as mqtt
import random as rnd

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("/sihs/equipe5/lum")

def on_message(client, userdata, msg):
    msg = str(msg.payload.decode('utf-8'))
    print(msg.topic+" "+str(msg.payload))

mqttc = mqtt.Client()
mqttc.on_connect = on_connect
mqttc.on_message = on_message

mqttc.connect("broker.hivemq.com", 1883)
mqttc.publish("/sihs/equipe5/lum", str(rnd.randint(10, 50)))

mqttc.loop_start()