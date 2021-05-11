import time
import paho.mqtt.client as paho
broker="test.mosquitto.org"
# broker="iot.eclipse.org"
#define callback
def on_message(client, userdata, message):
    print("received message =",str(message.payload.decode("utf-8")))

client= paho.Client("client-001") #create client object client1.on_publish = on_publish #assign function to callback client1.connect(broker,port) #establish connection client1.publish("house/bulb1","on")
######Bind function to callback

#####
print("connecting to broker ",broker)
client.connect(broker)#connect
client.loop_start() #start loop to process received messages

print("subscribing ")
client.subscribe("ICS_TI")#subscribe

i=0

while(1):
    i+=1
    client.publish("ICS",i)#publish
    time.sleep(1)
    client.on_message=on_message
    print(i)