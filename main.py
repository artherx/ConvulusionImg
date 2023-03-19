import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


imagen = Image.open('assets\img\2022-Tesla-Model-S-8.jpg')

imagenBL = imagen.convert('L')
imagenBL1 = imagen.convert('L')
imagenBL2 = imagen.convert('L')

width, high = imagenBL.size




n=3
lados = int((n-1)/2)
suma=0
matriz = np.zeros((width+(lados*2), high+(lados*2)))

for x in range(width):
    for y in range(high):
        matriz[x+lados,y+lados] = imagenBL.getpixel((x,y))


for x in range(lados,width+(lados*2)):
    for y in range(lados,high+(lados*2)):
        for pasX in range(n):
            for pasY in range(n):
                suma+=matriz[x,y]
        if suma >256:
            suma=255
        elif suma < -1:
            suma = 0
        imagenBL1.putpixel((x-(lados*2),y-(lados*2)),int(suma/(n*n)))
        suma = 0

for x in range(width):
   for y in range(high):
      imagenBL1.putpixel((x,y),(imagenBL.getpixel((x,y))-imagenBL1.getpixel((x,y))))
      
imagenBL.show()
imagenBL1.show()
imagenBL2.show()