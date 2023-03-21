import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import lib as lb


# Cargar la imagen
imagen = Image.open('assets\img\Resistencia.jpg')

# Convertir a escala de grises
imagen = imagen.convert('L')
# Tamaño de la imagen
width, height = imagen.size

# Filtro promedio 3x3
kernel = 3
filtro = np.ones((kernel, kernel)) / kernel**2

filtro_redre = np.array([[-1,-1,-1],
                  [-1, 8,-1],
                   [-1,-1,-1]])


filtro_shepen =np.array([[-1,-1,-1],
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
                suma += (matriz[x + i, y + j] * filtro[i, j])
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
