import sys
import cv2
from matplotlib import pyplot as plt
img=cv2.imread("C:\\Users\\Rohit\\Downloads\\abc.jpg",cv2.IMREAD_ANYCOLOR)
img_negative=255-img # each pixel lai subtract
print(img)
print(img_negative)

plt.hist(img.ravel(),256,[0,256]);plt.show()

dimension=img.shape
print("dimesion =",dimension)

while True:
    cv2.imshow("lenna",img)
    cv2.imshow("negative",img_negative)
    cv2.waitKey(0)
    sys.exit()

cv2.destroyAllWindows()