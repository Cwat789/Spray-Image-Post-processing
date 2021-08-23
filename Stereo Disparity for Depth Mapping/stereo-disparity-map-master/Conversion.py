import cv2
import numpy as np

img1 = cv2.imread('IN\holo_o11_r22_d1346726_2.tif')

img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)


res1 = img1.copy()
res2 = img1.copy()

for i in range(len(img1)):
        for j in range(len(img1[i])):
                
                if ((len(img1)/2) >= i):
                    res1[i,j] = img1[i,j];
                    res2[i,j] = 0;
                else:
                    res1[i,j] = 0;
                    res2[i,j] = img1[i,j];


cv2.imshow("result 1", res1)
cv2.imshow("result 2", res2)

cv2.imwrite("OUT\split_img1.tif",res1)
cv2.imwrite("OUT\split_img2.tif",res2)

#closes windows if space bar is pressed
cv2.waitKey(0)
cv2.destroyAllWindows()



