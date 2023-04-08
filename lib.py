import numpy as np
import matplotlib.pyplot as plt
import multiprocessing
from PIL import Image
from numba import njit
import random


objetos:int = 1

# Filtro promedio 3x3
def filt_prome(tam):
    kernel = tam
    filtro = np.ones((kernel, kernel)) / kernel**2
    return filtro
@njit
def filt_gaussian(tam, sigma:float):
    m_half = tam // 2
    n_half = tam // 2
    gaussian_filter = np.zeros((tam, tam), np.float32)

    # generating the filter
    for y in range(-m_half, m_half):
        for x in range(-n_half, n_half):
            normal = 1 / (2.0 * np.pi * sigma**2.0)
            exp_term = np.exp(-(x**2.0 + y**2.0) / (2.0 * sigma**2.0))
            gaussian_filter[y+m_half, x+n_half] = normal * exp_term
    return gaussian_filter

def img_central(imagen: Image, filtro):
    width, height = imagen.size
    borde = filtro.shape[0] // 2
    matriz = np.zeros((width + 2 * borde, height + 2 * borde))

    # Rellenar la matriz con los valores de la imagen
    for x in range(width):
        for y in range(height):
            matriz[x + borde, y + borde] = imagen.getpixel((x, y))
    return matriz


filtro_redre = np.array([[-1,-1,-1],
                  [-1, 8,-1],
                   [-1,-1,-1]])


filtro_shapen =np.array([[-1,-1,-1],
                        [-1,9,-1],
                        [-1,-1,-1]])

filtro_gaussian3x3 =np.array([[-1,-1,-1],
                 [-1,9,-1],
                 [-1,-1,-1]])

filtro_roberts= np.array([[-1,-1],
                          [1,1]] )

filtro_solberx =  np.array( [[-1,0,1],
                            [-2,0,2],
                            [-1,0,1]] )

filtro_solbery =  np.array( [[-1,-2,-1],
                            [0,0,0],
                            [-1,-2,1]])

prewittx = np.array([[1,1,1],
                    [0,0,0],
                    [-1,-1,-1]])

prewitty = np.array([[-1,0,1],
                    [-1,0,1],
                    [-1,0,1]])

def convo(imagen,filtro,matriz):
    width, height = imagen.size
    imagen_filt = Image.new('L', (width, height))
    for x in range(width):
        for y in range(height):
            suma = 0
            for i in range(filtro.shape[0]):
                for j in range(filtro.shape[1]):
                    suma = suma + (matriz[x + i, y + j] * filtro[i, j])
                    suma += (matriz[x + i, y + j] * filtro[i, j])
            # Asegurarse de que el valor esté en el rango [0, 255]
            valor = int(max(0, min(suma, 255)))
            imagen_filt.putpixel((x, y), valor)
    return imagen_filt




def img_resta(imagen,imagen_filt):
    width, height = imagen.size
    imagen_know = Image.new('L', (width, height))
    for x in range(width):
        for y in range(height):
            imagen_know.putpixel((x,y),(imagen.getpixel((x,y))-imagen_filt.getpixel((x,y))))
    return imagen_know

def img_sum(imagen,imagen_filt):
    width, height = imagen.size
    imagen_know = Image.new('L', (width, height))
    for x in range(width):
        for y in range(height):
            imagen_know.putpixel((x,y),(imagen.getpixel((x,y))+imagen_filt.getpixel((x,y))))
    return imagen_know

def prewitt(img):
    imagen_know = img_sum(convo(img,prewittx,img_central(img,prewittx)),convo(img,prewitty,img_central(img,prewitty)))
    return imagen_know

def filtro_solber(img):
    imagen_know = img_sum(convo(img,filtro_solberx,img_central(img,filtro_solberx)),convo(img,filtro_solbery,img_central(img,filtro_solbery)))
    return imagen_know


