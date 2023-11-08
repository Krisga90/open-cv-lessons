
import cv2
import numpy as np

filename = "../image/shapes.png"
image = cv2.imread(filename)

image_grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# apply any edge detector

lower_threshold = 100
upper_threshold = 150
canny_edge = cv2.Canny(image_grayscale, lower_threshold, upper_threshold)

# find the contours
contours, hierarchy = cv2.findContours(canny_edge.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# find length of the contours

print(f"Length of the contours = {len(contours)}")


image_copy = image.copy()
for contour in contours:
    # draw cntours
    area = cv2.contourArea(contour)

    cv2.drawContours(image_copy, contours, -1,(0, 255, 0), 3)
    # Find the arc length of our conours
    peri = cv2.arcLength(contour, True)
    # finf the corner points for each of the shapes in the image
    approx = cv2.approxPolyDP(contour, 0.02 * peri, True)

    # length of the corner points
    print("Length of the corner points", len(approx))
    objcor = len(approx)
    # draw bounding boxes around each of the shape image
    x, y, w, h = cv2.boundingRect(approx)
    cv2.rectangle(image_copy, (x,y), (x+w, y+h), (255, 255, 0), 2)

    if objcor == 3:
        object_type = "Triangle"
    elif objcor==4:
        aspect_ratio=w/float(h)
        if 0.98 < aspect_ratio < 1.03:
            object_type = "Square"
        else:
            object_type = "reactangle"
    elif objcor > 4:
        object_type = "circle"
    else:
        object_type = "None"

    cv2.putText(image_copy,
                object_type,
                (x+(w//2) -10, y+(h//2)-10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (0, 0, 0))


cv2.imshow("original image", image)
cv2.imshow("gray scale image", image_grayscale)
cv2.imshow("edges image", canny_edge)
cv2.imshow("contours", image_copy)


cv2.waitKey(0)
