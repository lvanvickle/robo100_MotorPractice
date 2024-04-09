import serial
import time
import RPi.GPIO as GPIO
from motor import Motor
from rover import Rover

# Initialize GPIO
GPIO.setmode(GPIO.BCM) # Use BCM GPIO numbering
GPIO.setwarnings(False)

# Motor set up
motor_left = Motor(17, 27)
motor_right = Motor(20, 21)

# Create rover instance
rover = Rover(motor_left, motor_right)

# Serial set up
serial_port = "/dev/ttyUSB0"
baud_rate = 9600
ser = ser.Serial(serial_port, baud_rate, timeout=1)

try:
	while True:
		if ser.in_waiting > 0:
			line = ser.readline().decode("utf-8").rstrip()
			try:
				distance = float(line)
				print(f"Distance: {distance} cm")
				
				if distance < 10:
					# Stop rover if obstruction is within 10 cm
					rover.stop()
					print("Obstruction detected. Stopping motors.")
				else:
					# Otherwise, move forward
					rover.forward()
					
			except ValueError:
				# In case Arduino sends bad data
				print("Error. Received bad data:", line)
				
		time.sleep(0.1)
		
except KeyboardInterrupt:
	print("Program stopped by user")
	
finally:
	GPIO.cleanup()
	ser.close()
					
				
