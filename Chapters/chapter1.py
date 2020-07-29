import cv2
# print("Imported successfully")

# to import image
'''img = cv2.imread("resources/Ayush.jpg")
cv2.imshow("Output", img)
cv2.waitKey(0) '''

# to import video
'''cap = cv2.VideoCapture("resources/test_video.mp4")
cap.set(3, 640)
cap.set(4, 480)
while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break'''

# to open web cam
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 100)
while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
