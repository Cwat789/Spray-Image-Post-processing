import cv2
import numpy as np

#img = cv2.imread('Test1/background_detection1.tif')
img = cv2.imread('Spray1.png')

medimage = cv2.medianBlur(img,5)
edge = cv2.Canny(medimage,90,100)
#kernel = np.ones((5,5),np.uint8)
#edge = cv2.dilate(edge,kernel,iterations =1)
#medimage[edge ==255]=0



cv2.imshow("Large edge detection2.png", edge)

cv2.imwrite("entire edge detection2.png",edge)

cv2.waitKey(0)
cv2.destroyAllWindows()
 
