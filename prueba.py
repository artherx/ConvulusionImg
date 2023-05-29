import cv2
import numpy as np
cap = cv2.VideoCapture(701)
if not cap.isOpened():
    print("No se pudo abrir la cámara")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        print("No se pudo recibir el cuadro de la cámara")
        break
    hsvframe= cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lower_color = np.array([24,52,24])
    upper_color = np.array([80,255,255])
    lower_barro = np.array([15, 100, 100])
    upper_barro = np.array([40, 255, 255])
    mask = cv2.inRange(hsvframe, lower_color, upper_color)
    mask1 = cv2.inRange(hsvframe, lower_barro, upper_barro)
    cv2.imshow('taco',mask)
    cv2.imshow('tac',mask1)
    cv2.imshow('tarro',frame)

    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()