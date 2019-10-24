import cv2 as cv

img = cv.imread("Lenna.png", 0)
print(img)
print("\n\n")
cv.imshow("Lenna",img)
cv.waitKey(0)

ddepth = cv.CV_16S #Nuestra imagen es CV_8U por lo que definimos ddepth = CV_16S para evitar el desbordamiento , y por tanto pone algunos números en negativo
kernel_size = 5 # 16-bit signed integers ( -32768..32767 )
dst = cv.Laplacian(img, ddepth, ksize=kernel_size) #Los valores los pone negativos
print("Laplacian cv_16S")
print(dst)

abs_dst = cv.convertScaleAbs(dst) # Convierte la salida a CV_8U (0,255)
print("\n\nLaplacian uint8\n")
print(abs_dst)

cv.imshow("LennaLaplaciano",abs_dst)
cv.waitKey(0)