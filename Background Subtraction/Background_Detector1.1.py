import cv2
import numpy as np

fg = cv2.imread('Test1\FG_Image_Test1.tif')
bg = cv2.imread('Test1\BG_Image_Test1.tif')



difference2 = fg.copy()

for i in range(len(fg)):
        for j in range(len(fg[i])):
                
                if ((int(bg[i,j,1])-int(fg[i,j,1])) >= 60):
                    difference2[i,j,1] = fg
                elif ((int(bg[i,j,1])-int(fg[i,j,1])) >= 30):
                    difference2[i,j,1] = 60

                
                else:
                    difference2[i,j,:] = 255


cv2.imshow("difference 2", difference2)
