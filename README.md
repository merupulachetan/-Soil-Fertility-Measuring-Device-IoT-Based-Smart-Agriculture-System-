# 🌱 IoT-Based Soil Fertility Monitoring System

A real-time IoT-based soil monitoring system that measures soil pH, Moisture, Temperature, and NPK (Nitrogen, Phosphorus, Potassium) levels using ESP32 and Python cloud integration.

---

## 📌 Project Objective

The objective of this project is to develop a portable, cost-effective, and real-time soil fertility monitoring device that:

- Measures soil pH
- Measures soil moisture
- Measures soil temperature
- Measures Nitrogen (N), Phosphorus (P), Potassium (K)
- Uploads data to ThingSpeak Cloud
- Enables remote monitoring via dashboard

---

## 🏗 System Architecture

Soil Sensors → ESP32 → WiFi → ThingSpeak Cloud → Web Dashboard

---

## 🔧 Hardware Components

- ESP32 Microcontroller
- Soil pH Sensor
- Capacitive Soil Moisture Sensor
- NPK Sensor
- DS18B20 Temperature Sensor
- OLED Display (Optional)
- Li-ion Battery

---

## 💻 Software Components

- Python 3.x
- Arduino IDE
- ThingSpeak Cloud
- Required Python Libraries:
  - requests
  - pyserial
  - pandas
  - matplotlib

---


📌 **What You Must Do on Adafruit IO Website**

- Login to https://io.adafruit.com
- Go to Feeds
- Create these feeds exactly:
  - soil-ph
  - soil-moisture
  - soil-nitrogen
  - soil-phosphorus
  - soil-potassium
  - soil-temperature
- Go to Dashboards
- Add gauges or charts for each feed
