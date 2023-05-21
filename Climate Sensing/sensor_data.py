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

def get_light_category(light_value):
	if light_value <100:
		return 'Very bright'
	elif light_value <500:
		return 'bright'
	elif light_value <1000:
		return 'dark/shady'
	else:
		return 'very dark'

try:
	f = open('/home/pi/sensor_data.csv','a+')
	if os.start('/home/pi/sensor_data.csv').st_size==0:
		f.write('{0} {1} {2:0.1f}*C {3:0.1f}% {4}\r\n'.format(time.strftime('%m/%d/%y'),time.strftime('%H:%M'),temperature_filtered,humidity_filtered,ldr_value,Light_category))

except:
	pass

def rc_time(pin_to_circuit):
	count=0

	GPIO.setup(pin_to_circuit,GPIO.OUT)
	GPIO.output(pin_to_circuit,GPIO.LOW)
	time.sleep(1)

	GPIO.setup(pin_to_circuit,GPIO.IN)

	while(GPIO.input(pin_to_circuit)==GPIO.LOW):
		count+=1
	return count 
while True :
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
		light_category = get_light_category(ldr_value)
		f.write('{0},{1},{2:0.1f}*C,{3:0.1f}%,{4},{5}\r\n'.format(time.strftime('%m/%d/%y'),time.strftime('%H:%M'),temperature_filtered, humidity_filtered,ldr_value,light_category))
		print('Temperature={0:0.1f}*C Humidity={1:0.1f}% Light Intensity={2} ({3})'.format(temperature_filtered,humidity_filtered,ldr_value,light_category))
	else:
		print("Falied to retrieve data from sensors")
