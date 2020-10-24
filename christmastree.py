import cv2  # Not actually necessary if you just want to create an image.
import numpy as np
import random
 
height = 1000
width = 1000
img = np.zeros((height,width,3), np.uint8)
img[::] = (255,255,255)      # (B, G, R)
# img[:,width//2:width] = (0,255,0)
# img[10,20,:] = (0,0,0) malowanie jednego piksela
odw = ((-0.67,-0.02,0,-0.18,0.81,10),(0.4,0.4,0,-0.1,0.4,0),(-0.4,-0.4,0,-0.1,0.4,0),(-0.1,0,0,0.44,0.44,-2))

point = [[0,0]]
# print(point[-1][-1])
def next(point,odw):
    ch_list = random.choices( odw, k = 1 )
    ch_list = ch_list[0]
    # print(ch_list)
    x_n = round(ch_list[0]*point[-1][-2] + ch_list[1]*point[-1][-1] + ch_list[2],2)
    y_n = round(ch_list[3]*point[-1][-2] + ch_list[4]*point[-1][-1] + ch_list[5],2)
    point.extend([[x_n,y_n]])

for i in range(0,100000):
    next(point,odw)

for val in point:
    img[int(10*val[0]+int(height/2)),int(10*val[1]+int(width/5)),:] = (0,0,0)

# print(point)
img1 = cv2.rotate(img, cv2.cv2.ROTATE_90_COUNTERCLOCKWISE) 

cv2.imshow('fractal',img1)
# print(point)
k = cv2.waitKey(0)
if k == 27 or k == ord('c'):         # wait for ESC key to exit
    cv2.destroyAllWindows()
