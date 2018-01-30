

# coding: UTF-8
import time
import os
import RPi.GPIO as GPIO
from GetThread import GetThread


if __name__ == "__main__":
	t = GetThread()
	t.start()
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
	DEBUG = 0

	# 使用するGPIO
	GPIO17 = 17

	# GPIOの設定

	GPIO.setup(GPIO17, GPIO.OUT)
	GPIO.output(GPIO17, 1)

	p17 = GPIO.PWM(GPIO17, 60)
	p17.start(0)

	try:
		while 1:
			if t.power > 1.0 and t.hz > 0.2 and t.hz < 5.0:
				span = 1.0/t.hz
				sleep_time = span/10.0
				# 徐々に明るく
				for dc in range(0, 100, 20):
					p17.ChangeDutyCycle(dc)
					time.sleep(sleep_time)

				# 徐々に暗く
				for dc in range(100, 0, -20):
					p17.ChangeDutyCycle(dc)
					time.sleep(sleep_time)
	except KeyboardInterrupt:
		pass
	t.stop()
	p17.stop()
	GPIO.cleanup()
