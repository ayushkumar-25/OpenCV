import cv2
# print("Imported successfully")

img = cv2.imread("resources/Ayush.jpg")
cv2.imshow("Output", img)
cv2.waitKey(0)