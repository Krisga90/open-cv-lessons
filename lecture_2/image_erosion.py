import cv2
import numpy as np

image_path: str = "../image/documentscanner2.jpg"
# image_path: str = "../image/car.jpg"
image = cv2.imread(image_path)

matrix_shape = (3, 3)
kernel = np.ones(matrix_shape, np.uint8)

# threshold values
t_lower = 100
t_higher = 120


image_edge = cv2.Canny(image, t_lower, t_higher)
image_dialation = cv2.dilate(image_edge, kernel, iterations=1)

image_erosion = cv2.erode(image_edge, kernel, iterations=1)

image_open = cv2.dilate(image_erosion, kernel, iterations=1)
image_close = cv2.erode(image_dialation, kernel, iterations=1)

window_name = "original"
window_name_2 = "edge"
window_name_3 = "dilate"
window_name_4 = "erode"
window_name_5 = "open"
window_name_6 = "close"

cv2.imshow(window_name, image)
cv2.imshow(window_name_2, image_edge)
cv2.imshow(window_name_3, image_dialation)
cv2.imshow(window_name_4, image_erosion)
cv2.imshow(window_name_5, image_open)
cv2.imshow(window_name_6, image_close)


cv2.waitKey(0)

