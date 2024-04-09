class Rover:
	def __init__(self, motor_left, motor_right):
		self.motor_left = motor_left
		self.motor_right = motor_right
		
	def forward(self):
		self.motor_left.move_forward()
		self.motor_right.move_forward()
		
	def backward(self):
		self.motor_left.move_backward()
		self.motor_right.move_backward()
		
	def stop(self):
		self.motor_left.stop()
		self.motor_right.stop()