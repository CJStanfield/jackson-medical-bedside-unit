import json
import random
from threading import Thread

import pandas as pd
from flask import Flask
import os
import time

from sseclient import SSEClient

local_url = "http://10.0.0.1/api/sse"
interface = "wlan1"
name = "DataPort-BT2-2764-103-000107"
password = "boditr@k"
app = Flask(__name__)


@app.route("/")
def hello():
    print("Identifying network...")
    for i in range(0, 3):
        rand = random.randint(0, 1)
        time.sleep(rand)
        print("...")
    print("network identified")
    print("connecting to ", name)
    # os.system('iwconfig ' + interface + ' essid ' + name + ' key ' + password)
    time.sleep(5)
    print("connection successful")
    print("starting data streaming")
    thread = Thread(target=start_sse_client)
    thread.start()
    return json.dumps({"status": "data streaming to raspberry pi"})


def start_sse_client():
    while True:
        print("test sse connection")
        time.sleep(1)
    # sse = SSEClient(local_url)
    # for response in sse:
    #     df = pd.read_json(response.data)
    #     self.save_sensor_data(df)
    #     if "readings" in df.columns:
    #         readings_array = str(df["readings"][0])
    #         print(readings_array)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)
