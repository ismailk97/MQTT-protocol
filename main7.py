import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))


def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed to topic with QoS: " + str(granted_qos[0]))


def on_message(client, userdata, message):
    print("Received message: "+str(message.payload.decode()))


#create client and subscribe to sensor/temp
subscriber = mqtt.Client(client_id="subscriber_client", clean_session=True)
subscriber.connect("localhost", port=1883)
subscriber.on_connect = on_connect
subscriber.on_subscribe = on_subscribe
subscriber.on_message = on_message
subscriber.subscribe("Sensor/Temp", qos=1)
time.sleep(5)

subscriber.disconnect()


publisher = mqtt.Client(client_id="publisher_client")
publisher.connect("localhost", port=1883)

for i in range(20):
    publisher.publish("Sensor/Temp", "Temperature: "+str(i), qos=1)

# reconnecting subscriber
subscriber.connect("localhost", port=1883)

subscriber.loop_forever()