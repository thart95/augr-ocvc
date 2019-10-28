import cv2
import numpy as np

imageRequest = input("What image would you like to search for?")
windowTimeoutValue = input("Window time out (default 5 seconds): ")

if not imageRequest:
    imageRequest = "test.png"

if not windowTimeoutValue:
    windowTimeoutValue = 5000
else:
    windowTimeoutValue = int(windowTimeoutValue) * 1000

img1 = cv2.imread("./media/img/"+imageRequest)

cv2.imshow("Response", img1)
cv2.waitKey(windowTimeoutValue)
cv2.destroyAllWindows()
