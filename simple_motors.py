import RPi.GPIO as GPIO
import time
from motor import Motor
from rover import Rover

# Initialize GPIO
GPIO.setmode(GPIO.BCM) # Use BCM GPIO numbering
GPIO.setwarnings(False)

# Create motor instances with GPIO pins
motor_left = Motor(4, 14)
motor_right = Motor(17, 27)

rover = Rover(motor_left, motor_right)

try:
	while True:
		user_choice = input("Enter a direction (f/b/l/r): ")
		
		if(user_choice.lower() == "f"):
			rover.forward()
			time.sleep(1)
		elif(user_choice.lower() == "b"):
			rover.backward()
			time.sleep(1)
		elif(user_choice.lower() == "l"):
			motor_left.stop()
			motor_right.move_forward()
			time.sleep(1)
		elif(user_choice.lower() == "r"):
			motor_left.move_forward()
			motor_right.stop()
			time.sleep(1)
		else:
			print("Invalid option. Please re-enter.")
except KeyboardInterrupt:
	print("Program stopped by user")
finally:
	GPIO.cleanup()
	