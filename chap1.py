import cv2
print("cv2 imported")

img = cv2.imread("Resources/Screenshot 2021-02-21 at 11.47.18.png")

cv2.imshow("Output",img)

cv2.waitKey(0)