import cv2


file_name = "../image/car.jpg"
image = cv2.imread(file_name)

window_name = "output"

cv2.imshow(window_name, image)

cv2.waitKey(0)

