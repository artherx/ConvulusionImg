import lib as lb
from PIL import Image
import os


imagen = Image.open('assets\img\chess.jpg')

# Convertir a escala de grises
width, height = imagen.size
imagen = imagen.convert('L')
if width>= 1000 or height >= 1000:
    imagen = imagen.resize((width//8,height//8))

a=1
imagen.show()
while a==1:
    nombre = input("ingresa:\n1 para filtro promedio\n2 para filtro gaussian\n3 para filtro readre\n4 para filtro shapen\n5 para filtro roberts\n6 para filtro prewitt\n7 para filtro sobel\nsi queires salir, escribe salir\n")
    print("se ingrso: ", nombre)
    if nombre=="1":
        tam = input("ingresa 3, 5, 9 para hacer una mascara de esos tamaños 3x3, 5x5 o 9x9: ")
        if tam.isdigit():
            tam = int(tam)
            if tam == 3:
                filtro_promedio=lb.convo(imagen,lb.filt_prome(tam),lb.img_central(imagen,lb.filt_prome(tam))).show()
                print("se añadio el filtro")
            if tam == 5:
                filtro_promedio=lb.convo(imagen,lb.filt_prome(tam),lb.img_central(imagen,lb.filt_prome(tam))).show()
                print("se añadio el filtro")
            if tam == 9:
                filtro_promedio=lb.convo(imagen,lb.filt_prome(tam),lb.img_central(imagen,lb.filt_prome(tam))).show()
                print("se añadio el filtro")
            else:
                print("Regresaras al inicio, ya que ingesaste valores no existentes: ")
        else:
            print("Regresaras al inicio, ya que no ingesaste números")
    if nombre == "2":
        sigma = input("ingresa el valor de sigma para el filtro de 0 a 1 ")
        sigma = float(sigma)
        if sigma<=1 and sigma>=0:
            tam = input("ingresa 3, 5, 9 para hacer una mascara de esos tamaños 3x3, 5x5 o 9x9: ")
            if tam.isdigit():
                tam = int(tam)
                if tam == 3:
                    filtro_gaussiano=lb.convo(imagen,lb.filt_gaussian(tam,sigma),lb.img_central(imagen,lb.filt_prome(tam))).show()
                    print("se añadio el filtro")
                if tam == 5:
                    filtro_gaussiano=lb.convo(imagen,lb.filt_prome(tam),lb.img_central(imagen,lb.filt_prome(tam))).show()
                    print("se añadio el filtro")
                if tam == 9:
                    filtro_gaussiano=lb.convo(imagen,lb.filt_prome(tam),lb.img_central(imagen,lb.filt_prome(tam))).show()
                    print("se añadio el filtro")
                else:
                    print("Regresaras al inicio, ya que ingesaste valores no existentes: ")
            else:
                print("Regresaras al inicio, ya que no ingesaste números")
        else:
            print("Regresaras al inicio, ya que no ingesaste números")
    if nombre == "3":
        filtro_redre = lb.convo(imagen,lb.filtro_redre,lb.img_central(imagen,lb.filtro_redre)).show()
        print("se añadio el filtro")
    if nombre == "4":
        filtro_shapen = lb.convo(imagen,lb.filtro_shapen,lb.img_central(imagen,lb.filtro_shapen)).show()
        print("se añadio el filtro")
    if nombre == "5":
        filtro_ruberts = lb.convo(imagen,lb.filtro_roberts,lb.img_central(imagen,lb.filtro_roberts)).show()
        print("se añadio el filtro")
    if nombre == "6":
        filtro_solber = lb.filtro_solber(imagen).show()
        print("se añadio el filtro")
    if nombre == "7":
        filtro_ruberts = lb.prewitt(imagen).show()
        print("se añadio el filtro")
    if nombre == "8":
        lb.conteo_obj_4N(imagen).show()
    if nombre == "9":
        lb.filtro_mediana(imagen).show()
    if nombre == "salir":
        os.system("cls")
        break
    else:
        print("lo sentimos, no ingreaste un valor exixtente")
    #os.system("cls")




