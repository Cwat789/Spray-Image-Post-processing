import cv2
import numpy as np

fg = cv2.imread('FG_256PSI.tif')
bg = cv2.imread('BG_256PSI.tif')


difference2 = fg.copy()

for i in range(len(fg)):
        for j in range(len(fg[i])):
                
                if ((int(bg[i,j,1])-int(fg[i,j,1])) >= 20):
                    difference2[i,j,:] = fg[i,j,:]
                


                
                else:
                        if (difference2[i,j,2]+30<=255):
                                difference2[i,j,2] = fg[i,j,2] +30;
                                difference2[i,j,0] = fg[i,j,0] +30;
                        else:
                                difference2[i,j,2]=225
                                difference2[i,j,0]=225
                                        
                        
                    
                    
                            
                            


cv2.imshow("difference 2", difference2)

cv2.imwrite("background_detection_256PSI_V2.tif",difference2)


#closes windows if space bar is pressed
cv2.waitKey(0)
cv2.destroyAllWindows()
