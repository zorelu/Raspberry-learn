import requests
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.iai.v20180301 import iai_client, models
import json
import time
import paho.mqtt.client as mqtt_client
from flask import Flask, session, redirect, url_for, escape, request
from flask_mqtt import Mqtt
import os
app = Flask(__name__)




HOST = "test.mosquitto.org"
PORT = 1883
mqtt_client = mqtt_client.Client()
mqtt_client.connect(HOST, PORT, 60)
a= "http://www.gzywwl.com/1.jpg"
getrul="http://127.0.0.1:5000/renlian?url=" + a
@app.route('/cam')
def cam():
        os.system( "raspistill -q 5 -o -> zorelu.jpg")
        return redirect(getrul)


@app.route('/mqtt')
def mqtt():
        mqtt_client.publish("zorelu","ledoff",2) # 发布一个主题为'chat',内容为‘hello ’的信息
        mqtt_client.loop_start()
        #mqtt_client.loop_stop(force=False)
        return "mqtt ok "
        
@app.route('/renlian', methods=['GET', 'POST'])
def renlian():
    try:
        cred = credential.Credential("AKIDeBWfdSkh2EE3gMzDMNDrKUTHwY3TjngO", "TmvypUxEJCzf9RWP5QegWDkBQUN4d4MU")
        httpProfile = HttpProfile()
        httpProfile.endpoint = "iai.tencentcloudapi.com"

        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        client = iai_client.IaiClient(cred, "ap-guangzhou", clientProfile)
        req = models.VerifyFaceRequest()
        ###获取图片转换格式
        img='{"Url":"http://www.gzywwl.com/4.png","PersonId":"001"}'
        data =json.loads(img)
        data['Url'] =request.args.get('url')
        getdata = json.dumps(data)
        params = str(getdata)
        req.from_json_string(params)

        resp = client.VerifyFace(req)
        data=resp.to_json_string()
        ##输出为dict/json并判断
        bllon=json.loads(data)
        print(bllon)
        print(bllon['IsMatch'])
        if bllon['IsMatch'] == True:
            
            req = requests.get(url='http://127.0.0.1:5000/mqtt') 
            return "renl ok "
        else:
            return "renl nok "    
    except TencentCloudSDKException as err:
        print(err)  
        return "renl notok "   

app.run(host='0.0.0.0')
