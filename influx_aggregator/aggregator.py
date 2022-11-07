#!/usr/bin/env python
import random
import time
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
from environs import Env


def env_setup():
    enviorment = "dev"

    env = Env()
    if enviorment == "dev":
        env.read_env(".env.dev", recurse=False)
    elif enviorment == "production":
        env.read_env(".env.production", recurse=False)

    token = env("TOKEN")
    org = env("ORG")
    bucket = env("BUCKET")

    return token, org, bucket


def aggregator():
    setup = env_setup()

    token = setup[0]
    org = setup[1]
    bucket = setup[2]

    with InfluxDBClient(url="http://localhost:8086", token=token,
                        org=org) as client:
        write_api = client.write_api(write_options=SYNCHRONOUS)

        for _ in range(1000):
            point = Point("testing").field("temperature",
                                           float(random.randint(1, 100)))
            write_api.write(bucket, org, point)
            time.sleep(1)

        client.close()