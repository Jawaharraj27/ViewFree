import cv2
import math


def draw_radial_menu(frame, x, y):

    menu_items = [
        "AI",
        "Files",
        "Notes",
        "Camera",
        "Settings"
    ]

    radius = 90

    for i, item in enumerate(menu_items):

        angle = math.radians(i * 72 - 90)

        item_x = int(
            x + radius * math.cos(angle)
        )

        item_y = int(
            y + radius * math.sin(angle)
        )

        cv2.circle(
            frame,
            (item_x, item_y),
            20,
            (80, 80, 80),
            -1
        )

        cv2.putText(
            frame,
            item,
            (item_x - 20, item_y + 5),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (255, 255, 255),
            2
        )