from machine import Pin, PWM
import utime 


led_ext1= Pin(15,Pin.OUT)
led_ext2= Pin(14,Pin.OUT)
led_ext3= Pin(13,Pin.OUT)

while True:
  led_ext1.value(1)
  print("EXT LED ON")
  utime.sleep(3)
  
  buzzer = PWM(Pin(15))
  buzzer.freq(500)
  buzzer.duty_u16(1000)
  utime.sleep(3)
  buzzer.duty_u16(0)

  led_ext1.value(0)
  print("EXT LED OFF")
  buzzer = PWM(Pin(15))
  buzzer.freq(500)
  buzzer.duty_u16(1000)
  utime.sleep(3)
  buzzer.duty_u16(0)

  utime.sleep(1)
  led_ext2.value(1)
  print("EXT LED ON")
  utime.sleep(2)
  led_ext2.value(0)
  print("EXT LED OFF")
  utime.sleep(1)
  led_ext3.value(1)
  print("EXT LED ON")
  utime.sleep(3)
  led_ext3.value(0)
  print("EXT LED OFF")
  utime.sleep(1)
