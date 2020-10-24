import numpy as np
import cv2
import random

height = 1000
width = 1000
img = np.zeros((height,width,3), np.uint8)
img[::] = (255,255,255)      # (B, G, R)

triangle = ( [266,500], [700,250], [700,750] )

# for val in triangle:
    # img[val[0],val[1],:] = (0,0,0)
x_f = random.randint(266, 700)
y_f = random.randint(250, 750)   
point = [[x_f,y_f ]]

def next(point, triangle):
   i = random.randint(0, 2)
   x_n = (point[-1][0]+triangle[i][0])/2
   y_n = (point[-1][1]+triangle[i][1])/2
   point.extend([[x_n,y_n]])

for val in range(0, 100000):
    next(point, triangle)

for val in point:
    img[int(val[0]),int(val[1]),:] = (0,0,0)

cv2.imshow('fractal',img)
# print(cv2.imwrite(r'F:\\zdjecia\fraktale\sierpinski.jpg', img))

k = cv2.waitKey(0)
if k == 27 or k == ord('c'):         # wait for ESC key to exit
    cv2.destroyAllWindows()
    
