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
    port_env = env("PORT")
    token_env = env("TOKEN")
    org_env = env("ORG")
    bucket_env = env("BUCKET")
    return port_env, token_env, org_env, bucket_env


port, token, org, bucket = env_setup()

ser = serial.Serial(port, 9600, timeout=5)
time.sleep(2)

with InfluxDBClient(url="http://localhost:8086", token=token,
                    org=org) as client:
    write_api = client.write_api(write_options=SYNCHRONOUS)

    while True:
        while ser.inWaiting() > 0:
            LINE = str(ser.readline())
            LINE = LINE.strip("',/\\n")
            LINE = LINE.strip("',/\\r")
            LINE = LINE.strip("b")
            LINE = LINE.strip("'")
            LINE = LINE.strip("\'")
            LINE = LINE.split(",")

            if len(LINE) == 3:
                write_api.write(bucket, org,
                                Point(LINE[0]).field(LINE[1], int(LINE[2])))
