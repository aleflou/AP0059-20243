from machine import Pin, ADC
from time import sleep

# Configuración del pin del LED y del potenciómetro
led1 = Pin(33, Pin.OUT)      # Definir el pin 33 como salida para el LED
led2 = Pin(32, Pin.OUT)
led3 = Pin(25, Pin.OUT)
pot = ADC(Pin(34))           # Definir el pin 34 para el ADC
pot.atten(ADC.ATTN_11DB)     # Configurar la atenuación del ADC para el rango completo de 3.3V

while True:
    pot_value = pot.read()    
    print(pot_value)
    sleep(0.15)                 # Esperar 1/2 segundo antes de la siguiente lectura

    if pot_value >500:
        led1.value(1)       # Encender el LED (1 = encendido)
    else:
        led1.value(0)
    if pot_value >1500:
        led2.value(1)       # Encender el LED (1 = encendido)
    else:
        led2.value(0)
    if pot_value >2500:
        led3.value(1)       # Encender el LED (1 = encendido)
    else:
        led3.value(0)
