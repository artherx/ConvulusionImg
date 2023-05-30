import cv2
import numpy as np

# Crear el objeto VideoCapture para acceder a la cámara
cap = cv2.VideoCapture(701)  # 0 indica el índice de la cámara predeterminada

# Verificar si la cámara se abrió correctamente
if not cap.isOpened():
    print("No se pudo abrir la cámara")
    exit()

kernel = np.ones((5, 5), np.uint8)

# Definir los rangos de color para la resistencia (verde)
lower_color = np.array([30,52,30])
upper_color = np.array([85, 255, 255])
#negro
RangooscuroN= np.array([0, 0, 0])
RangoclaroN= np.array([10, 10, 10])
#Marrón:

RangooscuroM= np.array([10, 100, 20])
RangoclaroM= np.array([20, 250, 30])
#Rojo:

RangooscuroR= np.array([0, 100, 100])
RangoclaroR= np.array([5, 255, 255])
#Naranja:

RangooscuroNa=np.array ([6, 100, 100])
RangoclaroNa= np.array([12, 255, 255])
#Amarllo:np.array
RangooscuroA=np.array ([15, 100, 100])
RangoclaroA= np.array([25, 255, 255])
#Azulnp.array
RangooscuroAz=np.array ([90, 100, 100])
RangoclaroAz= np.array([130, 255, 255])
#Violta:np.array
RangooscuroV=np.array ([131, 100, 100])
RangoclaroV= np.array([155, 255, 255])
#Grinp.array
RangooscuroG=np.array ([0, 0, 50])
RangoclaroG= np.array([179, 30, 220])
#Blanco:np.array
RangooscuroB= np.array([0, 0, 221])
RangoclaroB=np.array([179, 30, 255])
#Dorado
RangooscuroDo= np.array([11, 100, 100])
RangoclaroPDo= np.array([25, 255, 255])
#plata
RangooscuroP = np.array([0, 0, 180])
RangoclaroP = np.array([180, 30, 255])
resistencias ={
    'contours_mask0':"0",
    'contours_mask1':"1",
    'contours_mask2':"2",
    'contours_mask3':"3",
    'contours_mask4':"4",
    'contours_mask5':"5",
    'contours_mask6':"6",
    'contours_mask7':"7",
    'contours_mask8':"8",
    'contours_mask9':"9",
    'contours_mask10':"5",
    'contours_mask11':"10"
}
#Plateado:
#Rango: ([0, 0, 150], [179, 30, 192])
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
        
        # Crear una máscara para los colores dentro del rango especificado
        mask = cv2.inRange(hsv_roi, RangooscuroN, RangoclaroN)
        mask1 = cv2.inRange(hsv_roi, RangooscuroM, RangoclaroM)
        mask2 = cv2.inRange(hsv_roi, RangooscuroR, RangoclaroR)
        mask3 = cv2.inRange(hsv_roi, RangooscuroNa, RangoclaroNa)
        mask4 = cv2.inRange(hsv_roi, RangooscuroA, RangoclaroA)
        mask5 = cv2.inRange(hsv_roi, lower_color, upper_color)
        mask6 = cv2.inRange(hsv_roi, RangooscuroAz, RangoclaroAz)
        mask7 = cv2.inRange(hsv_roi, RangooscuroV, RangoclaroV)
        mask8 = cv2.inRange(hsv_roi, RangooscuroG, RangoclaroG)
        mask9 = cv2.inRange(hsv_roi, RangooscuroB, RangoclaroB)
        mask10 = cv2.inRange(hsv_roi, RangooscuroDo, RangoclaroPDo)
        mask11 = cv2.inRange(hsv_roi, RangooscuroP, RangoclaroP)
        
        # Encontrar los contornos en la máscara
        misContornos = {

        }
        misContornos['contours_mask0'], _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_TC89_L1)
        misContornos['contours_mask1'], _ = cv2.findContours(mask1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_TC89_L1)
        misContornos['contours_mask2'], _ = cv2.findContours(mask2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_TC89_L1)
        misContornos['contours_mask3'], _ = cv2.findContours(mask3, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_TC89_L1)
        misContornos['contours_mask4'], _ = cv2.findContours(mask4, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_TC89_L1)
        misContornos['contours_mask5'], _ = cv2.findContours(mask5, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_TC89_L1)
        misContornos['contours_mask6'], _ = cv2.findContours(mask6, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_TC89_L1)
        misContornos['contours_mask7'], _ = cv2.findContours(mask7, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_TC89_L1)
        misContornos['contours_mask8'], _ = cv2.findContours(mask8, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_TC89_L1)
        misContornos['contours_mask9'], _ = cv2.findContours(mask9, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_TC89_L1)
        misContornos['contours_mask10'], _ = cv2.findContours(mask10, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_TC89_L1)
        misContornos['contours_mask11'], _ = cv2.findContours(mask11, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_TC89_L1)

        # Dibujar los contornos encontrados en el cuadro original
        
        
        
        vector=[]
        for i in range(9):
            if len(misContornos['contours_mask'+str(i)]) > 0:
                vector.append(i)
                if len(vector)>=3:
                    valor_resis= (int(resistencias["contours_mask"+str(vector[0])]+resistencias["contours_mask"+str(vector[1])])*pow(10,int(resistencias["contours_mask"+str(vector[2])])))
                    cv2.drawContours(roi, misContornos['contours_mask'+str(vector[0])], -1, (0, 255, 0), 2)
                    cv2.drawContours(roi, misContornos['contours_mask'+str(vector[1])], -1, (0, 255, 255), 2)
                    cv2.drawContours(roi, misContornos['contours_mask'+str(vector[2])], -1, (255, 255, 0), 2)
                    cv2.imshow("Roi", roi)
                    print("¡Color encontrado!"+str(valor_resis)+" ts "+ str(vector[0]) +str(vector[1])+str(vector[2]))

                else:
                    valor_resis= 0

        cv2.circle(draw,(cx,cy),3,(0,0,255),-1)
        cv2.putText(draw,"R/. "+str(valor_resis)+" ohmios "+str(resistencias['contours_mask10'])+"%",(cx+10,cy+10),font,0.5,(0,0,0),2)
        moneda+=1
    

    # Mostrar la imagen segmentada en una ventana
    cv2.imshow("Segmentación", draw)

    # Esperar la tecla 'q' para salir del bucle
    if cv2.waitKey(1) == ord('q'):
        break

# Liberar los recursos
cap.release()
cv2.destroyAllWindows()
