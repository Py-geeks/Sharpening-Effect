import cv2
import numpy as np

#reading imagae from file
img = cv2.imread("cat.png") #Add your png or jpg file here
#SHARPENING EFFECT
kernel_sharpening = np.array([[-1,-1,-1], 
                              [-1, 9,-1],
                              [-1,-1,-1]])
sharpened = cv2.filter2D(img,-1,kernel_sharpening)
#completion message
print('Image Sharpened.')

#comparing original vs resized
cv2.imshow('ORIGINAL',img)
cv2.imshow('SHARPEN',sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()
