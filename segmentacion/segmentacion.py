from PIL import Image
import numpy as np

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
foto=Image.open('chess.jpg')
#si la imagen no es a escala de grises se hace la conversion
if foto.mode != 'L':
    foto=foto.convert('L')

#============== OLD UMBRAL =====================
#el umbral esta forzosamente comprendido entre 1 y 254 para las
#imagenes de 8 bits a escala de grises
#umbral=64
#============== /OLD UMBRAL =====================

#============= UMBRAL ======================
#obtenemos el umbral de la imagen aplicando la funcion def 'umbra' (simplificacion en def)
umbral = umbra(foto)
#============= /UMBRAL ======================

#============= LLAMADO A FUNCIONES ======================

a=1
foto.show()
while a==1:
    nombre = input("ingresa:\n1 para Segmetnación por Otsu\n2 para Segmetnación por Bordes\n3 para Segmetnación por Crecimiento de regiones")
    print("se ingrso: ", nombre)
    if nombre=="1":
        width, height = foto.size
        #hace una copia de la imagen 'img' externa a 'def otsu' con las nuevas características
        img_otsu = Image.new('L', (width, height))
        #se intentara simplificar la funcion con un array que contenga los datos de la foto/imagen
        #debemos convertir la imagen a un arreglo que contenga los valores de cada pixel de la matriz.
        datos = np.array(foto)
        #realizamos la lectura de la imagen mediante for anidados
        for x in range(width):
            for y in range(height):
                #operacion: determina si CADA pixel X de Y es menor al del umbral
                if x < umbral:
                    # axis=0 -> row/fila
                    # axis=1 -> column/columna
                    # ,0, -> negro
                    # ,255, -> blanco
                    suma = 0
                    suma += (np.append(datos,0,axis=0))
                    continue
                #si es mayor o igual a umbral se agrega 255 en ves de 0
                np.append(datos,255,axis=0)
        #agrega los nuevos datos de la iamgen a img_otsu
        img_otsu.putdata(datos)
        #renombra y guarda la imagen ya 'otsurizada'
        img_otsu.save('chess-otsu.jpg')
        img_otsu.close()
        foto.close()
        #imagen_otsu=otsu(foto,umbral)
        print("Se completó la funcion de segmentacion por otsu.")
#============= /LLAMADO A FUNCIONES ======================

#===============================================================================================================
#METODO OTSU
#===============================================================================================================
def otsu(img,umbral):
    width, height = img.size
    #hace una copia de la imagen 'img' externa a 'def otsu' con las nuevas características
    img_otsu = Image.new('L', (width, height))
    #se intentara simplificar la funcion con un array que contenga los datos de la foto/imagen
    #debemos convertir la imagen a un arreglo que contenga los valores de cada pixel de la matriz.
    datos = np.array(img)
    #realizamos la lectura de la imagen mediante for anidados
    for x in range(width):
        for y in range(height):
            #operacion: determina si CADA pixel X de Y es menor al del umbral
            if x < umbral:
                # axis=0 -> row/fila
                # axis=1 -> column/columna
                # ,0, -> negro
                # ,255, -> blanco
                suma += (np.append(datos,0,axis=0))
                continue
            #si es mayor o igual a umbral se agrega 255 en ves de 0
            np.append(datos,255,axis=0)
    #agrega los nuevos datos de la iamgen a img_otsu
    img_otsu.putdata(datos)
    #renombra y guarda la imagen ya 'otsurizada'
    img_otsu.save('chess-otsu.jpg')
    #que retorna la funcion?
    #retorna la nueva imagen
    return img_otsu

#se obtienen los datos de los pixeles de la imagen
#cada pixel con su valor es dejado ahi con getdata()
#bonarios hace la funcion de alamcenarlos en un array ya preparada para contener los pixeles de la imagen
#datos=foto.getdata()
#datos_binarios=[]

#for x in datos:
    #hara el recorrido de cada x en cada y de la imagen hasta encontrar el umbral
#    if x<umbral:
        #agrega cada nuevo dato que lee y compara con el umbral
        #append concatena: agrega nuevos elementos en el vector, este caso: matrix.
#        datos_binarios.append(0)
#        continue
    #si es mayor o igual a umbral se agrega 1 en ves de 0
    #podria hacerse con 255 en ves de 1
#    datos_binarios.append(1)

#en caso de utilizar 255 como valor superior el metodo new
#llevaria 'L' en ves de '1' en el primer argumento
#otsu_imagen=Image.new('1', foto.size)
#otsu_imagen.putdata(datos_binarios)
#otsu_imagen.save('chess-otsu.jpg')

#otsu_imagen.close()
#foto.close()

#===============================================================================================================
#METODO DETECCION BORDES
#===============================================================================================================



#===============================================================================================================
#METODO CRECIMIENTO DE REGIONES
#===============================================================================================================