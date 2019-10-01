import cv2
import numpy as np

#Apartado 2
#a)Separa los tres canales RGB que componen la imagen y visualiza cada uno por separado como imágenes en escala de grises.
img = cv2.imread("mariposa-azul.jpg", 1)

b,g,r = cv2.split(img)
cv2.imshow("r", r)
cv2.waitKey(0)
cv2.imshow("g", g)
cv2.waitKey(0)
cv2.imshow("b", b)
cv2.waitKey(0)


#b)Pasa la imagen a color a escala de grises de dos formas: usando la fórmula de Y en el modelo YIQ y la de I en el modelo HSI
i = 1/3*(r+g+b)
i=i.astype(np.uint8)
print(i)
cv2.imshow("i", i)
cv2.waitKey(0)

y = 0.299*r+0.587*g+0.144*b
y=y.astype(np.uint8)
print(y)
cv2.imshow("y", y)
cv2.waitKey(0)