import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Cargar la imagen
imagen = Image.open('assets\img\papu2.jpg')

# Convertir a escala de grises
imagen = imagen.convert('L')

# Tamaño de la imagen
width, height = imagen.size

# Filtro promedio 3x3
kernel = 3
filtro = np.ones((kernel, kernel)) / kernel**2

#valores = np.array([[-1,-1,-1],
#                    [-1, 8,-1],
#                    [-1,-1,-1]])

#filtro[:3, :3] = valores

#filtro[:3,:3] = [[-1,-1,-1],[-1,8,-1],[-1,-1,-1]]

# Crear una matriz de ceros con borde de tamaño del filtro
borde = filtro.shape[0] // 2
matriz = np.zeros((width + 2 * borde, height + 2 * borde))

# Rellenar la matriz con los valores de la imagen
for x in range(width):
    for y in range(height):
        matriz[x + borde, y + borde] = imagen.getpixel((x, y))

# Aplicar el filtro a cada píxel de la imagen
imagen_filt = Image.new('L', (width, height))
for x in range(width):
    for y in range(height):
        suma = 0
        for i in range(filtro.shape[0]):
            for j in range(filtro.shape[1]):
                suma += matriz[x + i, y + j] * filtro[i, j]
        # Asegurarse de que el valor esté en el rango [0, 255]
        valor = int(max(0, min(suma, 255)))
        imagen_filt.putpixel((x, y), valor)

# Mostrar las imágenes original y filtrada
imagen_fil = Image.new('L', (width, height))
for x in range(width):
   for y in range(height):
      imagen_fil.putpixel((x,y),(imagen.getpixel((x,y))-imagen_filt.getpixel((x,y))))

imagen.show()
imagen_filt.show()
imagen_fil.show()
