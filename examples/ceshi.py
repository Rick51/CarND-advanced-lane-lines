import numpy as np
import cv2
img_size = [1280,720]
# Create a black image
img = np.zeros((512,512,3), np.uint8)

pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)

src = np.int32(
    [[(img_size[0] // 2) - 55, img_size[1] // 2 + 100],
    [((img_size[0] // 6) - 10), img_size[1]],
    [(img_size[0] * 5 // 6) + 60, img_size[1]],
    [(img_size[0] // 2 + 55), img_size[1] // 2 + 100]])
print('1',pts.shape)
print('2',src.shape)
pts = pts.reshape((-1,1,2))
print('3',pts.shape)
cv2.polylines(img,[pts],True,(0,255,255))


cv2.imshow('line',img)
cv2.waitKey()