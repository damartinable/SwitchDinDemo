import paho.mqtt.client as mqtt  # import the client1
import time
import random
import pendulum
import json


def on_message(client, userdata, message):
    print("message received ", str(message.payload.decode("utf-8")))
    print("message topic=", message.topic)
    print("message qos=", message.qos)
    print("message retain flag=", message.retain)


def on_connect(client, userdata, flags, rc):
    print('Connected with results code ' + str(rc))


broker_address = "test.mosquitto.org"
broker_port = 1883
broker_topic = 'rng_example'

# print("creating new instance")
client = mqtt.Client("test server")  # create new instance
client.on_message = on_message  # attach function to callback
client.on_connect = on_connect
# print("connecting to broker")

client.connect(broker_address, broker_port)  # connect to broker

print("Subscribing to topic", broker_topic)
client.subscribe(broker_topic)

while True:
    client.loop_start()  # start the loop
    print("Publishing message to topic", broker_topic)

    now = pendulum.now()
    rng = random.randint(0, 100)
    print(rng)

    message = {
        'timestamp': now.timestamp(),
        'rng': rng
    }

    print(message)

    client.publish(broker_topic, json.dumps(message))
    time.sleep(30)  # wait
    client.loop_stop()  # stop the loop
