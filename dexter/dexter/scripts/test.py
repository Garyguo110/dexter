import time

from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

mh = Adafruit_MotorHAT(addr=0x60)
leftMotor = mh.getMotor(4)
rightMotor = mh.getMotor(3)
leftMotor.setSpeed(70)
rightMotor.setSpeed(70)


def s():
    leftMotor.run(Adafruit_MotorHAT.RELEASE)
    rightMotor.run(Adafruit_MotorHAT.RELEASE)


def move(l_direction, r_direction, duration):
    leftMotor.run(l_direction)
    rightMotor.run(r_direction)
    time.sleep(duration)
    s()


def f(duration=5):
    move(Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.FORWARD, duration)


def b(duration=5):
    move(Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.BACKWARD, duration)


def l(duration=5):
    move(Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.FORWARD, duration)


def r(duration=5):
    move(Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.BACKWARD, duration)
