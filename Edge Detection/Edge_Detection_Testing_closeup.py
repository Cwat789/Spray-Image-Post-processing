import cv2
import numpy as np

#img = cv2.imread('Test1/background_detection1.tif')
img = cv2.imread('closeup.png')

medimage = cv2.medianBlur(img,19)
edge = cv2.Canny(medimage,10,30)

#dialites lines for visability
kernel = np.ones((2,2),np.uint8) #affects size of line
edge = cv2.dilate(edge,kernel,iterations =1)
medimage[edge ==255]=0

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


newimage = cv2.addWeighted(edge,0.3,img,0.7,0)

cv2.imshow("edge detection", newimage)

cv2.imwrite("closeup edge detection1.png",edge)

cv2.waitKey(0)
cv2.destroyAllWindows()
 
