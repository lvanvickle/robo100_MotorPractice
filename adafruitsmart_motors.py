import serial
import time
from adafruit_motor import AdafruitMotor
from rover import Rover

# Initialize AdafruitMotor instances for left and right motors
# Adjust motor IDs based on how motors are connected to the Adafruit Motor HAT
motor_left = AdafruitMotor(1)  # Assuming motor 1 is the left motor
motor_right = AdafruitMotor(2)  # Assuming motor 2 is the right motor

# Create a Rover instance
rover = Rover(motor_left, motor_right)

# Serial setup for receiving distance measurements
serial_port = "/dev/ttyUSB0"  # Adjust as necessary
baud_rate = 9600
ser = serial.Serial(serial_port, baud_rate, timeout=1)

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
                    print("Obstruction detected. Stopping.")
                else:
                    # Move forward if the path is clear
                    rover.forward()
            except ValueError:
                # Handle cases where the distance reading is not a valid float
                print(f"Error. Received bad data: {line}")

        time.sleep(0.1)

except KeyboardInterrupt:
    print("Program stopped by user.")
finally:
    # Ensure motors are stopped and serial port is closed when program ends
    rover.stop()
    ser.close()