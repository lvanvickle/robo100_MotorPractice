from adafruit_motorkit import MotorKit

class AdafruitMotor:
    def __init__(self, motor_id):
        self.kit = MotorKit()
        if motor_id == 1:
            self.motor = self.kit.motor1
        elif motor_id == 2:
            self.motor = self.kit.motor2
        elif motor_id == 3:
            self.motor = self.kit.motor3
        elif motor_id == 4:
            self.motor = self.kit.motor4
        else:
            raise ValueError("Invalid motor ID. Choose a value between 1 and 4.")

    def move_forward(self, speed=1.0):
        self.motor.throttle = speed

    def move_backward(self, speed=1.0):
        self.motor.throttle = -speed

    def move_stop(self):
        self.motor.throttle = 0