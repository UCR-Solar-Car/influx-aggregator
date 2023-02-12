#pylint: disable=too-few-public-methods
import time
import serial


from environs import Env
#!/usr/bin/env python
#pylint: disable=import-error

from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

ENVIRONMENT = "dev"




def env_setup():
    env = Env()
    env.read_env(".env-dev")
    port_es = env("PORT")
    #print(PORT)
    token_es= env("TOKEN")
    org_es = env("ORG")
    bucket_es = env("BUCKET")
    return port_es, token_es, org_es, bucket_es


i = 0
setup = env_setup()
port = setup[0]
token = setup[1]
bucket = setup[2]
org = setup[3]

ser = serial.Serial(port, 9600, timeout=5)
time.sleep(2)

while ser.inWaiting() > 0:
    LINE = str(ser.readline())
    LINE = LINE.strip("',/\\n")
    LINE = LINE.strip("',/\\r")
    LINE = LINE.strip("b")
    LINE = LINE.strip("'")
    LINE = LINE.strip("\'")
    LINE = LINE.split(",")

    print(LINE)
    with InfluxDBClient(url="http://localhost:8086", token=token,
                        org=org) as client:
        write_api = client.write_api(write_options=SYNCHRONOUS)
        write_api.write(
            bucket, org,
            Point(LINE[0].strip(" ")).field(LINE[1].strip(" "), int(LINE[2])))
