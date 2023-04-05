from PIL import Image
import numpy as np
import os

#definicion para obtener el umbral
def umbra(img):
    alto, ancho = img.shape
    for y in range (alto):
        for x in range (ancho):
            if img[y,x]>100:
                img[y,x] = 255
            else:
                img[y,x] = 0
    return img

#===============================================================================================================
#FUNCION PRINCIPAL
#===============================================================================================================

#Llamamos a la iamgen - cambiar ruta si es necesario
foto=Image.open('ConvulusionImg\segmentacion\chess.jpg')
#si la imagen no es a escala de grises se hace la conversion
foto=foto.convert('L')
width, height = foto.size
#============== OLD UMBRAL =====================
#el umbral esta forzosamente comprendido entre 1 y 254 para las
#imagenes de 8 bits a escala de grises
#umbral=64
#============== /OLD UMBRAL =====================
#============= UMBRAL ======================
#se intentara simplificar la funcion con un array que contenga los datos de la foto/imagen
#debemos convertir la imagen a un arreglo que contenga los valores de cada pixel de la matriz.
umbral = umbra(np.array(foto))
#============= /UMBRAL ======================
#============= LLAMADO A FUNCIONES ======================
a=1
while a==1:
    nombre = input("ingresa:\n1 para Segmetnación por Otsu\n2 para Segmetnación por Bordes\n3 para Segmetnación por Crecimiento de regiones")
    print("se ingrso: ", nombre)
    if nombre=="1":
        #===============================================================================================================
        #METODO OTSU
        #===============================================================================================================
        #agrega los nuevos datos de la iamgen a nueva_imagen
        image_otsu = Image.fromarray(umbral)
        #renombra y guarda la imagen ya 'otsurizada'
        image_otsu.save('ConvulusionImg\segmentacion\chess-otsu.jpg')
        image_otsu.show()
        foto.close()
        #imagen_otsu=otsu(foto,umbral)
        print("Se completó la funcion de segmentacion por otsu.")
    if nombre=="2":
        #===============================================================================================================
        #METODO DETECCION BORDES
        #===============================================================================================================
        
    if nombre=="3":
        #===============================================================================================================
        #METODO CRECIMIENTO DE REGIONES
        #===============================================================================================================
        
    if nombre == "salir":
        os.system("cls")
        break
    else:
        print("lo sentimos, no ingreaste un valor exixtente")