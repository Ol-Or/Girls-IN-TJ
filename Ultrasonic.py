import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

TRIG = 18
ECHO = 21

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

# 초음파 출력 초기화
GPIO.output(TRIG, False)
time.sleep(2)

relay = 4
GPIO.setup(relay, GPIO.OUT)
GPIO.output(relay, GPIO.LOW)

try:
    # 펄스 발생 딜레이
    while True:
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

        # ECHO 상승 시간값 저장
        while GPIO.input(ECHO) == 0:
            pulse_start = time.time()

        # ECHO 하강 시간값 저장
        while GPIO.input(ECHO) == 1:
            pulse_stop = time.time()

        pulse_time = pulse_stop - pulse_start

        # 물까지의 거리계산
        distance = pulse_time * 17150

        time.sleep(1)

        # 워터펌프 작동
        if distance > 10:  # 10은 임의의 값으로 잡았음
            GPIO.output(relay, GPIO.HIGH)
        else:
            GPIO.output(relay, GPIO.LOW)


except KeyboardInterrupt:
    GPIO.cleanup()
