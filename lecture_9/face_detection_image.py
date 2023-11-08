
import cv2

file_name = "../image/face.png"
image = cv2.imread(file_name)


faceCascade = cv2.CascadeClassifier("../haarcascades/haarcascade_frontalface_default.xml")


gray_scale_frame = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

scale = 1.1
minimum_neighbours = 3
faces = faceCascade.detectMultiScale(gray_scale_frame, scale, minimum_neighbours)

for x, y, w, h in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 255, 0), 3)

cv2.imshow("photo", image)

cv2.waitKey(0)
