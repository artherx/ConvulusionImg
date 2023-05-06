import numpy as np
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
prueba = np.array(prueba)
preuba= gradienteMorfo(prueba,estrucCirculo)
preuba= Image.fromarray(preuba)
preuba.show()
