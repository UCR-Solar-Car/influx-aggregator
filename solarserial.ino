void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
}

void loop() {
  Serial.print("MOTOR,motor_temp,");
  Serial.println(random(100));
  Serial.print("BATTERY,battery_voltage,");
  Serial.println(random(100));
  Serial.print("BATTERY,battery_temp,");
  Serial.println(random(100));
  Serial.print("BATTERY,battery_range,");
  Serial.println(random(100));
  Serial.print("MOTOR,motor_voltage,");
  Serial.println(random(100));
  Serial.print("MOTOR,motor_distance,");
  Serial.println(random(100));
  Serial.print("TIRE_PRESSURE,BR_tire_pressure,");
  Serial.println(random(100));
  Serial.print("TIRE_PRESSURE,FR_tire_pressure,");
  Serial.println(random(100));
  Serial.print("TIRE_PRESSURE,BL_tire_pressure,");
  Serial.println(random(100));
  Serial.print("TIRE_PRESSURE,FL_tire_pressure,");
  Serial.println(random(100));
  Serial.print("ICONS,icon_L_indicator,");
  Serial.println(random(2));
  Serial.print("ICONS,icon_R_indicator,");
  Serial.println(random(2));
  Serial.print("MOTOR,motor_speed,");
  Serial.println(random(100));
  Serial.print("ICONS,icon_cruise_control,");
  Serial.println(random(2));
  Serial.print("ICONS,icon_day_lights,");
  Serial.println(random(2));
  Serial.print("ICONS,icon_night_lights,");
  Serial.println(random(2));
  Serial.print("MOTOR,motor_warning,");
  Serial.println(random(2));
  Serial.print("BATTERY,battery_warning,");
  Serial.println(random(2));
  Serial.print("BATTERY,battery_bps_fault,");
  Serial.println(random(2));
  Serial.print("ICONS,icon_horn,");
  Serial.println(random(2));
  delay(1000);
}
