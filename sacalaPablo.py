from PIL import Image
import numpy as np

# Cargar la imagen con PIL
img = Image.open("pablo.png")

# Convertir la imagen a una matriz NumPy
img_np = np.array(img)
print(img_np.shape)
mask = (img_np[:, :, 0] >= 215) & (img_np[:, :, 0] <= 255)
mask &= (img_np[:, :, 1] >= 215) & (img_np[:, :, 1] <= 255)
mask &= (img_np[:, :, 2] >= 0) & (img_np[:, :, 2] <= 150)
mask &= (img_np[:, :, 3] == 255)
coords = np.argwhere(mask)
print(coords.shape)

# Crear una matriz en negro
black = np.zeros_like(img_np)
print(black.shape)
# Copiar los píxeles amarillos a la matriz en negro
black[coords[:,0], coords[:,1], :] = img_np[coords[:,0], coords[:,1], :]

# Crear una nueva imagen con la matriz en negro
new_img = Image.fromarray(black)

# Mostrar la nueva imagen
new_img.show()