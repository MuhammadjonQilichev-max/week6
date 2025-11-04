
def summarize_sensor_data(readings):
    if not readings:
        return []
    
    sensor_max = {}

    for sensor_id, temperature in readings:
        if sensor_id not in sensor_max or temperature > sensor_max[sensor_id]:
            sensor_max[sensor_id] = temperature

    final = sorted(sensor_max.items())
    return final
readings = [
	('SensorB', 25.4),
	('SensorA', 22.1),
	('SensorB', 26.1),
	('SensorC', 30.5),
	('SensorA', 21.9), 
	('SensorB', 25.9)
]

print(summarize_sensor_data(readings))

# Case 2:
readings2 = []
print(summarize_sensor_data(readings2))