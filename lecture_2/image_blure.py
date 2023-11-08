import cv2

image_path: str = "../image/lambo.png"

image = cv2.imread(image_path)
gaussian_size = (17, 17)
sigma_value = 0
image_blured = cv2.GaussianBlur(image, gaussian_size, sigma_value)

window_name = "original"
window_name_2 = "blured"
cv2.imshow(window_name, image)
cv2.imshow(window_name_2, image_blured)

cv2.waitKey(0)

