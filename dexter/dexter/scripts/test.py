import time

from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

mh = Adafruit_MotorHAT(addr=0x60)
leftMotor = mh.getMotor(4)
rightMotor = mh.getMotor(3)
leftMotor.setSpeed(10)
rightMotor.setSpeed(10)


def turnOffMotors():
    leftMotor.run(Adafruit_MotorHAT.RELEASE)
    rightMotor.run(Adafruit_MotorHAT.RELEASE)


def move(l_direction, r_direction):
    leftMotor.run(l_direction)
    rightMotor.run(r_direction)
    time.sleep(5)
    turnOffMotors()


def forward():
    move(Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.FORWARD)


def backwards():
    move(Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.BACKWARD)


def left():
    move(Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.FORWARD)


def right():
    move(Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.BACKWARD)
