import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import random


# Filtro promedio 3x3
def filt_prome(tam):
    kernel = tam
    filtro = np.ones((kernel, kernel)) / kernel**2
    return filtro

def filt_gaussian(tam, sigma:float):
    kernel = tam
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

def img_central(imagen, filtro):
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

def conteo_obj_4N(img: Image) -> Image:
    anch, alto = img.size
    imgM = Image.new('L', (anch, alto))
    a = 0
    x:int = 0
    y:int = 0
    tono = img.getpixel((x,y))
    nTono = 255

    while anch*alto != a :
        if img.getpixel((x,y)) == tono and imgM.getpixel((x, y)) == 0:
            imgM.putpixel((x,y), nTono)
            #print("color colocado:", imgM.getpixel((x, y)), " X:", x, " Y:", y)
            if (y > 0 and imgM.getpixel((x, y-1)) == 0) or \
               (x < anch-1 and imgM.getpixel((x+1, y)) == 0) or \
               (y < alto-1 and imgM.getpixel((x, y+1)) == 0) or \
               (x > 0 and imgM.getpixel((x-1, y)) == 0):
                if y > 0 and imgM.getpixel((x, y-1)) == 0 and img.getpixel((x, y-1))==tono:
                    y-=1
                elif x < anch-1 and imgM.getpixel((x+1, y)) == 0 and img.getpixel((x+1, y))==tono:
                    x+=1
                elif y < alto-1 and imgM.getpixel((x, y+1)) == 0 and img.getpixel((x, y+1))==tono:
                    y+=1
                elif x > 0 and imgM.getpixel((x-1, y)) == 0 and img.getpixel((x-1, y))==tono:
                    x-=1
                #print(" fX:", x, " fY:", y)
                
                
        else:
            #print("no se mueve")
            for i in range(anch):
                for j in range(alto):
                    if imgM.getpixel((i,j))==0:
                        tono = img.getpixel((i,j))
                        nTono = nTono//2
                    if i == anch-1 and j == alto-1 and imgM.getpixel((i,j))!=0:
                        a = anch*alto

            

        a+=1
    
    return imgM

def conteo_obj_8N(img: Image) -> Image:
    anch, alto = img.size
    imgM = Image.new('L', (anch, alto))
    a = 0
    x:int = 0
    y:int = 0
    tono = img.getpixel((x,y))
    nTono = 255

    while anch*alto != a :
        if img.getpixel((x,y)) == tono and imgM.getpixel((x, y)) == 0:
            imgM.putpixel((x,y), nTono)
            #print("color colocado:", imgM.getpixel((x, y)), " X:", x, " Y:", y)
            if (x> 0 and y > 0 and imgM.getpixel((x-1, y-1)) == 0) or \
                (y > 0 and imgM.getpixel((x, y-1)) == 0) or \
               (x < anch-1 and y > 0 and imgM.getpixel((x+1, y-1)) == 0) or \
               (x < anch-1 and imgM.getpixel((x+1, y)) == 0) or \
               (y < alto-1 and x < anch-1 and imgM.getpixel((x+1, y+1)) == 0) or \
               (y < alto-1 and imgM.getpixel((x, y+1)) == 0) or \
               (x > 0 and y < alto-1 and imgM.getpixel((x-1, y+1)) == 0) or \
                (x > 0 and imgM.getpixel((x-1, y)) == 0):
                if x> 0 and y > 0 and imgM.getpixel((x-1, y-1)) == 0 and img.getpixel((x, y-1))==tono:
                    y-=1
                    x-=1
                elif y > 0 and imgM.getpixel((x, y-1)) == 0 and img.getpixel((x, y-1))==tono:
                    y-=1
                elif x < anch-1 and y > 0 and imgM.getpixel((x+1, y-1)) == 0 and img.getpixel((x+1, y))==tono:
                    x+=1
                    y-=1
                elif x < anch-1 and imgM.getpixel((x+1, y)) == 0 and img.getpixel((x+1, y))==tono:
                    x+=1
                elif y < alto-1 and x < anch-1 and imgM.getpixel((x+1, y+1)) == 0 and img.getpixel((x, y+1))==tono:
                    y+=1
                    x+=1
                elif y < alto-1 and imgM.getpixel((x, y+1)) == 0 and img.getpixel((x, y+1))==tono:
                    y+=1
                elif x > 0 and y < alto-1 and imgM.getpixel((x-1, y + 1)) == 0 and img.getpixel((x-1, y))==tono:
                    x-=1
                    y+=1
                elif x > 0 and imgM.getpixel((x-1, y)) == 0 and img.getpixel((x-1, y))==tono:
                    x-=1
                #print(" fX:", x, " fY:", y)
                
       
        else:
            #print("no se mueve")
            for i in range(anch):
                for j in range(alto):
                    if imgM.getpixel((i,j))==0:
                        tono = img.getpixel((i,j))
                        nTono = nTono//2
                    if i == anch-1 and j == alto-1 and imgM.getpixel((i,j))!=0:
                        a = anch*alto
            

        a+=1
    
    return imgM

def conteo_obj_4D(img: Image) -> Image:
    anch, alto = img.size
    imgM = Image.new('L', (anch, alto))
    a = 0
    x:int = 0
    y:int = 0
    tono = img.getpixel((x,y))
    nTono = 255

    while anch*alto != a :
        if img.getpixel((x,y)) == tono and imgM.getpixel((x, y)) == 0:
            imgM.putpixel((x,y), nTono)
            #print("color colocado:", imgM.getpixel((x, y)), " X:", x, " Y:", y)
            if (x> 0 and y > 0 and imgM.getpixel((x-1, y-1)) == 0) or \
               (x < anch-1 and y > 0 and imgM.getpixel((x+1, y-1)) == 0) or \
               (y < alto-1 and x < anch-1 and imgM.getpixel((x+1, y+1)) == 0) or \
               (x > 0 and y < alto-1 and imgM.getpixel((x-1, y+1)) == 0):
                if x> 0 and y > 0 and imgM.getpixel((x-1, y-1)) == 0 and img.getpixel((x, y-1))==tono:
                    y-=1
                    x-=1
                elif x < anch-1 and y > 0 and imgM.getpixel((x+1, y-1)) == 0 and img.getpixel((x+1, y))==tono:
                    x+=1
                    y-=1
                elif y < alto-1 and x < anch-1 and imgM.getpixel((x+1, y+1)) == 0 and img.getpixel((x, y+1))==tono:
                    y+=1
                    x+=1
                elif x > 0 and y < alto-1 and imgM.getpixel((x-1, y + 1)) == 0 and img.getpixel((x-1, y))==tono:
                    x-=1
                    y+=1
                #print(" fX:", x, " fY:", y)
                
       
        else:
            #print("no se mueve")
            for i in range(anch):
                for j in range(alto):
                    if imgM.getpixel((i,j))==0:
                        tono = img.getpixel((i,j))
                        nTono = nTono//2
                    if i == anch-1 and j == alto-1 and imgM.getpixel((i,j))!=0:
                        a = anch*alto
           

            

        a+=1
    
    return imgM

def filtro_mediana(img: Image) -> Image:
    
    filtro = np.array([[1,1,1],
              [1,1,1],
              [1,1,1]])
    
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
    filtro = [1]*9
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
    filtro = [1]*9
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
    filtro = [1]*9
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