import cv2
import numpy as np

fg = cv2.imread('FG_256PSI.tif')
bg = cv2.imread('BG_256PSI.tif')

fg = cv2.cvtColor(fg, cv2.COLOR_BGR2GRAY)
bg = cv2.cvtColor(bg, cv2.COLOR_BGR2GRAY)

difference2 = fg.copy()

pixelRange = 50

for i in range(len(fg)):
        for j in range(len(fg[i])):
                
                if ((int(bg[i,j])-int(fg[i,j])) >= pixelRange):
                    difference2[i,j] = fg[i,j]
                


                
                else:
                    difference2[i,j] = 255


cv2.imshow("difference 2", difference2)

cv2.imwrite("background_detection_256PSI.tif",difference2)


#closes windows if space bar is pressed
cv2.waitKey(0)
cv2.destroyAllWindows()
