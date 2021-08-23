import cv2
import numpy as np



fg = cv2.imread('Test1\FG_Image_Test1.tif')
bg = cv2.imread('Test1\BG_Image_Test1.tif')



#Converting to grayscale
fg = cv2.cvtColor(fg, cv2.COLOR_BGR2GRAY)
bg = cv2.cvtColor(bg, cv2.COLOR_BGR2GRAY)

#Gaussian Blur
#bg = cv2.GaussianBlur(bg, (15, 15), 0)
#fg = cv2.GaussianBlur(fg, (15, 15), 0)

#Inverting Image
bg = cv2.bitwise_not(bg)
fg = cv2.bitwise_not(fg)


difference = cv2.absdiff(fg, bg)

#used to copy size of fg array, all values will change
difference2 = fg.copy()
#Computing difference, with negatives being zero



            
difference2 = cv2.bitwise_not(difference2)  #this is the output
difference = cv2.bitwise_not(difference)


#Subtracting absolute difference from background photo for new image
for i in range(len(fg)):
        for j in range(len(fg[i])):
                
                if ((-int(bg[i,j])+int(difference[i,j])) >= 0):
                    difference2[i,j] = -int(bg[i,j])+int(difference[i,j])
                else:
                    difference2[i,j] = 0

                    

#un inverting fg image for compairison
fg = cv2.bitwise_not(fg)

#Creates Bianary Value of image depending on grayscale threshhold
# Currently Removed
#_, fg = cv2.threshold(fg, 85, 255, cv2.THRESH_BINARY) 
#_, difference2 = cv2.threshold(difference2, 85, 255, cv2.THRESH_BINARY) 

#cv2.imshow("Background", bg)
cv2.imshow("Image w/ Object", fg)
cv2.imshow("difference", difference)

cv2.imshow("difference 2", difference2)

cv2.imwrite("difference3.tif",difference3)




# Consider adding gaussian filters such as bg = cv2.GaussianBlur(bg, (5, 5), 0)

#closes windows if space bar is pressed
cv2.waitKey(0)
cv2.destroyAllWindows()
