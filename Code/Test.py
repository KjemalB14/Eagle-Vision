from gpiozero import LED
from time import sleep

#set led input to pin 17
led = LED(17)

#setting the led up to turn off and on every second
while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)