const hostname = 'test.mosquitto.org';
const port = '8080';
const topic = 'rng_example';

// Generate a random client id
clientID = "clientID_" + parseInt(Math.random() * 10000);

// Create a client instance
client = new Paho.MQTT.Client(hostname, Number(port), clientID);

// set callback handlers
client.onConnectionLost = onConnectionLost;
client.onMessageArrived = onMessageArrived;

// connect the client
client.connect({onSuccess:onConnect});


// called when the client connects
function onConnect() {
  // Once a connection has been made, make a subscription and send a message.
  console.log("onConnect");
  client.subscribe(topic);
}

// called when the client loses its connection
function onConnectionLost(responseObject) {
  if (responseObject.errorCode !== 0) {
    console.log("onConnectionLost:"+responseObject.errorMessage);
  }
}

// called when a message arrives
function onMessageArrived(message) {
  // console.log("onMessageArrived:"+message.payloadString);
  let data = JSON.parse(message.payloadString);
  let height = Number(data.rng);
  console.log(height);
  $("#my-rect").velocity({ width: 100, height: height });
}