from scan import scan
import cv2
import numpy as np

scanned_img = scan('C:/Users/KIIT/Desktop/Bubble sheet choice scanner/test.png')
cv2.imshow("scanned image",scanned_img)
thresh =150

img_gray = cv2.cvtColor(scanned_img,cv2.COLOR_BGR2GRAY)
ret,thresh_img = cv2.threshold(img_gray, thresh, 255, cv2.THRESH_BINARY)
circles = cv2.HoughCircles(thresh_img, cv2.HOUGH_GRADIENT, 1.2, 100)
'''
for (x, y, r) in circles:
    cv2.circle(output, (x, y), r, (0, 255, 0), 4)
'''



cv2.imshow("threshold image",thresh_img)




cv2.waitKey(0)
cv2.destroyAllWindows()