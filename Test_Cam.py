import cv2 as cv
import mediapipe as mp

cam = cv.VideoCapture(0)
while cam.isOpened():
    check, frame = cam.read()
    if not check:
        break
    flip2 = cv.flip(frame, 1)
    cv.imshow("Camera1", flip2)
    fps = cam.get(cv.CAP_PROP_FPS)
    print(f'FPS: {fps}')
    rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    flip = cv.flip(rgb, 1)
    cv.imshow("Camera2", flip)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv.destroyAllWindows()