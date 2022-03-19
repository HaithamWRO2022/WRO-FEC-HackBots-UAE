import sys
from gpiozero import LED
from time import sleep

gpio = sys.argv[1]

led = LED(int(gpio))

while True:
  led.on()
  sleep(0.3)
  led.off()
  sleep(0.3)
