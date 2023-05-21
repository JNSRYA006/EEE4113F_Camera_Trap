import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
pin_to_circuit = 11

def rc_time(pin_to_circuit):
	count = 0
	GPIO.setup(pin_to_circuit, GPIO.OUT)
	GPIO.output(pin_to_circuit, GPIO.LOW)
	time.sleep(1)

	GPIO.setup(pin_to_circuit,GPIO.IN)

	while (GPIO.input(pin_to_circuit) == GPIO.LOW):
		count+=1
	return count

try:
	while True:
		reading = rc_time(pin_to_circuit)

		print("Light intensity:",rc_time(pin_to_circuit))
		
 
except KeyboardInterrupt:
	pass
finally:
	GPIO.cleanup

