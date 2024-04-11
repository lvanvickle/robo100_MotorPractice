from adafruit_motor import AdafruitMotor

class Rover:
    def __init__(self, motor_left, motor_right):
        # Assuming motor_left and motor_right are instances of AdafruitMotor
        self.motor_left = motor_left
        self.motor_right = motor_right
        
    def forward(self, speed=1.0):
        # Move both motors forward
        self.motor_left.move_forward(speed)
        self.motor_right.move_forward(speed)
        
    def backward(self, speed=1.0):
        # Move both motors backward
        self.motor_left.move_backward(speed)
        self.motor_right.move_backward(speed)
        
    def stop(self):
        # Stop both motors
        self.motor_left.move_stop()
        self.motor_right.move_stop()
        
    def turn_left(self, speed=1.0):
        # For a simple turn, stop one motor and move the other
        # Adjust as necessary for your specific rover design
        self.motor_left.move_backward(speed)
        self.motor_right.move_forward(speed)
        
    def turn_right(self, speed=1.0):
        # For a simple turn, move one motor forward and the other backward
        # Adjust as necessary for your specific rover design
        self.motor_left.move_forward(speed)
        self.motor_right.move_backward(speed)