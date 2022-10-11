#!/usr/bin/env python
import random
import time
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
from environs import Env

ENVIRONMENT = "dev"

env = Env()
if ENVIRONMENT == "dev":
    env.read_env(".env.dev", recurse=False)
elif ENVIRONMENT == "production":
    env.read_env(".env.production", recurse=False)

TOKEN = env("TOKEN")
ORG = env("ORG")
BUCKET = env("BUCKET")

with InfluxDBClient(url="http://localhost:8086", token=TOKEN,
                    org=ORG) as client:

    write_api = client.write_api(write_options=SYNCHRONOUS)

    for i in range(1000):
        point = Point("testing").field("temperature",
                                       float(random.randint(1, 100)))
        write_api.write(BUCKET, ORG, point)
        time.sleep(1)

    client.close()
