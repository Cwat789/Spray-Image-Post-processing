import cv2
import numpy as np

img = cv2.imread('Test1/FG_256PSI.tif')
#img = cv2.imread('closeup.png')

medimage = cv2.medianBlur(img,21) #21 is good value here, must be odd 
edge = cv2.Canny(medimage,10,25)

#dialites lines for visability
kernel = np.ones((2,2),np.uint8) #affects size of line
edge = cv2.dilate(edge,kernel,iterations =1)
medimage[edge ==255]=0


edge = cv2.cvtColor(edge, cv2.COLOR_GRAY2BGR)
for i in range(len(edge)):
        for j in range(len(edge[i])):
                edge[i,j,1] = 0
                edge[i,j,0] = 0



newimage = cv2.addWeighted(edge,0.3,img,0.85,0)

cv2.imshow("edge detection", newimage)

cv2.imwrite("256PSI Edge.png",newimage)

cv2.waitKey(0)
cv2.destroyAllWindows()
 
