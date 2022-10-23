#!/usr/bin/env python
import random
import time
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
from environs import Env

from influx_aggregator.payload import Payload

ENVIRONMENT = "dev"

env = Env()
if ENVIRONMENT == "dev":
    env.read_env(".env.dev", recurse=False)
elif ENVIRONMENT == "production":
    env.read_env(".env.production", recurse=False)

TOKEN = env("TOKEN")
ORG = env("ORG")
BUCKET = env("BUCKET")

payload = Payload()


def testbench():
    with InfluxDBClient(url="http://localhost:8086", token=TOKEN,
                        org=ORG) as client:
        write_api = client.write_api(write_options=SYNCHRONOUS)
        for _ in range(1500):
            payload.battery.set_voltage(random.randint(0, 500))
            payload.battery.set_temperature(random.randint(0, 100))
            payload.battery.set_range(random.randint(0, 150))
            payload.battery.set_warning(random.randint(0, 1))
            payload.battery.set_bps_fault(random.randint(0, 1))
            payload.battery.set_automatic_power_opening(random.randint(0, 1))
            payload.tire_pressure.set_back_left(random.randint(0, 50))
            payload.tire_pressure.set_back_right(random.randint(0, 50))
            payload.tire_pressure.set_front_left(random.randint(0, 50))
            payload.tire_pressure.set_front_right(random.randint(0, 50))
            payload.motor.set_distance(random.randint(0, 150))
            payload.motor.set_motor_temperature(random.randint(0, 100))
            payload.motor.set_motor_voltage(random.randint(0, 200))
            payload.motor.set_speed(random.randint(0, 200))
            payload.motor.set_motor_warning(random.randint(0, 1))
            payload.icons.set_cruise_control(random.randint(0, 1))
            payload.icons.set_day_lights(random.randint(0, 1))
            payload.icons.set_gears(random.randint(0, 1))
            payload.icons.set_horn(random.randint(0, 1))
            payload.icons.set_left_indicator(random.randint(0, 1))
            payload.icons.set_right_indicator(random.randint(0, 1))
            payload.icons.set_night_lights(random.randint(0, 1))
            write_api.write(
                BUCKET, ORG,
                Point("BATTERY").field("battery_voltage",
                                       payload.battery.get_voltage()))
            write_api.write(
                BUCKET, ORG,
                Point("BATTERY").field("battery_temp",
                                       payload.battery.get_temperature()))
            write_api.write(
                BUCKET, ORG,
                Point("BATTERY").field("battery_range",
                                       payload.battery.get_range()))
            write_api.write(
                BUCKET, ORG,
                Point("BATTERY").field("battery_warning",
                                       payload.battery.get_warning()))
            write_api.write(
                BUCKET, ORG,
                Point("BATTERY").field("battery_bps_fault",
                                       payload.battery.get_bps_fault()))
            write_api.write(
                BUCKET, ORG,
                Point("BATTERY").field(
                    "battery_auto_power_opening",
                    payload.battery.get_automatic_power_opening()))
            write_api.write(
                BUCKET, ORG,
                Point("TIRE_PRESSURE").field(
                    "BL_tire_pressure", payload.tire_pressure.get_back_left()))
            write_api.write(
                BUCKET, ORG,
                Point("TIRE_PRESSURE").field(
                    "BR_tire_pressure",
                    payload.tire_pressure.get_back_right()))
            write_api.write(
                BUCKET, ORG,
                Point("TIRE_PRESSURE").field(
                    "FL_tire_pressure",
                    payload.tire_pressure.get_front_left()))
            write_api.write(
                BUCKET, ORG,
                Point("TIRE_PRESSURE").field(
                    "FR_tire_pressure",
                    payload.tire_pressure.get_front_right()))
            write_api.write(
                BUCKET, ORG,
                Point("MOTOR").field("motor_distance",
                                     payload.motor.get_distance()))
            write_api.write(
                BUCKET, ORG,
                Point("MOTOR").field("motor_temp",
                                     payload.motor.get_motor_temperature()))
            write_api.write(
                BUCKET, ORG,
                Point("MOTOR").field("motor_voltage",
                                     payload.motor.get_motor_voltage()))
            write_api.write(
                BUCKET, ORG,
                Point("MOTOR").field("motor_speed", payload.motor.get_speed()))
            write_api.write(
                BUCKET, ORG,
                Point("MOTOR").field("motor_warning",
                                     payload.motor.get_motor_warning()))
            write_api.write(
                BUCKET, ORG,
                Point("ICONS").field("icon_cruise_control",
                                     payload.icons.get_cruise_control()))
            write_api.write(
                BUCKET, ORG,
                Point("ICONS").field("icon_day_lights",
                                     payload.icons.get_day_lights()))
            write_api.write(
                BUCKET, ORG,
                Point("ICONS").field("icon_gears", payload.icons.get_gears()))
            write_api.write(
                BUCKET, ORG,
                Point("ICONS").field("icon_horn", payload.icons.get_horn()))
            write_api.write(
                BUCKET, ORG,
                Point("ICONS").field("icon_L_indicator",
                                     payload.icons.get_left_indicator()))
            write_api.write(
                BUCKET, ORG,
                Point("ICONS").field("icon_R_indicator",
                                     payload.icons.get_right_indicator()))
            write_api.write(
                BUCKET, ORG,
                Point("ICONS").field("icon_night_lights",
                                     payload.icons.get_night_lights()))
            time.sleep(1)
        client.close()


testbench()
