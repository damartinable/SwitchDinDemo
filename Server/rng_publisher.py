import paho.mqtt.client as mqtt  # import the client1
import time
import random
import pendulum
import json


# Config needs to be improved to use a script or framework.
broker_address = "test.mosquitto.org"
broker_port = 1883
broker_topic = 'rng_example'


# Callback functions adapted from example documentation
def on_message(client, userdata, message):
    print("message received ", str(message.payload.decode("utf-8")))
    print("message topic=", message.topic)
    print("message qos=", message.qos)
    print("message retain flag=", message.retain)


def on_connect(client, userdata, flags, rc):
    print('Connected with results code ' + str(rc))


client = mqtt.Client("test server")  # create new instance
client.on_message = on_message  # attach function to callback
client.on_connect = on_connect  # attach function to callback

client.connect(broker_address, broker_port)  # connect to broker
client.subscribe(broker_topic)

# Simple loop to keep sending messages every 5 seconds. Needs a lot of improvement.
# Error handling, reconnecting, etc
while True:
    client.loop_start()  # start the loop
    print("Publishing message to topic", broker_topic)

    now = pendulum.now()
    rng = random.randint(0, 100)

    # Simple message including the random int and timestamp.
    message = {
        'timestamp': now.timestamp(),
        'rng': rng
    }

    print(message)

    client.publish(broker_topic, json.dumps(message))
    time.sleep(5)  # wait
    client.loop_stop()  # stop the loop
