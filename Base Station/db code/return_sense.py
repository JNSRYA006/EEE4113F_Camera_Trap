import  RPi.GPIO as GPIO
import time
import Adafruit_DHT
import os 

GPIO.setmode(GPIO.BOARD)

pin_to_circuit = 11

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN=4
Moving_AVG_SIZE = 5
temperature_avg = [None]*Moving_AVG_SIZE
humidity_avg = [None]*Moving_AVG_SIZE

def rc_time(pin_to_circuit):
	count=0

	GPIO.setup(pin_to_circuit,GPIO.OUT)
	GPIO.output(pin_to_circuit,GPIO.LOW)
	time.sleep(1)

	GPIO.setup(pin_to_circuit,GPIO.IN)

	while(GPIO.input(pin_to_circuit)==GPIO.LOW):
		count+=1
	return count 

def getSensorVal(pin_to_circuit, DHT_SENSOR, DHT_PIN):
	ldr_value = rc_time(pin_to_circuit)

	humidity,temperature = Adafruit_DHT.read_retry(DHT_SENSOR,DHT_PIN)
	ldr_filter = []
	for i in range(5):
		ldr_filter.append(rc_time(pin_to_circuit))
		time.sleep(1)
	ldr_value = sum(ldr_filter)/len(ldr_filter)
	if humidity is not None and temperature is not None:
		temperature_avg.pop(0)
		temperature_avg.append(temperature)
		humidity_avg.pop(0)
		humidity_avg.append(humidity)
		temperature_sum = sum(filter(lambda x: x is not None,temperature_avg))
		humidity_sum = sum(filter(lambda x: x is not None, humidity_avg))

		temperature_filtered = temperature_sum/len(list(filter(lambda x:x is not None,temperature_avg)))
		humidity_filtered = humidity_sum/len(list(filter(lambda x: x is not None,humidity_avg)))
		return round(temperature_filtered,3), round(humidity_filtered,3), round(ldr_value,3)
	else:
		print("Falied to retrieve data from sensors")