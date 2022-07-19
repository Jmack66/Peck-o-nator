import RPi.GPIO as GPIO
import time

servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

START_POS = 90
END_POS = 20

servo = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
servo.start(2.5) # Initialization

def ServoWrite(angle):
    duty = angle / duty + 2
    servo.ChangeDutyCycle(duty)
    return 0

def LERP(start_pos, end_pos,steps):
    return (1 - steps) * start_pos + steps * end_pos

def DefaultPeck():
    ServoWrite(START_POS)
    for i in range(0,END_POS):
        ServoWrite(LERP(START_POS,END_POS,7))
        time.sleep(0.01)