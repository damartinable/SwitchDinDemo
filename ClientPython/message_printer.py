import paho.mqtt.client as mqtt
import pendulum

broker_address = "test.mosquitto.org"
broker_port = 1883
broker_topic = 'rng_example'


def on_connect(client, userdata, flags, rc):
    print('Connected with results code ' + str(rc))

    client.subscribe(broker_topic)


def on_message(client, userdata, msg):
    print('message received')
    now = pendulum.now()
    print(msg.topic + ' ' + str(msg.payload), now.timestamp())


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker_address, broker_port, 60)

client.loop_forever()
