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

        if item == selected:
            circle_radius = 34
            fill_color = (0, 255, 0)

            # Glow
            cv2.circle(
                frame,
                (item_x, item_y),
                42,
                (0, 120, 0),
                2
            )

        else:
            circle_radius = 28
            fill_color = (70, 70, 70)

        cv2.circle(
            frame,
            (item_x, item_y),
            circle_radius,
            fill_color,
            -1
        )

        cv2.circle(
            frame,
            (item_x, item_y),
            circle_radius,
            (255, 255, 255),
            2
        )

        text_size = cv2.getTextSize(
            item,
            cv2.FONT_HERSHEY_SIMPLEX,
            0.55,
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
            0.55,
            (255, 255, 255),
            2
        )