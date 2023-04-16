
from PIL import Image
from scipy.fft import dctn, idctn
import numpy as np

# Paso 1: Subdividir la imagen en matrices de 8x8
def subdividir_imagen(imagen):
    columnas, filas= imagen.shape
    subdivisiones = []
    for i in range(0, columnas, 8):
        for j in range(0, filas, 8):
            subdivision = imagen[i:i+8, j:j+8]
            subdivisiones.append(subdivision)
    return subdivisiones

# Paso 2: Restar cada pixel por 128
def restar_128(subdivisiones):
    for i in range(len(subdivisiones)):
        subdivisiones[i] = subdivisiones[i] - 128
    return subdivisiones
def suma_128(subdivisiones):
    for i in range(len(subdivisiones)):
        subdivisiones[i] = subdivisiones[i] + 128
    return subdivisiones

# Paso 3: Aplicar la transformada discreta de coseno (DCT) en cada subdivisión
def aplicar_dct(subdivisiones):
    for i in range(len(subdivisiones)):
        subdivisiones[i] = dctn(subdivisiones[i], norm='ortho')
    return subdivisiones
def aplicar_idctn(subdivisiones):
    for i in range(len(subdivisiones)):
        subdivisiones[i] = idctn(subdivisiones[i], norm='ortho')
    return subdivisiones

# Paso 4: Dividir la subdivisión con la matriz de cuantización estándar
def dividir_con_matriz_quantizacion(subdivisiones, matriz_quantizacion):
    for i in range(len(subdivisiones)):
        subdivisiones[i] = np.round(subdivisiones[i] / matriz_quantizacion)
    return subdivisiones
def multiplicar_con_matriz_quantizacion(subdivisiones, matriz_quantizacion):
    for i in range(len(subdivisiones)):
        subdivisiones[i] = np.round(subdivisiones[i] * matriz_quantizacion)
    return subdivisiones

# Paso 5: Combinar las subdivisiones en una matriz del mismo tamaño que la imagen original
def combinar_subdivisiones(subdivisiones, forma_original):
    columnas , filas = forma_original.shape
    imagen_comprimida = np.zeros((columnas,filas))
    idx = 0
    for i in range(0, columnas, 8):
        for j in range(0, filas, 8):
            imagen_comprimida[i:i+8, j:j+8] = subdivisiones[idx]
            idx += 1
    return imagen_comprimida

# Cargar la imagen
imagen = Image.open('assets\img\WhatsApp Image 2023-03-20 at 9.05.16 PM.jpeg').convert('L')  # Ejemplo de imagen generada aleatoriamente, reemplazar con la imagen deseada
imagen.show()
imagen = np.array(imagen)

# Paso 1: Subdividir la imagen en matrices de 8x8
subdivisiones = subdividir_imagen(imagen)

# Paso 2: Restar cada pixel por 128
subdivisiones = restar_128(subdivisiones)

# Paso 3: Aplicar la transformada discreta de coseno (DCT) en cada subdivisión
subdivisiones = aplicar_dct(subdivisiones)

# Paso 4: Dividir la subdivisión con la matriz de cuantización estándar
matriz_quantizacion = np.array([[16, 11, 10, 16, 24, 40, 51, 61],
                               [12, 12, 14, 19, 26, 58, 60, 55],
                               [14, 13, 16, 24, 40, 57, 69, 56],
                               [14, 17, 22, 29, 51, 87, 80, 62],
                               [18, 22, 37, 56, 68, 109, 103, 77],
                               [24, 35, 55, 64, 81, 104, 113, 92],
                               [49, 64, 78, 87, 103, 121, 120, 101],
                               [72, 92, 95, 98, 112, 100, 103, 99]])

subdivisiones = dividir_con_matriz_quantizacion(subdivisiones, matriz_quantizacion)

#vuelta al mundo
subdivisiones = multiplicar_con_matriz_quantizacion(subdivisiones, matriz_quantizacion)
subdivisiones = aplicar_idctn(subdivisiones)
subdivisiones = suma_128(subdivisiones)

# Paso 5: Combinar las subdivisiones en una matriz del mismo tamaño que la imagen original
subdivisiones =combinar_subdivisiones(subdivisiones, imagen)

imgSub = Image.fromarray(subdivisiones)
imgSub.show()

# Las subdivisiones comprimidas están ahora en forma de matriz y se pueden procesar o guardar según sea necesario