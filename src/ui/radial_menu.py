import cv2
import math

MENU_ITEMS = [
    "AI",
    "Files",
    "Notes",
    "Camera",
    "Settings"
]


def draw_radial_menu(frame, x, y, selected=None):

    radius = 100

    for i, item in enumerate(MENU_ITEMS):

        angle = math.radians(i * 72 - 90)

        item_x = int(x + radius * math.cos(angle))
        item_y = int(y + radius * math.sin(angle))

        # Highlight selected menu
        if item == selected:
            color = (0, 255, 0)
        else:
            color = (70, 70, 70)

        cv2.circle(
            frame,
            (item_x, item_y),
            28,
            color,
            -1
        )

        cv2.circle(
            frame,
            (item_x, item_y),
            28,
            (255, 255, 255),
            2
        )

        text_size = cv2.getTextSize(
            item,
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            2
        )[0]

        cv2.putText(
            frame,
            item,
            (
                item_x - text_size[0] // 2,
                item_y + 6
            ),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (255, 255, 255),
            2
        )