import sys
import random
import time
from Adafruit_IO import MQTTClient

AIO_FEED_IDs = ["nutnhan1","nutnhan2"]
AIO_USERNAME = "longthangtran"
AIO_KEY = "aio_Kszy30GOmsAh8CdBAL7HC55MdgO2"

def connected(client):
    print("Ket noi thanh cong ...")
    for topic in AIO_FEED_IDs:
        client.subscribe(topic)

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe thanh cong ...")

def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit (1)

def message(client , feed_id , payload):
    print("Nhan du lieu: " + payload + " , feed id:" + feed_id)

client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()
counter = 10
sensor_type = 0
while True:
    counter = counter - 1
    if counter <= 0:
        counter = 10
        #TODO
        print("Random data is publishing...")
        if sensor_type == 0:
            print("Temp...")
            temp = random.randint(10,20)
            client.publish("cambien1", temp)
            sensor_type = 1
        elif sensor_type == 1:
            print("Humidity...")
            humi = random.randint(50,70)
            client.publish("cambien2", humi)
            sensor_type = 2
        elif sensor_type == 2:
            print("Light...")
            light = random.randint(100,500)
            client.publish("cambien3", light)
            sensor_type = 0
    time.sleep(1)
    pass