import cv2

image_path: str = "../image/lambo.png"

image = cv2.imread(image_path)
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

window_name = "oryginal"
window_name_2 = "gray"
cv2.imshow(window_name, image)
cv2.imshow(window_name_2, image_gray)

cv2.waitKey(0)

