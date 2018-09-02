import cv2
from os import path
width=28
height=28
dim=(width,height)

for i in range (26541):
    loc='/home/surgan/Desktop/DL-Models/CNN/Test_Age/Test/'+str(i)+'.jpg'
    if (path.exists(loc)):
        img = cv2.imread(loc, cv2.IMREAD_UNCHANGED)
        resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
        cv2.imwrite(loc,resized)
 
    





