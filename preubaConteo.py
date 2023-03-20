import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from skimage import filters

# Cargar la imagen
imagen = Image.open('assets\img\ImgRes\IMG_20230319_201515.jpg')

# Convertir a escala de grises
imagen = imagen.convert('L')

# Tamaño de la imagen
width, height = imagen.size

# Filtro promedio 3x3
kernel = 9
filtro = np.ones((kernel, kernel)) / kernel**2

#valores = np.array([[-1,-1,-1],
 #                   [-1, 8,-1],
  #                  [-1,-1,-1]])

#filtro[:3, :3] = valores

#filtro[:3,:3] = [[-1,-1,-1],
#                 [-1,8,-1],
#                 [-1,-1,-1]]

# Crear una matriz de ceros con borde de tamaño del filtro
borde = filtro.shape[0] // 2
matriz = np.zeros((width + 2 * borde, height + 2 * borde))

# Rellenar la matriz con los valores de la imagen
for x in range(width):
    for y in range(height):
        matriz[x + borde, y + borde] = imagen.getpixel((x, y))

# Aplicar el filtro a cada píxel de la imagen
imagen_filt = Image.new('L', (width, height))
imagen_umb = Image.new('L', (width, height))
for x in range(width):
    for y in range(height):
        suma = 0
        for i in range(filtro.shape[0]):
            for j in range(filtro.shape[1]):
                suma += matriz[x + i, y + j] * filtro[i, j]
        # Asegurarse de que el valor esté en el rango [0, 255]
        valor = int(max(0, min(suma, 255)))
        imagen_umb.putpixel((x, y), valor)
        if imagen_umb.getpixel((x,y)) > 120:
            imagen_umb.putpixel((x,y),(0))
        else:
            imagen_umb.putpixel((x,y),(255))
        imagen_filt.putpixel((x, y), valor)

# Mostrar las imágenes original y filtrada
imagen_fil = Image.new('L', (width, height))
for x in range(width):
   for y in range(height):
      imagen_fil.putpixel((x,y),(imagen.getpixel((x,y))-imagen_filt.getpixel((x,y))))

#for x in range(width):
#   for y in range(height):
 #       if imagen_filt.getpixel((x,y)) > 120:
  #          imagen_filt.putpixel((x,y),(0))
   #     else:
    #        imagen_filt.putpixel((x,y),(255))

# Calcular el umbral
#imagen_fil_array = np.array(imagen_filt)
#umbral = filters.threshold_otsu(imagen_fil_array)

# Contar el número de objetos
#num_objetos = 0
#for i in range(imagen_fil_array.shape[0]):
 #   for j in range(imagen_fil_array.shape[1]):
  #      if imagen_fil_array[i,j] < umbral:
   #         num_objetos += 1

#print("Número de objetos encontrados:", num_objetos)

imagen.show()
imagen_filt.show()
imagen_umb.show()
imagen_fil.show()




