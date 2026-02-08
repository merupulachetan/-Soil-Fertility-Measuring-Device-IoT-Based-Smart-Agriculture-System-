"""
Project: IoT-Based Soil Fertility Monitoring System
Cloud Platform: Adafruit IO
Protocol: MQTT

Description:
Reads soil data from ESP32 via Serial
Publishes data to Adafruit IO feeds.
"""

import time
import serial
from Adafruit_IO import MQTTClient

# ==============================
# CONFIGURATION
# ==============================

ADA_USERNAME = "YOUR_ADAFRUIT_USERNAME"
ADA_KEY = "YOUR_ADAFRUIT_AIO_KEY"

SERIAL_PORT = "COM3"        # Change to your port
BAUD_RATE = 9600

# Feed Names (Create these in Adafruit IO dashboard)
FEED_PH = "soil-ph"
FEED_MOISTURE = "soil-moisture"
FEED_NITROGEN = "soil-nitrogen"
FEED_PHOSPHORUS = "soil-phosphorus"
FEED_POTASSIUM = "soil-potassium"
FEED_TEMPERATURE = "soil-temperature"

# ==============================
# MQTT CALLBACKS
# ==============================

def connected(client):
    print("Connected to Adafruit IO")

def disconnected(client):
    print("Disconnected from Adafruit IO")
    exit(1)

# ==============================
# MQTT CLIENT SETUP
# ==============================

client = MQTTClient(ADA_USERNAME, ADA_KEY)
client.on_connect = connected
client.on_disconnect = disconnected

client.connect()
client.loop_background()

# ==============================
# SERIAL INITIALIZATION
# ==============================

ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
time.sleep(2)

print("Soil Monitoring System Started...")

# ==============================
# MAIN LOOP
# ==============================

while True:
    try:
        line = ser.readline().decode("utf-8").strip()

        if line:
            print("Received:", line)

            # Expected format:
            # ph,moisture,N,P,K,temp
            values = line.split(",")

            if len(values) == 6:
                ph = float(values[0])
                moisture = float(values[1])
                nitrogen = float(values[2])
                phosphorus = float(values[3])
                potassium = float(values[4])
                temperature = float(values[5])

                # Publish to Adafruit IO
                client.publish(FEED_PH, ph)
                client.publish(FEED_MOISTURE, moisture)
                client.publish(FEED_NITROGEN, nitrogen)
                client.publish(FEED_PHOSPHORUS, phosphorus)
                client.publish(FEED_POTASSIUM, potassium)
                client.publish(FEED_TEMPERATURE, temperature)

                print("Data sent to Adafruit IO successfully.")

        time.sleep(10)

    except Exception as e:
        print("Runtime Error:", e)
        time.sleep(5)
