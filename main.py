import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))


def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed to topic with QoS: " + str(granted_qos[0]))


def on_message(client, userdata, message):
    print("Received message: "+str(message.payload.decode()))

# creating publisher and subscriber client
publisher = mqtt.Client(client_id="publisher_client")
subscriber = mqtt.Client(client_id="subscriber_client")
subscriber2 = mqtt.Client(client_id="subscriber_client")



#connect publisher to mosquitto broker
publisher.connect("localhost", port=1883)


#connect subscriber to mosquitto broker and subscribe
subscriber.connect("localhost", port=1883)
subscriber2.connect("localhost", port=1883)
subscriber.subscribe("CyberSec/IKT520")
subscriber2.subscribe("CyberSec/IKT520/+/+")

# Set up callbacks for events
publisher.on_connect = on_connect
subscriber.on_connect = on_connect
subscriber.on_subscribe = on_subscribe
subscriber.on_message = on_message

subscriber2.on_connect = on_connect
subscriber2.on_subscribe = on_subscribe
subscriber2.on_message = on_message

# Publish a message to the topic CyberSec/IKT520
publisher.publish("CyberSec/IKT520", "Hi", qos=0, retain=True)
publisher.publish("CyberSec/IKT520/assignment5/one", "this is a test", qos=0, retain= True)
publisher.publish("CyberSec/IKT520/assignment5/two", "this is a test2", qos=0, retain= True)

#making sure the client does not disconnect

subscriber.loop_start()
subscriber2.loop_start()

# Keep the main thread alive
while True:
    pass