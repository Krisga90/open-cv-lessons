import cv2

# image_path: str = "../image/documentscanner2.jpg"
image_path: str = "../image/car.jpg"
image = cv2.imread(image_path)

# threshold values
t_lower = 100
t_higher = 120


image_edge = cv2.Canny(image, t_lower, t_higher)

window_name = "original"
window_name_2 = "edge"
cv2.imshow(window_name, image)
cv2.imshow(window_name_2, image_edge)

cv2.waitKey(0)

