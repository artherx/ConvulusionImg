
from PIL import Image
from scipy.fft import dctn, idctn
import numpy as np
import os

CPU=os.cpu_count()
matriz_quantizacion = np.array([[89,  72,  58,  72,  95, 114, 131, 137],
                               [72,  62,  51,  60,  81, 104, 126, 130],
                               [58,  51,  46,  56,  76,  98, 119, 124],
                               [72,  60,  56,  68,  87, 103, 121, 128],
                               [95,  81,  76,  87, 105, 125, 138, 145],
                               [114, 104,  98, 103, 125, 145, 161, 169],
                               [131, 126, 119, 121, 138, 161, 180, 192],
                               [137, 130, 124, 128, 145, 169, 192, 210]])

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
        subdivisiones[i] = dctn(subdivisiones[i])
    return subdivisiones
def aplicar_idctn(subdivisiones):
    for i in range(len(subdivisiones)):
        subdivisiones[i] = np.round(idctn(subdivisiones[i]))
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
imagen = Image.open('assets\img\Selfie.jpg')# Ejemplo de imagen generada aleatoriamente, reemplazar con la imagen deseada

imagen.show()
imagen = np.array(imagen)
original_MB = os.path.getsize("assets\img\WhatsApp Image 2023-03-20 at 9.05.16 PM.jpeg") / 1024**2

# Paso 1: Subdividir la imagen en matrices de 8x8
subdivisiones = subdividir_imagen(imagen)

# Paso 2: Restar cada pixel por 128
# Paso 3: Aplicar la transformada discreta de coseno (DCT) en cada subdivisión
subdivisiones = aplicar_dct(subdivisiones)

# Paso 4: Dividir la subdivisión con la matriz de cuantización estándar

subdivisiones = dividir_con_matriz_quantizacion(subdivisiones, matriz_quantizacion)
baja =combinar_subdivisiones(subdivisiones, imagen)
imgSub = Image.fromarray(baja).convert('L')
imgSub.save('assets\img\WCompre.jpeg')
compre_MB = os.path.getsize("assets\img\WCompre.jpeg") / 1024**2
imgSub.show()

#vuelta al mundo
subdivisiones = multiplicar_con_matriz_quantizacion(subdivisiones, matriz_quantizacion)
subdivisiones = aplicar_idctn(subdivisiones)


# Paso 5: Combinar las subdivisiones en una matriz del mismo tamaño que la imagen original
subdivisiones =combinar_subdivisiones(subdivisiones, imagen)
#calculo de error cuadratico medio

#tasaCompre = imagen.nbytes / subdivisiones.nbytes
tasaCompre = imagen.nbytes / baja.nbytes
diferencia = (imagen - baja)**2
mse = np.mean(diferencia)
print('Error cuadratico',mse)
print('Tasa de compresion original vs descomprimida ', original_MB)
tasaCompre = (imagen.nbytes/(1024**2)) / (subdivisiones.nbytes/(1024**2))
print('Tasa de compresion original vs comprimida ', compre_MB, " ", (baja.nbytes/(1024**2)))
imgSub = Image.fromarray(subdivisiones).convert('L')
imgSub.save('assets\img\WDesco.jpeg')
imgSub.show()

# Las subdivisiones comprimidas están ahora en forma de matriz y se pueden procesar o guardar según sea necesario