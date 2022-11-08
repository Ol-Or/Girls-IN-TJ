#사진 5초마다 촬영 후 저장
from picamera import PiCamera
from time import sleep

camera = PiCamera()

for i in range(5):
   sleep(5)
   camera.capture('/home/pi/image.jpg'.format(i))

#저장한 jpg 파일 읽고 평균값 추출
import cv2
import sys
import numpy as np
import matplotlib.pyplot as plt
src = cv2.imread('/home/pi/image.jpg'.format(i))

if src is None:
    print('Image load failed!')
    sys.exit()

colors = ['b', 'g', 'r']
bgr_planes = cv2.split(src)

for (p, c) in zip(bgr_planes, colors):
    hist = cv2.calcHist([p], [0], None, [256], [0, 256])   

Red = []
Green = []
Blue = []

for x in src:
    for y in x:
        Red.append(y[0])
        Green.append(y[1])
        Blue.append(y[2])

R_max = max(Red)
G_max = max(Green)
B_max = max(Blue)

R_avg = sum(Red) / len(Red)
G_avg = sum(Green) / len(Green)
B_avg = sum(Blue) / len(Blue)
   
print("Max Value")
print("R : ", R_max)
print("G : ", G_max)
print("B : ", B_max)

print("Avg Value")
print("R : ", R_avg)
print("G : ", G_avg)
print("B : ", B_avg)


cv2.imshow('src', src)
cv2.waitKey(1)








