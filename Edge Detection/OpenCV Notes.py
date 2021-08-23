####weighted addition of two images

newimage = cv2.addWeighted(img1,0.7,img2,0.3,0) #last value is "gamma correction"
#Can use weighted subtraction by using negative numbers for weights


#####Median Bluring: "EDGE PRESERVING FILTER"

medimage = cv2.medianBlur(img1,29)

#medianBlur(src, ksize[, dst])


#####Canny EDGE DETECTION and dilation

edge = cv2.Canny(medimage,10,150)
kernel = np.ones((5,5),np.uint8)
edge = cv2.dilate(edge,kernel,iterations =1)
medimage[edge ==255]=0

#####look into "non local means filtering"


#####high pass edge detection
#laplacian filter
highimage = cv2.Laplacian(img,cv2.CV_64F)

#sobel filter (can be in x or y direction)-replace x w/1 and y w/0 for x

x=1
y=0
highimage2 = cv2.Sobel(img,cv2.CV_64F,x,y,ksize=5)
#NOTE X AND Y DIR WILL YIELD DIFFERENT RESULTS

#Canny edge detection (More complex than derivative) -theory on opencv website
highimage3 = cv2.Canny(img,100,200) #100 and 200 are threshhold values
