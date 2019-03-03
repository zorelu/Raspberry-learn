import paho.mqtt.client as mqtt
import time
HOST = "test.mosquitto.org"
PORT = 1883


client = mqtt.Client()
client.connect(HOST, PORT, 60)

client.publish("zorelu","hello",2) # 发布一个主题为'chat',内容为‘hello ’的信息
client.loop_start()

client.loop_stop(force=False)
