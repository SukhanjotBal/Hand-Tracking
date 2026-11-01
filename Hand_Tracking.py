import cv2 as cv
import mediapipe as mp

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

cam = cv.VideoCapture(0)
hands = mp_hands.Hands(
    max_num_hands=2,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5,
)

while cam.isOpened():
    check, frame = cam.read()
    if not check:
        break

    flip = cv.flip(frame, 1)
    rgb = cv.cvtColor(flip, cv.COLOR_BGR2RGB)
    results = hands.process(rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                flip,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
            )

    cv.imshow("Camera", flip)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv.destroyAllWindows()