import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from scipy.signal import convolve2d

# Cargar la imagen
imagen = Image.open('assets\img\ImgRes\IMG_20230319_201515.jpg')

# Convertir a escala de grises
imagen = imagen.convert('L')

# Tamaño de la imagen
width, height = imagen.size

# Filtro promedio 3x3
kernel = 3
filtro = np.ones((kernel, kernel)) / kernel**2

# Aplicar el filtro
imagen_arr = np.array(imagen)
imagen_filt_arr = convolve2d(imagen_arr, filtro, mode='same')
imagen_filt = Image.fromarray(imagen_filt_arr.astype(np.uint8))

# Calcular la diferencia entre la imagen original y la filtrada
imagen_fil_arr = imagen_arr - imagen_filt_arr
imagen_fil = Image.fromarray(imagen_fil_arr.astype(np.uint8))



# Mostrar las imágenes original, filtrada y la diferencia
imagen_filt.show()
fig, axs = plt.subplots(1, 3)
axs[0].imshow(imagen, cmap='gray')
axs[0].set_title('Original')
axs[1].imshow(imagen_filt, cmap='gray')
axs[1].set_title('Filtrada')
axs[2].imshow(imagen_fil, cmap='gray')
axs[2].set_title('Diferencia')
for ax in axs:
    ax.axis('off')
plt.show()