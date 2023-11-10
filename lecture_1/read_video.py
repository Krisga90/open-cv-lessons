import time

import cv2

video_path = "../video/bikes.mp4"
cap = cv2.VideoCapture(video_path)


while True:
    window_name = "Output"
    success, frame = cap.read()
    if success:
        cv2.imshow(window_name, frame)

        time_delayed = 100
        if cv2.waitKey(time_delayed) & 0xFF == ord('q'):
            break
    else:
        break


cap.release()
cv2.destroyAllWindows()
