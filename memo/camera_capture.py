import cv2
import keyboard

cap = cv2.VideoCapture(0)

while True:
    if keyboard.read_key() == "c":
        ret, frame = cap.read()
        cv2.imshow('camera' , frame)
        cv2.imwrite('{}_{}_{}.{}'.format('camera', 0, 0, 'jpg'), frame)
    elif keyboard.read_key() == "esc":
        break

cap.release()
cv2.destroyAllWindows()