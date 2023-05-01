import lib as lb
from PIL import Image
import numpy as np

imagen = Image.open('WhatsApp Image 2023-03-20 at 9.05.16 PM.jpeg')

imagen = imagen.convert('L')
imagen_array = np.array(imagen)
imagen_array = lb.umbra(imagen_array)
imagen_array=lb.prewitt(imagen_array)
print(lb.conteo_obj_4N(imagen_array))
imagen_pil = Image.fromarray(imagen_array)
imagen_pil.show()
