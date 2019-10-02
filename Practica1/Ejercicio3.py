import cv2
import numpy as np

img = cv2.imread("messi.jpg", 0) #el flag 0 para que salga en escala de grises
img2 = cv2.imread("playa.jpg", 0)

cv2.imshow("Messi en escala de grises", img)
cv2.imshow("Playa en escala de grises ", img2)

print(img.shape) #603x980
print(img2.shape) #678x1200

img2 = cv2.resize(img2,(980,603)) #redimensiono la imagen 2 , y la pongo mas pequeña para poder realizar la suma con la img1
img = img/2 #divido/2 para coger la mitad de escala de grises de los pixeles con la img2 , para sumarlas y que no pase de 255
img2 = img2/2
imgFinal = np.add(img,img2) #suma de las matrices de las imágenes
imgFinal = imgFinal.astype(np.uint8)
print(imgFinal)#comprobamos que no se pasa de 255
cv2.imshow("Superposición",imgFinal) #superposicion de las imágenes
cv2.waitKey(0)

