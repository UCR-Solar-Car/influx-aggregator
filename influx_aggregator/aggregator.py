#!/usr/bin/env python

from datetime import datetime

from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
import random
import time

# You can generate an API token from the "API Tokens Tab" in the UI
token = "bNMiIcMJcrP5x5YQM0D91Rod2hakW_aodrFfr6yPbN4crDJbJw4dmb_cgwclH80vql6_nOhih7MHiwkLDztcfA=="
org = "UCR Solar Car"
bucket = "Telemetry"

with InfluxDBClient(url="http://localhost:8086", token=token,
                    org=org) as client:

    write_api = client.write_api(write_options=SYNCHRONOUS)

    for i in range(1000):
        point = Point("testing").field("temperature",
                                       float(random.randint(1, 100)))
        write_api.write(bucket, org, point)
        time.sleep(1)

    client.close()
