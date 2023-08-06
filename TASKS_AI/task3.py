import cv2
import numpy as np
file__name = 'D:\TASKS_AI\cat.jpg'
####### Scalling #########
window_name = 'Scalling Image'
img = cv2.imread(file__name)
(height, width) = img.shape[:2]
res = cv2.resize(img, (int(width/2), int(height/2)),
                    interpolation=cv2.INTER_CUBIC)
cv2.imshow("source", img)
cv2.imshow(window_name, res)
cv2.waitKey(0)
###### Rotation #########
window_name = 'Rotation Image'
img = cv2.imread(file__name)
res = cv2.rotate(img, cv2.cv2.ROTATE_90_CLOCKWISE)

cv2.imshow(window_name, res)
cv2.waitKey(0)

###### Cut image ########
img = cv2.imread(file__name)
print(img.shape)
cropped_img = img[0:50, 0:50]
cv2.imshow("Original", img)
cv2.imshow("cropped", cropped_img)
cv2.waitKey(0)
