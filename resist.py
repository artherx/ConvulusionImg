import cv2
import numpy as np

# Crear el objeto VideoCapture para acceder a la cámara
cap = cv2.VideoCapture(701)  # 0 indica el índice de la cámara predeterminada

# Verificar si la cámara se abrió correctamente
if not cap.isOpened():
    print("No se pudo abrir la cámara")
    exit()

kernel = np.ones((5, 5), np.uint8)
# Bucle para capturar continuamente imágenes de la cámara
while True:
    # Leer el cuadro de la cámara
    ret, frame = cap.read()    # Verificar si el cuadro se leyó correctamente
    if not ret:
        print("No se pudo recibir el cuadro de la cámara")
        break



    # Convertir la imagen a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    gray = cv2.erode(gray,kernel,iterations=2)
    gray = cv2.dilate(gray,kernel,iterations=5)

    # Aplicar el algoritmo de detección de bordes (Canny)
    edges = cv2.Canny(gray, 100, 200)
    
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    font= cv2.FONT_HERSHEY_SIMPLEX
    draw= cv2.drawContours(frame.copy(),contours,-1,(255,0,0),2)
    moneda=1
    for i in contours:
        momento=cv2.moments(i)
        a= momento['m00']
        if a==0: a=1
        cx=int(momento['m10']/a)
        cy=int(momento['m01']/a)
        # Extraer la región de interés del contorno
        x, y, w, h = cv2.boundingRect(i)
        roi = frame[y:y+h, x:x+w]

        # Convertir la región de interés a espacio de color HSV
        hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

        # Definir los rangos de color para la resistencia (verde)
        lower_color = np.array([30,52,30])
        upper_color = np.array([85, 255, 255])

        # # Rango de color para el marrón
        # lower_brown = np.array([0, 20, 20])
        # upper_brown = np.array([40, 255, 255])

        # # Rango de color para el negro
        # lower_black = np.array([0, 0, 0])
        # upper_black = np.array([180, 255, 30])


        # Crear una máscara para los colores dentro del rango especificado
        mask = cv2.inRange(hsv_roi, lower_color, upper_color)

        # Encontrar los contornos en la máscara
        contours_mask, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Dibujar los contornos encontrados en el cuadro original
        cv2.drawContours(roi, contours_mask, -1, (0, 255, 0), 2)
        cv2.imshow("Roi", roi)
        
        cv2.circle(draw,(cx,cy),3,(0,0,255),-1)
        cv2.putText(draw,"R/. "+str(moneda),(cx+10,cy+10),font,0.5,(0,0,0),2)

        if len(contours_mask) > 0:
            print("¡Color encontrado!")

        moneda+=1
    

    # Mostrar la imagen segmentada en una ventana
    cv2.imshow("Segmentación", draw)

    # Esperar la tecla 'q' para salir del bucle
    if cv2.waitKey(1) == ord('q'):
        break

# Liberar los recursos
cap.release()
cv2.destroyAllWindows()
