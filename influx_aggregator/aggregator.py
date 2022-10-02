#!/usr/bin/env python
import random
import time
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

# You can generate an API token from the "API Tokens Tab" in the UI
TOKEN = "bNMiIcMJcrP5x5YQM0D91Rod2hakW_aodrFfr6yPbN4crDJbJw4dmb_cgwclH80vql6_nOhih7MHiwkLDztcfA=="
ORG = "UCR Solar Car"
BUCKET = "Telemetry"

with InfluxDBClient(url="http://localhost:8086", token=TOKEN,
                    org=ORG) as client:

    write_api = client.write_api(write_options=SYNCHRONOUS)

    for i in range(1000):
        point = Point("testing").field("temperature",
                                       float(random.randint(1, 100)))
        write_api.write(BUCKET, ORG, point)
        time.sleep(1)

    client.close()