@njit
def conteo_obj_8N(img: np.ndarray[(1024,1024), int]) -> int:
    alto, ancho = img.shape
    imgM = np.zeros((alto, ancho))
    x, y, a = 0,0,0
    ay, ax = 0,0
    my, mx = 0,0
    tao = 0
    tono = img[y,x]
    nTono = 255
    while alto*ancho !=a:
        #vecinos
        if img[y,x] == tono and imgM[y,x]==0:
            imgM[y,x] = nTono #Para visualizar lo que pasa se punta una matriz vacia
            if my < y:
                my=y #se cambia el maxima altura de la forma geometrica
            if mx < x:
                mx=x #se cambia el maxima anchura de la forma geometrica
            #vecino arriba
            if y>0 and x> 0 and imgM[y-1,x-1] == 0 and img[y-1,x-1]==tono:
                y-=1
                x-=1
            elif y>0 and imgM[y-1,x] == 0 and img[y-1,x]==tono:
                y-=1
            #vecino derecha
            elif x<ancho-1 and y>0 and imgM[y-1,x+1] == 0 and img[y-1,x+1]==tono:
                x+=1
                y-=1
            elif x<ancho-1 and imgM[y,x+1] == 0 and img[y,x+1]==tono:
                x+=1
            #vecino abajo
            elif y<alto-1 and x<ancho-1 and imgM[y+1,x+1] == 0 and img[y+1,x+1] == tono:
                y+=1
                x+=1
            elif y<alto-1 and imgM[y+1,x] == 0 and img[y+1,x] == tono:
                y+=1
            #vecino izquierda
            elif x>0 and y < alto-1 and imgM[y+1,x-1]== 0 and img[y+1,x-1]==tono:
                x-=1
                y+=1
            elif x>0 and imgM[y,x-1]== 0 and img[y,x-1]==tono:
                x-=1
                
            else:
                #comprovar que se relleno todo el objeto
                for j in range(ay,my+1):
                    for i in range(ax,mx+1):
                        if (imgM[ay+1,ax+1] == 0 and img[ay-1,ax-1]==tono) or \
                            (imgM[ay+1,ax] == 0 and img[ay-1,ax]==tono) or \
                            (imgM[ay+1,ax-1] == 0 and img[ay-1,ax+1]==tono) or \
                            (imgM[ay,ax-1] == 0 and img[ay,ax+1]==tono) or \
                            (imgM[ay-1,ax+1] == 0 and img[ay+1,ax+1] == tono) or\
                            (imgM[ay-1,ax] == 0 and img[ay+1,ax] == tono) or\
                            (imgM[ay-1,ax+1]== 0 and img[ay+1,ax-1]==tono) or\
                            (imgM[ay,ax+1]== 0 and img[ay,ax-1]==tono):
                            if img[j,i]==tono and imgM[j,i]== 0:
                                y = j
                                ay = j
                                x = i
                                break
                    else:
                        continue
                    break
                
        else:
            #se llega aqui cuando los pixeles de la figura creada ya esta
            for ji in range(alto):
                for ii in range(ancho):
                    if imgM[ji,ii]==0 :
                        x = ii
                        y = ji
                        ay=ji
                        ax=ii
                        tono = img[ji,ii]
                        tao +=1
                        if nTono<100:
                            nTono = random.randint(100,255)
                        nTono = nTono // 2
                        break  
                else:
                    continue
                break   

            
            
        a+=1
    return imgM
