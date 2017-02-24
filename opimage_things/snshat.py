from sense_hat import SenseHat

def get_readings():
    sense = SenseHat()
    humidity = sense.get_humidity()
    temp_h = sense.get_temperature_from_humidity()
    temp_p = sense.get_temperature_from_pressure()
    pressure = sense.get_pressure()
    return [humidity, temp_h, pressure, temp_p]



