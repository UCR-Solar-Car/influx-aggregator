#pylint: disable=too-few-public-methods

import serial
import time

from environs import Env
#!/usr/bin/env python
#pylint: disable=import-error
import time
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

ENVIRONMENT = "dev"

env = Env()



def env_setup():
    env = Env()
    env.read_env(".env-dev")
    PORT = env("PORT")
    print(PORT)
    TOKEN = env("TOKEN")
    ORG = env("ORG")
    BUCKET = env("BUCKET")
    return PORT, TOKEN, BUCKET, ORG


i = 0
setup = env_setup()
port = setup[0]
token = setup[1]
bucket= setup[2]
org = setup[3]

ser = serial.Serial(port, 9600, timeout = 5)
time.sleep(2)


while ser.inWaiting() > 0:
    line = str(ser.readline())
    line = line.strip("',/\\n")
    line = line.strip("',/\\r")
    line = line.strip("b")
    line = line.strip("'")
    line = line.strip("\'")
    line = line.split(",")
    
    
    print(line)
    with InfluxDBClient(url="http://localhost:8086", token=token,
                        org=org) as client:
        write_api = client.write_api(write_options=SYNCHRONOUS)
        write_api.write(
                bucket, org,
                Point(line[0].strip(" ")).field(
                    line[1].strip(" "), (int)line[2]))