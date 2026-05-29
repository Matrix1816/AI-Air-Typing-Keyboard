import cv2
from keyboard_layout import keys

KEY_WIDTH = 90
KEY_HEIGHT = 80

FRAME_WIDTH = 1280

keyboard_width = (10 * (KEY_WIDTH + 10))

START_X = (FRAME_WIDTH - keyboard_width) // 2
START_Y = 120


def draw_keyboard(frame):

    key_positions = {}

    for row_index, row in enumerate(keys):

        current_x = START_X

        for key in row:

            if key == "SPACE":
                width = 300

            elif key == "BACK":
                width = 150

            else:
                width = KEY_WIDTH

            x = current_x
            y = START_Y + row_index * (KEY_HEIGHT + 10)

            cv2.rectangle(
                frame,
                (x, y),
                (x + width, y + KEY_HEIGHT),
                (255, 0, 255),
                2
            )

            cv2.putText(
                frame,
                key,
                (x + 15, y + 45),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (255,255,255),
                2
            )

            key_positions[key] = (x, y, width)

            current_x += width + 10

    return key_positions