import paho.mqtt.client as mqtt
import pendulum
import json

broker_address = "test.mosquitto.org"
broker_port = 1883
broker_topic = 'rng_example'


# Callback functions adapted from example documentation
def on_connect(client, userdata, flags, rc):
    print('Connected with results code ' + str(rc))

    client.subscribe(broker_topic)


def on_message(client, userdata, msg):
    now = pendulum.now()
    data = json.loads(msg.payload)

    print_string = 'Message topic {0}, Random number generated: {1}, Sent timestamp: {2},' \
                   ' Received timestamp: {3}'.format(msg.topic, data['rng'], data['timestamp'], now.timestamp())
    print(print_string)


# Init the client
client = mqtt.Client()

# Register callbacks
client.on_connect = on_connect
client.on_message = on_message

# Connect to broker address.
client.connect(broker_address, broker_port, 60)

# Simple demonstrative loop, needs a huge amount of improvement and features,
# reconnecting, errors, etc.
client.loop_forever()
