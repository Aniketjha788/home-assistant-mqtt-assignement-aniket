import time
import json
import paho.mqtt.client as mqtt

# =========================================
# REQUIRED BY ASSIGNMENT (DON'T REMOVE)
# =========================================
student_name = "Aniket Jha"       
unique_id = "42614011"            
topic = "home/aniketjha-42614011-2025/sensor"
# =========================================

BROKER = "localhost"   # Mosquitto broker same PC pe chal raha hai
PORT = 1883            # Default MQTT port

# Extra sensor of your choice – maine gas liya hai
EXTRA_SENSOR_NAME = "gas" 

# MQTT client create karo
client = mqtt.Client()

# Broker se connect karo
client.connect(BROKER, PORT, 60)

print("=========================================")
print(f"Connected to MQTT Broker: {BROKER}:{PORT}")
print(f"Student Name : {student_name}")
print(f"Unique ID    : {unique_id}")
print(f"MQTT Topic   : {topic}")
print("Publishing data every 5 seconds...")
print("Press Ctrl + C to stop.")
print("=========================================")

try:
    while True:
        # Assignment ke hisaab se fixed values
        temperature = 25      # degree celsius
        humidity = 60         # percent
        extra_value = 300     # gas sensor dummy value (ppm)

        # JSON payload create kar rahe hain
        payload = {
            "student_name": student_name,
            "unique_id": unique_id,
            "temperature": temperature,
            "humidity": humidity,
            EXTRA_SENSOR_NAME: extra_value
        }

        # Convert dictionary to JSON string
        payload_str = json.dumps(payload)

        # Publish message to MQTT
        result = client.publish(topic, payload_str)
        status = result[0]

        if status == 0:
            print(f"Published to {topic}: {payload_str}")
        else:
            print(f"Failed to publish message to topic {topic}")

        time.sleep(5)   # 5 sec delay

except KeyboardInterrupt:
    print("\nStopping publisher...")

finally:
    client.disconnect()
    print("Disconnected from MQTT broker.")
