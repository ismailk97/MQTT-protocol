# MQTT-protocol
This was a school project mandatory assignment, 
simulating several  instances  of  the  MQTT  protocol.  
The  documentation in https://pypi.org/project/paho-mqtt/ 
will assist you in implementing the protocol  using Python.   

I used Eclipse Mosquitto as the broker for the MQTT protocol.


MQTT is a messaging protocol used for sending and receiving data between different devices.
It's designed to work well in situations where the network connection might not be great, like when you're using a mobile phone or a satellite connection.
The way it works is that one device sends a message to a "broker," which is like a central hub that receives all the messages. 
Then, any other devices that are interested in receiving that message can subscribe to it and the broker will send it to them.
This is useful because it means that devices can communicate with each other without needing to know the specifics of who they're talking to or where they are. 
It's like sending a message out into the world and having anyone who's interested in hearing it be able to listen in.


Assigment description:
1. Use the paho-mqtt library and create two clients (publisher and a subscriber). Discuss the 
meanings of the arguments that you have used when creating clients. 
 
2. Connect the publishing client to a Broker. Use the on_connect method to observe the CONNACK 
reply from the Broker. What do the arguments on the on_connect function mean?    
 
3. Connect the subscribing client to the Broker. Make a subscription to the topic CyberSec/IKT520. 
Use the on_subscription function to investigate about the SUBACK reply from the Broker. 
 
4. Publish a message to the topic CyberSec/IKT520. What are the meanings of the arguments that 
you have used in the PUBLISH message. Check whether the published message is received by the 
subscribing client. 
 
5. Make two subscriptions with 1 being a single-level wild card and the other with a multi-level wild 
card. Then, make several publishing and thereby explain how the wild card subscriptions 
operate.   
 
6. Create a client and connect to the Broker with clean session set to FALSE. Then, subscribe to the 
topic Sensor/Temp with QoS 1. Disconnect the subscriber. Create another client and publish 20 
messages to the topic Sensor/Temp with QoS 1. Reconnect the subscriber. What is your 
observation? Give reasons for your observation. 
 
7. Create a client and connect to the Broker with clean session set to TRUE. Then, subscribe to the 
topic Sensor/Temp with QoS 1. Disconnect the subscriber. Create another client and publish 20 
messages to the topic Sensor/Temp with QoS 1. Reconnect the subscriber. What is your 
observation? Give reasons for your observation. 
 
8. Create a client and connect to the Broker with clean session set to FALSE. Then, subscribe to the 
topic Sensor/Temp with QoS 0. Disconnect the subscriber. Create another client and publish 20 
messages to the topic Sensor/Temp with QoS 2. Reconnect the subscriber. What is your 
observation? Give reasons for your observation.

