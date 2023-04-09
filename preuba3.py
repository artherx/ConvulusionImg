import lib as lb
from PIL import Image
import numpy as np
import time
import os


imagen = Image.open('assets\img\chess.jpg')
imagen1 = Image.open('assets\img\WhatsApp Image 2023-03-20 at 9.05.16 PM.jpeg')

# Convertir a escala de grises
width, height = imagen.size
width, height = imagen1.size
imagen = imagen.convert('L')
imagen1 = imagen1.convert('L')
imagenAr = np.array(imagen1)
imagen_array = np.array(imagen)
anch, alto = imagen.size
a=1

imgMN = lb.umbra(imagen_array)
imgPil = Image.fromarray(imgMN)
imgPil.show()
while a==1:
    nombre = input("ingresa:\n1 para filtro promedio\n2 para filtro gaussian\n3 para filtro readre\n4 para filtro shapen\n5 para filtro roberts\n6 para filtro prewitt\n7 para filtro sobel\n8 contar objetos 4N\n9 contar objetos 8N\n10 contar objetos 4D\nsi queires salir, escribe salir\n")
    print("se ingrso: ", nombre)
    if nombre=="1":
        tam = input("ingresa 3, 5, 9 para hacer una mascara de esos tamaños 3x3, 5x5 o 9x9: ")
        if tam.isdigit():
            tam = int(tam)
            if tam == 3:
                filtro_promedio=lb.convo(imagenAr,lb.filt_prome(tam),lb.img_central(imagenAr,lb.filt_prome(tam)))
                imgPil = Image.fromarray(filtro_promedio)
                imgPil.show()
                print("se añadio el filtro")
            if tam == 5:
                filtro_promedio=lb.convo(imagenAr,lb.filt_prome(tam),lb.img_central(imagenAr,lb.filt_prome(tam)))
                imgPil = Image.fromarray(filtro_promedio)
                imgPil.show()
                print("se añadio el filtro")
            if tam == 9:
                filtro_promedio=lb.convo(imagenAr,lb.filt_prome(tam),lb.img_central(imagenAr,lb.filt_prome(tam)))
                imgPil = Image.fromarray(filtro_promedio)
                imgPil.show()
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
                    filtro_gaussiano=lb.convo(imagenAr,lb.filt_gaussian(tam,sigma),lb.img_central(imagenAr,lb.filt_prome(tam)))
                    imgPil = Image.fromarray(filtro_gaussiano)
                    imgPil.show()
                    print("se añadio el filtro")
                if tam == 5:
                    filtro_gaussiano=lb.convo(imagenAr,lb.filt_prome(tam),lb.img_central(imagenAr,lb.filt_prome(tam)))
                    imgPil = Image.fromarray(filtro_gaussiano)
                    imgPil.show()
                    print("se añadio el filtro")
                if tam == 9:
                    filtro_gaussiano=lb.convo(imagenAr,lb.filt_prome(tam),lb.img_central(imagenAr,lb.filt_prome(tam)))
                    imgPil = Image.fromarray(filtro_gaussiano)
                    imgPil.show()
                    print("se añadio el filtro")
                else:
                    print("Regresaras al inicio, ya que ingesaste valores no existentes: ")
            else:
                print("Regresaras al inicio, ya que no ingesaste números")
        else:
            print("Regresaras al inicio, ya que no ingesaste números")
    if nombre == "3":
        filtro_redre = lb.convo(imagenAr,lb.filtro_redre,lb.img_central(imagenAr,lb.filtro_redre))
        imgPil = Image.fromarray(filtro_redre)
        imgPil.show()
        print("se añadio el filtro")
    if nombre == "4":
        filtro_shapen = lb.convo(imagenAr,lb.filtro_shapen,lb.img_central(imagenAr,lb.filtro_shapen))
        imgPil = Image.fromarray(filtro_shapen)
        imgPil.show()
        print("se añadio el filtro")
    if nombre == "5":
        filtro_ruberts = lb.convo(imagenAr,lb.filtro_roberts,lb.img_central(imagenAr,lb.filtro_roberts))
        imgPil = Image.fromarray(filtro_ruberts)
        imgPil.show()
        print("se añadio el filtro")
    if nombre == "6":
        filtro_solber = lb.filtro_solber(imagenAr)
        imgPil = Image.fromarray(filtro_solber)
        imgPil.show()
        print("se añadio el filtro")
    if nombre == "7":
        filtro_ruberts = lb.prewitt(imagenAr)
        imgPil = Image.fromarray(filtro_ruberts)
        imgPil.show()
        print("se añadio el filtro")
    if nombre == "8":
        t1 = time.perf_counter_ns()
        imgM = lb.conteo_obj_4N(imgMN)
        # Rellenar la imagen con los valores de la matriz
        print(imgM)
        t2 = time.perf_counter_ns()
        print((t2-t1)/10**9)
    if nombre == "9":
        t1 = time.perf_counter_ns()
        imgM = lb.conteo_obj_8N(imgMN)
        # Rellenar la imagen con los valores de la matriz
        print(imgM)
        t2 = time.perf_counter_ns()
        print((t2-t1)/10**9)
    if nombre == '10':
        t1 = time.perf_counter_ns()
        imgM = lb.conteo_obj_4D(imgMN)
        # Rellenar la imagen con los valores de la matriz
        print(imgM)
        t2 = time.perf_counter_ns()
        print((t2-t1)/10**9)
    if nombre == "salir":
        os.system("cls")
        break
    else:
        print("lo sentimos, no ingreaste un valor exixtente")
    #os.system("cls")




