import RPi.GPIO as GPIO
import time


servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

START_POS = 30
END_POS = 100

servo = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
servo.start(START_POS / 18 + 2)
def ServoWrite(angle):
    duty = angle / 18 + 2
    print(angle, duty)
    servo.ChangeDutyCycle(duty)
    return 0
def LERP(start_pos, end_pos,steps):
    return (1 - steps) * start_pos + steps * end_pos

def interp(start_pos, end_pos, steps):
    return (start_pos - end_pos) / steps

def DefaultPeck():
    ServoWrite(START_POS)
    current_pos = START_POS
    for i in range(1,7):
        current_pos -= interp(START_POS,END_POS,7)
        ServoWrite(current_pos)
        time.sleep(0.02)
    ServoWrite(START_POS)

#def Peck(peck_count,time):
    #ServoWrite(START_POS)
    #current_pos = START_POS
    #for i in range(1,peck_count):
        #for i in range(1,time):
            #current_pos -= interp(START_POS,END_POS,time)
            #ServoWrite(current_pos)
            #time.sleep(0.02)
        #ServoWrite(START_POS)
        #time.sleep(1)

def Peck(peck_count, arc):
    for i in range(1,peck_count):
        ServoWrite(END_POS + arc)
        time.sleep(0.5)
        ServoWrite(END_POS)
        time.sleep(1)
    ServoWrite(START_POS)
    return 0 