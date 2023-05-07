import numpy as np
import os
from PIL import Image



estruc3x3 =np.array([[255,255,255],
            [255,255,255],
            [255,255,255]],dtype=np.uint8)

estrucCruz = np.array([[0,255,0],
            [255,255,255],
              [0,255,0]],dtype=np.uint8)

estruc5x5 =np.array([[255,255,255,255,255],
          [255,255,255,255,255],
          [255,255,255,255,255],
          [255,255,255,255,255],
          [255,255,255,255,255]],dtype=np.uint8)
estrucCirculo =np.array([  [0,255,255,255,0],
                [255,255,255,255,255],
                [255,255,255,255,255],
                [255,255,255,255,255],
                  [0,255,255,255,0]],dtype=np.uint8)

def dilatacion(prueba,filtro):
    alto, ancho=filtro.shape
    ft = alto//2
    alto, ancho = prueba.shape
    npImagen = np.zeros_like(prueba)
    npImagen[ prueba >=150] = 255
    npPrueba=npImagen.copy()
    for y in range(ft,alto-1-ft):
        for x in range(ft,ancho-1-ft):
            if npPrueba[y,x] == filtro[ft,ft]:
                npImagen[y-ft:y+ft+1, x-ft:x+ft+1] += filtro
                temp = npImagen[y-ft:y+ft+1, x-ft:x+ft+1].copy()
                temp[temp==254]=255
                npImagen[y-ft:y+ft+1, x-ft:x+ft+1]=temp
    return npImagen
def erosion(prueba,filtro):
    alto, ancho=filtro.shape
    ft = alto//2
    alto, ancho = prueba.shape
    npImagen = np.zeros_like(prueba)
    npImagen[ prueba >=150] = 255
    npPrueba=npImagen.copy()
    for y in range(ft,alto-1-ft):
        for x in range(ft,ancho-1-ft):
            if npPrueba[y,x] != filtro[ft,ft]:
                npImagen[y-ft:y+ft+1, x-ft:x+ft+1] -= filtro
                temp = npImagen[y-ft:y+ft+1, x-ft:x+ft+1].copy()
                temp[temp==1]=0
                npImagen[y-ft:y+ft+1, x-ft:x+ft+1]=temp
    return npImagen
def cierre(url,filtro):
    dilata=dilatacion(url,filtro=filtro)
    cierre=erosion(dilata,filtro=filtro)
    return cierre
def apertura(url,filtro):
    ero=erosion(url,filtro=filtro)
    apertu=dilatacion(ero,filtro=filtro)
    return apertu
def gradienteMorfo(url,filtro):
    resta=dilatacion(url,filtro)-erosion(url,filtro)
    return resta


url ="LogosUMNGabiertos.png"
prueba = Image.open(url).convert("L")
prueba.show()
preuba = np.array(prueba)
while(True):
    tipo = input("Ingrese 1 para dilatación\n2 para erosión\n3 para cierre\n4 para apartura\n5 para gradiente morfologico\n")
    tipo =int(tipo)
    print("Se ingreso", tipo)
    if tipo == 1:
        tip = input("Ingrese 1 para estruc3x3\n 2 para estrucCruz\n 3 para estruc5x5\n 4 para estrucCirculo\n")
        print("Se ingreso", tipo)
        tipo =int(tipo)
        if tipo == 1:
            apunta = dilatacion(preuba,estruc3x3)
            apunta= Image.fromarray(apunta)
            apunta.show()
        if tipo == 2:
            apunta = dilatacion(preuba,estrucCruz)
            apunta= Image.fromarray(apunta)
            apunta.show()
        if tipo == 3:
            apunta = dilatacion(preuba,estruc5x5)
            apunta= Image.fromarray(apunta)
            apunta.show()
        if tipo == 4:
            apunta = dilatacion(preuba,estrucCirculo)
            apunta= Image.fromarray(apunta)
            apunta.show()
    if tipo == 2:
        tipo = input("Ingrese 1 para estruc3x3\n 2 para estrucCruz\n 3 para estruc5x5\n 4 para estrucCirculo\n")
        print("Se ingreso", tipo)
        tipo =int(tipo)
        if tipo == 1:
            apunta = erosion(preuba,estruc3x3)
            apunta= Image.fromarray(apunta)
            apunta.show()
        if tipo == 2:
            apunta = erosion(preuba,estrucCruz)
            apunta= Image.fromarray(apunta)
            apunta.show()
        if tipo == 3:
            apunta = erosion(preuba,estruc5x5)
            apunta= Image.fromarray(apunta)
            apunta.show()
        if tipo == 4:
            apunta = erosion(preuba,estrucCirculo)
            apunta= Image.fromarray(apunta)
            apunta.show()
    if tipo == 3:
        tipo = input("Ingrese 1 para estruc3x3\n 2 para estrucCruz\n 3 para estruc5x5\n 4 para estrucCirculo\n")
        print("Se ingreso", tipo)
        tipo =int(tipo)
        if tipo == 1:
            apunta = cierre(preuba,estruc3x3)
            apunta= Image.fromarray(apunta)
            apunta.show()
        if tipo == 2:
            apunta = cierre(preuba,estrucCruz)
            apunta= Image.fromarray(apunta)
            apunta.show()
        if tipo == 3:
            apunta = cierre(preuba,estruc5x5)
            apunta= Image.fromarray(apunta)
            apunta.show()
        if tipo == 4:
            apunta = cierre(preuba,estrucCirculo)
            apunta= Image.fromarray(apunta)
            apunta.show()
    if tipo == 4:
        tipo = input("Ingrese 1 para estruc3x3\n 2 para estrucCruz\n 3 para estruc5x5\n 4 para estrucCirculo\n")
        print("Se ingreso", tipo)
        tipo =int(tipo)
        if tipo == 1:
            apunta = apertura(preuba,estruc3x3)
            apunta= Image.fromarray(apunta)
            apunta.show()
        if tipo == 2:
            apunta = apertura(preuba,estrucCruz)
            apunta= Image.fromarray(apunta)
            apunta.show()
        if tipo == 3:
            apunta = apertura(preuba,estruc5x5)
            apunta= Image.fromarray(apunta)
            apunta.show()
        if tipo == 4:
            apunta = apertura(preuba,estrucCirculo)
            apunta= Image.fromarray(apunta)
            apunta.show()
    if tipo == 5:
        tipo = input("Ingrese 1 para estruc3x3\n 2 para estrucCruz\n 3 para estruc5x5\n 4 para estrucCirculo\n")
        print("Se ingreso", tipo)
        tipo =int(tipo)
        if tipo == 1:
            apunta = gradienteMorfo(preuba,estruc3x3)
            apunta= Image.fromarray(apunta)
            apunta.show()
        if tipo == 2:
            apunta = gradienteMorfo(preuba,estrucCruz)
            apunta= Image.fromarray(apunta)
            apunta.show()
        if tipo == 3:
            apunta = gradienteMorfo(preuba,estruc5x5)
            apunta= Image.fromarray(apunta)
            apunta.show()
        if tipo == 4:
            apunta = gradienteMorfo(preuba,estrucCirculo)
            apunta= Image.fromarray(apunta)
            apunta.show()
    os.system("cls")


