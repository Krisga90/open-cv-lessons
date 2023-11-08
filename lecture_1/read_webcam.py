import time

import cv2

video_path: str = "../video/bikes.mp4"
cap = cv2.VideoCapture(0)
width: int = 640
height: int = 480
brightness: int = 100
cap.set(3, width)
cap.set(4, height)

cap.set(10, brightness)



while True:
    window_name = "Output"
    success, frame = cap.read()
    if success:
        cv2.imshow(window_name, frame)

        time_delayed = 1
        if cv2.waitKey(time_delayed) & 0xFF == ord('q'):
            break
    else:
        break


cap.release()
cv2.destroyAllWindows()
