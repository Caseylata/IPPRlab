import cv2
import numpy as np

print("HELLO ile 2")
img = cv2.imread("abc.jpg")
# median=cv2.medianBlur(img,5)
# gauss = cv2.GaussianBlur(img,(5,5),0)
laplacian=cv2.Laplacian(img,cv2.CV_16S,3)
images = np.concatenate((img,laplacian), axis=1)


cv2.imshow('img', laplacian)
cv2.waitKey(0)
cv2.destroyAllWindows
