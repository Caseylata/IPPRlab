import cv2
import numpy as np

print("HELLO ile 2")
img = cv2.imread("saltnpepa.jpg")
median=cv2.medianBlur(img,5)
gauss = cv2.GaussianBlur(img,(5,5),0)
images = np.concatenate((img,median, gauss), axis=1)


cv2.imshow('img', images)
cv2.waitKey(0)
cv2.destroyAllWindows

