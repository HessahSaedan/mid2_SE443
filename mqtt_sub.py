import time
import paho.mqtt.client as paho
import json
broker= "10.20.1.95"

def on_message(client, userdata, message):
    time.sleep(1)
    y = json.loads(message.payload)
    print("received message =")
    print("y['name']=", y["name"]) 
    print("y['surname']=", y["surname"])
    print("y['id']=", y["id"])  
    print("y['telephone']=", y["telephone"]) 
    print("y['grade']=", y["grade"]) 
    

client= paho.Client() #create client object 

client.on_message=on_message
#####
print("connecting to broker ",broker)
client.connect(broker)#connect
client.loop_start() #start loop to process received messages
print("subscribing ")
client.subscribe("se443/midterm2")#subscribe
while(True):
	client.on_message=on_message
