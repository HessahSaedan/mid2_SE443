import paho.mqtt.client as mqtt
import json
broker_address= "10.20.1.95"
# This is the Publisher
client = mqtt.Client()
topic = "se443/midterm2"
message = '{ "name":"hissah", "surname":saidan,"id":201394, "telephone":"0530841191", "grade":100}'

if (client.connect(broker_address,1883,60) ==0):
	print ("Connected succesfully to "+broker_address)
	
client.publish(topic, message)
print ("Published in "+topic+", msg = "+message)
client.disconnect();