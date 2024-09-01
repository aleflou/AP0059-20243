from machine import Pin
import time

# Definir los pines GPIO para controlar el motor
in1 = Pin(18, Pin.OUT)
in2 = Pin(19, Pin.OUT)
stop = Pin (22, Pin.OUT)

def motor_forward():
    in1.value(1)
    in2.value(0)
    stop.value(0)
    print("Motor girando hacia adelante")

def motor_backward():
    in1.value(0)
    in2.value(1)
    stop.value(0)
    print("Motor girando hacia atrás")

def motor_stop():
    in1.value(0)
    in2.value(0)
    stop.value(1)
    print("Motor detenido")

while True:
    # Motor hacia adelante
    motor_forward()
    time.sleep(2)

    # Detener motor
    motor_stop()
    time.sleep(1) 

    # Motor hacia atrás
    motor_backward()
    time.sleep(2)  

    # Detener motor
    motor_stop()
    time.sleep(1)  
