import cv2

img = cv2.imread('solar-system.jpg')

cv2.putText(img, 'Sun', (20,300),fontFace=cv2.FONT_HERSHEY_PLAIN,fontScale=2, color=(255,255,255))
cv2.imshow('planets',img)
cv2.waitKey(0)


