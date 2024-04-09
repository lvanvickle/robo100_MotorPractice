import RPi.GPIO as GPIO

class Motor:
	def __init__(self, in1_pin, in2_pin):
		self.in1_pin = in1_pin
		self.in2_pin = in2_pin
		
		GPIO.setup(self.in1_pin, GPIO.OUT)
		GPIO.setup(self.in2_pin, GPIO.OUT)
		
	def move_forward(self):
		GPIO.output(self.in1_pin, GPIO.HIGH)
		GPIO.output(self.in2_pin, GPIO.LOW)
		
	def move_backward(self):
		GPIO.output(self.in1_pin, GPIO.LOW)
		GPIO.output(self.in2_pin, GPIO.HIGH)
		
	def move_stop(self):
		GPIO.output(self.in1_pin, GPIO.LOW)
		GPIO.output(self.in2_pin, GPIO.LOW)
