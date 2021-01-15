import cv2
import numpy as np
def accumulator(image,threshold_val):
    rows_in_image_matrix = image.shape[0]
    cols_in_image_matrix = image.shape[1]
    rmax = int(np.sqrt(rows_in_image_matrix**2+cols_in_image_matrix**2))
    beg = -rmax
    #setting up accumulator matrix
    num = 2*rmax+2
    acc = np.zeros(num*182).reshape(num,182)
    for i in range(1,num):
        acc[i][0] = beg
        beg = beg+1
    for j in range(1,182):
        acc[0][j]=j-1
    #we have finished setting up the accumulator matrix
    #now instead of for each pixel, we willl compare for only those where value=255
    #since only they form lines
    row_indices,col_indices = np.where(image==255)
    for k in range(0,len(row_indices)):
        x = col_indices[k]
        y = row_indices[k]
        for theta in range(0,181):
            theta_rad = theta*np.pi/180
            rho = int(x*np.cos(theta_rad)+y*np.sin(theta_rad))
            acc[rho+rmax+1][theta+1]+=1
    hough = []
    row_threshold,col_threshold = np.where(acc>=threshold_val)
    for z in range(0,len(row_threshold)):
        if col_threshold[z]!=0 and row_threshold[z]!=0:
            hough.append([row_threshold[z]-rmax-1,col_threshold[z]-1])
    return hough
x = cv2.imread('./soduku.jpg')
cv2.imshow('Original Image',x)
cv2.waitKey()
cv2.destroyAllWindows()
x_gray= cv2.cvtColor(x,cv2.COLOR_BGR2GRAY)
canny_edged = cv2.Canny(x_gray,70,100,apertureSize=3)
hough_lines = accumulator(canny_edged,200)
for points in hough_lines:
    rho = points[0]
    theta = points[1]
    a = np.cos(theta*np.pi/180)
    b = np.sin(theta*np.pi/180)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0+1000*(-b))
    y1 = int(y0+1000*(a))
    x2 = int(x0-1000*(-b))
    y2 = int(y0-1000*(a))
    cv2.line(x,(x1,y1),(x2,y2),(255,0,0),2)
cv2.imshow('Hough Lines', x)
cv2.waitKey()
cv2.destroyAllWindows()
