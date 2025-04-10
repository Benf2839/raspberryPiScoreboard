import paho.mqtt.client as mqtt

# Define the MQTT callback functions
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("tennis/scoreboard")  # Subscribe to the topic

def on_message(client, userdata, msg):
    print(f"Message received: {msg.payload.decode()}")
    # Update the scoreboard based on the message

# Initialize the client
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Connect to the broker
client.connect("broker_ip_address", 1883, 60)

# Start the MQTT loop
client.loop_start()
