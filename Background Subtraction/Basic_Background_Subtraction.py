import cv2
import numpy as np
import itertools


fg = cv2.imread('Test1\FG_Image_Test1.tif')
bg = cv2.imread('Test1\BG_Image_Test1.tif')



#Converting to grayscale
fg = cv2.cvtColor(fg, cv2.COLOR_BGR2GRAY)
bg = cv2.cvtColor(bg, cv2.COLOR_BGR2GRAY)

#Gaussian Blur
#bg = cv2.GaussianBlur(bg, (15, 15), 0)
#fg = cv2.GaussianBlur(fg, (15, 15), 0)

#Inverting Image
#bg = cv2.bitwise_not(bg)
#fg = cv2.bitwise_not(fg)


difference = cv2.absdiff(fg, bg)

#used to copy size of fg array, all values will change
difference2 = fg.copy()
#Computing difference, with negatives being zero
for i in range(len(fg)):
        for j in range(len(fg[i])):
                
                if ((int(bg[i,j])-int(fg[i,j])) >= 0):
                    difference2[i,j] = int(bg[i,j])-int(fg[i,j])
                else:
                    difference2[i,j] = 0


            


#Creates Bianary Value of image depending on grayscale threshhold
# Currently Removed
#_, difference = cv2.threshold(difference, 25, 255, cv2.THRESH_BINARY) 


cv2.imshow("Background", bg)
cv2.imshow("Image w/ Object", fg)
cv2.imshow("difference", difference)

cv2.imshow("difference 2", difference2)

cv2.imwrite("difference3.tif",difference2)




# Consider adding gaussian filters such as bg = cv2.GaussianBlur(bg, (5, 5), 0)

#closes windows if 0 is pressed
cv2.waitKey(0)
cv2.destroyAllWindows()
