from adafruit_motor import AdafruitMotor
from rover import Rover  # Make sure to adapt the Rover class to use AdafruitMotor
import time

# Create AdafruitMotor instances for left and right motors
# Note: The motor IDs (1-4) depend on how you've connected the motors to the Motor HAT
motor_left = AdafruitMotor(1)  # Assuming motor 1 is the left motor
motor_right = AdafruitMotor(2)  # Assuming motor 2 is the right motor

# Initialize the rover with AdafruitMotor instances
rover = Rover(motor_left, motor_right)

try:
    while True:
        user_choice = input("Enter a direction (f/b/l/r): ")

        if user_choice.lower() == "f":
            rover.forward()
            time.sleep(1)
        elif user_choice.lower() == "b":
            rover.backward()
            time.sleep(1)
        elif user_choice.lower() == "l":
            # For turning, adjust as needed based on your rover's design.
            # This might involve reversing one motor while moving the other forward.
            motor_left.move_backward()
            motor_right.move_forward()
            time.sleep(1)
        elif user_choice.lower() == "r":
            motor_left.move_forward()
            motor_right.move_backward()
            time.sleep(1)
        else:
            print("Invalid option. Please re-enter.")

except KeyboardInterrupt:
    print("Program stopped by user")
finally:
    # The Adafruit library takes care of cleanup, but you may want to stop all motors here
    motor_left.move_stop()
    motor_right.move_stop()