import cv2 as cv
import matplotlib.pyplot as plt
import math
import numpy as np
            ######## PARA QUE FUNCIONEN LAS FUNCIONES HAY QUE DESCOMENTAR LA LÍNEA DESEADA AL FINAL DEL CODIGO Y VICEVERSA. ########
img = cv.imread("low.jpg", 0)
filas, columnas = img.shape  # dimensiones de la imagen
img3 = np.zeros((filas, columnas),dtype=np.uint8)  # devuelve un array de la forma dada con 0's y lo convierte al tipo uint8 para operar con enteros e iremos añadiendo los elementos
img4 = np.zeros((filas, columnas),dtype=np.uint8)

#A)
def histograma():
    img2 = cv.calcHist([img], [0], None, [256], [0, 256])  # calcula histograma
    plt.xlabel('Gray Level') #editamos etiquetas para los ejes x e y
    plt.ylabel('Pixel Count')
    plt.plot(img2)  # monto la gráfica
    plt.show() #la mostramos
    cv.imshow("hist",img)

#B)
def transfLog():
   r = np.max(img)  # L-1
   c = r / math.log(1 + r) #calculamos constante C
   print(c)
   for x in range(filas):
      for y in range(columnas):  # para cada pixel
          img3[x, y] = c * math.log(1 + img[x, y]) #aplicamos la transformacion T(r) = c*log(1+r) donde r es el valor en la escala de grises de cada pixel
   cv.imshow("log",img3)


def transPotencia(n):
   r = np.max(img) #L-1
   c = r/pow(r,n) #cálculo de la constance C = r/ r^n donde n es un número que le pasaremos por parámetro
   print(c)
   for x in range(filas):
       for y in range(columnas):
           img4[x,y] = c*(pow(img[x,y],n)) #aplicamos la transformación
   cv.imshow("potencia",img4)
   print(img4)

#C)
def ecualiza():
    cv.imshow("ORIGINAL",img)
    img5=cv.equalizeHist(img) #aplicamos la función para equalizar la imágen
    cv.imshow("EQUALIZADA",img5)
    img2=img/2 #divido/2 para coger la mitad de escala de grises de los pixeles con la img2 , para sumarlas y que no pase de 255
    img5=img5/2
    imgDif = img2-img5 #hacemos la diferencia de la imagen original en escala de grises - la equalizada
    imgDif = imgDif.astype(np.uint8) #transformamos a uint8 para trabajar con enteros

    #MOSTRAMOS MATRICES
    print("ORIGINAL\n")
    print(img2)
    print("\n\n")
    print("MODIFICADA\n")
    print(img5)
    print("\n\n")
    print("DIF\n")
    print(imgDif)

    cv.imshow("DIFERENCIA",imgDif)

                ######## PARA QUE FUNCIONEN LAS FUNCIONES HAY QUE DESCOMENTAR LA LÍNEA DESEADA AL FINAL DEL CODIGO Y VICEVERSA. ########
histograma()
#transfLog()
#transPotencia(1/4)
#transPotencia(1/2)
#transPotencia(2)
#transPotencia(3)
#ecualiza()

