"""
Project: IoT-Based Soil Fertility Monitoring System
Description:
Receives soil sensor data from ESP32 via Serial
and uploads it to ThingSpeak Cloud.
"""

import requests
import time
import serial

# ==============================
# CONFIGURATION
# ==============================

THINGSPEAK_API_KEY = "YOUR_THINGSPEAK_WRITE_KEY"
THINGSPEAK_URL = "https://api.thingspeak.com/update"

SERIAL_PORT = "COM3"      # Change to your port (e.g., COM4 or /dev/ttyUSB0)
BAUD_RATE = 9600

# ==============================
# INITIALIZE SERIAL CONNECTION
# ==============================

ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
time.sleep(2)

# ==============================
# FUNCTION TO UPLOAD DATA
# ==============================

def upload_to_thingspeak(ph, moisture, nitrogen, phosphorus, potassium, temperature):
    payload = {
        "api_key": THINGSPEAK_API_KEY,
        "field1": ph,
        "field2": moisture,
        "field3": nitrogen,
        "field4": phosphorus,
        "field5": potassium,
        "field6": temperature,
    }

    try:
        response = requests.post(THINGSPEAK_URL, data=payload)

        if response.status_code == 200:
            print("Data uploaded successfully.")
        else:
            print("Upload failed:", response.text)

    except Exception as e:
        print("Error while uploading:", e)

# ==============================
# MAIN LOOP
# ==============================

print("Starting Soil Monitoring System...")

while True:
    try:
        line = ser.readline().decode("utf-8").strip()

        if line:
            print("Received:", line)

            # Expected Format:
            # ph,moisture,N,P,K,temp
            values = line.split(",")

            if len(values) == 6:
                ph = float(values[0])
                moisture = float(values[1])
                nitrogen = float(values[2])
                phosphorus = float(values[3])
                potassium = float(values[4])
                temperature = float(values[5])

                upload_to_thingspeak(
                    ph, moisture, nitrogen,
                    phosphorus, potassium, temperature
                )

        time.sleep(15)

    except Exception as e:
        print("Runtime Error:", e)
