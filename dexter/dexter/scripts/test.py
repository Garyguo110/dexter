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


def forward():
    leftMotor.run(Adafruit_MotorHAT.FORWARD)
    rightMotor.run(Adafruit_MotorHAT.FORWARD)
    time.sleep(1)
    turnOffMotors()
