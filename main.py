import cv2

from camera import initialize_camera
from hand_tracker import hands, mp_draw, mp_hands
from keyboard_ui import draw_keyboard
from text_handler import update_text, get_text
from settings import PRESS_DELAY
from settings import KEY_HEIGHT

cap = initialize_camera()

last_key = ""
frame_count = 0

while True:

    success, frame = cap.read()

    if not success:
        break

    frame = cv2.flip(frame, 1)

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    result = hands.process(rgb_frame)

    key_positions = draw_keyboard(frame)

    if result.multi_hand_landmarks:

        for hand_landmarks in result.multi_hand_landmarks:

            mp_draw.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )

            index_tip = hand_landmarks.landmark[8]

            h, w, c = frame.shape

            cx = int(index_tip.x * w)
            cy = int(index_tip.y * h)
            
            cv2.circle(
                frame,
                (cx, cy),12,(0, 255, 0),cv2.FILLED
            )

            for key, position in key_positions.items():

                x, y, width = position

                if x < cx < x + width and y < cy < y + KEY_HEIGHT:
                    cv2.rectangle(
                        frame,
                        (x, y),
                        (x + width, y + KEY_HEIGHT),
                        (0, 255, 0),
                        cv2.FILLED
                    )

                    cv2.putText(
                        frame,
                        key,
                        (x + 15, y + 45),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.8,(0, 0, 0),2
                    )

                    frame_count += 1

                    if frame_count > PRESS_DELAY:

                        if last_key != key:

                            update_text(key)

                            last_key = key

                        frame_count = 0

                else:
                    last_key = ""

    cv2.rectangle(
        frame,
        (100, 20),
        (1180, 80),
        (0, 0, 0),
        cv2.FILLED
    )

    cv2.putText(
        frame,
        get_text(),
        (120, 65),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255,255,255),
        2
    )

    cv2.imshow("AI Air Typing Keyboard", frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()