@njit
def conteo_obj_4N(img):#img es una mariz numpy que previamente era una imagen de PIL
    alto, ancho = img.shape
    imgM = np.zeros((alto, ancho))
    x, y, a = 0,0,0
    ay, ax = 0,0
    my, mx = 0,0
    tao = 0
    tono = img[y,x]
    nTono = 255
    while alto*ancho !=a:
        #vecinos
        if img[y,x] == tono and imgM[y,x]==0:
            imgM[y,x] = nTono #Para visualizar lo que pasa se punta una matriz vacia
            if my < y:
                my=y #se cambia el maxima altura de la forma geometrica
            if mx < x:
                mx=x #se cambia el maxima anchura de la forma geometrica
            #vecino arriba
            if y>0 and imgM[y-1,x] == 0 and img[y-1,x]==tono:
                y-=1
            #vecino derecha
            elif x<ancho-1 and imgM[y,x+1] == 0 and img[y,x+1]==tono:
                x+=1
            #vecino abajo
            elif y<alto-1 and imgM[y+1,x] == 0 and img[y+1,x] == tono:
                y+=1
            #vecino izquierda
            elif x>0 and imgM[y,x-1]== 0 and img[y,x-1]==tono:
                x-=1
            else:
                #comprovar que se relleno todo el objeto
                for j in range(ay,my+1):
                    for i in range(ax,mx+1):
                        if (imgM[ay+1,ax] == 0 and img[ay-1,ax]==tono) or \
                            (imgM[ay,ax-1] == 0 and img[ay,ax+1]==tono) or \
                            (imgM[ay-1,ax] == 0 and img[ay+1,ax] == tono) or\
                            (imgM[ay,ax+1]== 0 and img[ay,ax-1]==tono):
                            if img[j,i]==tono and imgM[j,i]== 0:
                                y = j
                                ay = j
                                x = i
                                break
                    else:
                        continue
                    break
        
        else:
            #se llega aqui cuando los pixeles de la figura creada ya esta
            for ji in range(alto):
                for ii in range(ancho):
                    if imgM[ji,ii]==0 :
                        x = ii
                        y = ji
                        ay=ji
                        ax=ii
                        tono = img[ji,ii]
                        tao +=1
                        if nTono<100:
                            nTono = random.randint(100,255)
                        nTono = nTono // 2
                        break  
                else:
                    continue
                break

    
            
            
        a+=1
    return imgM
@njit
def conteo_obj_4D(img: np.ndarray[(1024,1024), int]) -> int:
    alto, ancho = img.shape
    imgM = np.zeros((alto, ancho))
    x, y, a = 0,0,0
    ay, ax = 0,0
    my, mx = 0,0
    tao = 0
    tono = img[y,x]
    nTono = 255
    while alto*ancho !=a:
        #vecinos
        if img[y,x] == tono and imgM[y,x]==0:
            imgM[y,x] = nTono #Para visualizar lo que pasa se punta una matriz vacia
            if my < y:
                my=y #se cambia el maxima altura de la forma geometrica
            if mx < x:
                mx=x #se cambia el maxima anchura de la forma geometrica
            #vecino arriba
            if y>0 and x> 0 and imgM[y-1,x-1] == 0 and img[y-1,x-1]==tono:
                y-=1
                x-=1
            #vecino derecha
            elif x<ancho-1 and y>0 and imgM[y-1,x+1] == 0 and img[y-1,x+1]==tono:
                x+=1
                y-=1
            #vecino abajo
            elif y<alto-1 and x<ancho-1 and imgM[y+1,x+1] == 0 and img[y+1,x+1] == tono:
                y+=1
                x+=1
            #vecino izquierda
            elif x>0 and y < alto-1 and imgM[y+1,x-1]== 0 and img[y+1,x-1]==tono:
                x-=1
                y+=1
            else:
                #comprovar que se relleno todo el objeto
                for j in range(ay,my+1):
                    for i in range(ax,mx+1):
                        if (imgM[ay+1,ax+1] == 0 and img[ay-1,ax-1]==tono) or \
                            (imgM[ay+1,ax-1] == 0 and img[ay-1,ax+1]==tono) or \
                            (imgM[ay-1,ax+1] == 0 and img[ay+1,ax+1] == tono) or\
                            (imgM[ay-1,ax+1]== 0 and img[ay+1,ax-1]==tono):
                            if img[j,i]==tono and imgM[j,i]== 0:
                                y = j
                                ay = j
                                x = i
                                break
                    else:
                        continue
                    break
                
        else:
            #se llega aqui cuando los pixeles de la figura creada ya esta
            for ji in range(alto):
                for ii in range(ancho):
                    if imgM[ji,ii]==0 :
                        x = ii
                        y = ji
                        ay=ji
                        ax=ii
                        tono = img[ji,ii]
                        tao +=1
                        if nTono<100:
                            nTono = random.randint(100,255)
                        nTono = nTono // 2
                        break  
                else:
                    continue
                break   

            
            
        a+=1
    return imgM

def filtro_mediana(img: Image) -> Image:
    
    filtro = np.ones(3,3)
    
    matriz= img_central(img,filtro)
    width, height = img.size
    imagen_filt = Image.new('L', (width, height))
    te = 0
    c = 1
    for x in range(width):
        for y in range(height):
            for i in range(filtro.shape[0]):
                for j in range(filtro.shape[1]):
                    if j+1 < width-1 and matriz[x, j] > matriz[x, j+1]:
                        te = img
                        matriz[i,j] = matriz[i,j+1]
                        matriz[i, j+1] = te
                        
            te = matriz[1,1]
            # Asegurarse de que el valor esté en el rango [0, 255]
            imagen_filt.putpixel((x, y), te)
    return imagen_filt

def filtro_menimo(img: Image) -> Image:
    matriz= img_central(img)
    filtro = np.ones(3,3)
    width, height = img.size
    imagen_filt = Image.new('L', (width, height))
    te = 0
    c = 1
    for x in range(width):
        for y in range(height):
            for i in range(filtro.shape[0]):
                for j in range(filtro.shape[1]):
                    if j+1 < width-1 and matriz[x, j] > matriz[x, j+1]:
                        te = matriz[x, j+1]
                        
            # Asegurarse de que el valor esté en el rango [0, 255]
            imagen_filt.putpixel((x, y), te)
    return imagen_filt



def filtro_bancos(img: Image) -> Image:
    width, height = img.size
    imagen_filt = Image.new('L', (width, height))
    te = 0
    c = 1
    for x in range(width):
        for y in range(height):
            if img.getpixel((x,y))==255:
                if y > 0 and img.getpixel((x, y-1)) != 255 :
                    te1 = 0
                    te1 = img.getpixel((x,y-1))
                if x < width-1 and img.getpixel((x+1, y)) != 255:
                    te2 = 0
                    te2 = img.getpixel((x+1,y))
                if y < height-1 and img.getpixel((x, y+1)) != 255:
                    te3 = 0
                    te3 = img.getpixel((x,y+1))
                if x > 0 and img.getpixel((x-1, y)) != 255:
                    te4 = 0
                    te4 = img.getpixel((x-1,y))
                te = (te1+te2+te3+te4)//4

            # Asegurarse de que el valor esté en el rango [0, 255]
            imagen_filt.putpixel((x, y), te)
    return imagen_filt

def filtro_negros(img: Image) -> Image:
    width, height = img.size
    imagen_filt = Image.new('L', (width, height))
    te = 0
    c = 1
    for x in range(width):
        for y in range(height):
            if img.getpixel((x,y))==0:
                if y > 0 and img.getpixel((x, y-1)) != 0 :
                    te1 = 0
                    te1 = img.getpixel((x,y-1))
                if x < width-1 and img.getpixel((x+1, y)) != 0:
                    te2 = 0
                    te2 = img.getpixel((x+1,y))
                if y < height-1 and img.getpixel((x, y+1)) != 0:
                    te3 = 0
                    te3 = img.getpixel((x,y+1))
                if x > 0 and img.getpixel((x-1, y)) != 0:
                    te4 = 0
                    te4 = img.getpixel((x-1,y))
                te = (te1+te2+te3+te4)//4

            # Asegurarse de que el valor esté en el rango [0, 255]
            imagen_filt.putpixel((x, y), te)
    return imagen_filt

def nuevoG(arr):
    alto, ancho = arr.shape
    img = Image.new('L', (ancho, alto))
    for y in range(alto):
        for x in range(ancho):
            img.putpixel((x, y), int(arr[y, x]))
    return img

def euclidianoP(img):
    alto, ancho =img.shape
    xa = -ancho//2
    xb = ancho//2
    ya = -alto//2
    yb = alto//2

    a = ((xb-xa)**2+(ya-ya))**0.5
    b = ((xb-xb)**2+(yb-ya)**2)**0.5
    c = ((xa-xb)**2+(yb-yb))**0.5
    d = ((xa-xa)**2+(ya-yb)**2)**0.5
    suma = a+b+c+d
    return suma
@njit
def umbra(img):
    alto, ancho = img.shape
    for y in range (alto):
        for x in range (ancho):
            if img[y,x]>90:
                img[y,x] = 255
            else:
                img[y,x] = 0
    return img
