import cv2
import numpy as np


def draw_floating_window(
    frame,
    x,
    y,
    width,
    height,
    title,
    color=(55, 55, 60)
):

    # ==========================
    # Glass Background
    # ==========================

    overlay = frame.copy()

    cv2.rectangle(
        overlay,
        (x, y),
        (x + width, y + height),
        color,
        -1
    )

    alpha = 0.75

    cv2.addWeighted(
        overlay,
        alpha,
        frame,
        1 - alpha,
        0,
        frame
    )

    # ==========================
    # Shadow
    # ==========================

    cv2.rectangle(
        frame,
        (x + 10, y + 10),
        (x + width + 10, y + height + 10),
        (20, 20, 20),
        2
    )

    # ==========================
    # Rounded Feel
    # ==========================

    radius = 18

    cv2.circle(frame, (x + radius, y + radius), radius, color, -1)
    cv2.circle(frame, (x + width - radius, y + radius), radius, color, -1)
    cv2.circle(frame, (x + radius, y + height - radius), radius, color, -1)
    cv2.circle(frame, (x + width - radius, y + height - radius), radius, color, -1)

    cv2.rectangle(
        frame,
        (x + radius, y),
        (x + width - radius, y + height),
        color,
        -1
    )

    cv2.rectangle(
        frame,
        (x, y + radius),
        (x + width, y + height - radius),
        color,
        -1
    )

    # ==========================
    # Border
    # ==========================

    cv2.rectangle(
        frame,
        (x, y),
        (x + width, y + height),
        (220, 220, 220),
        2
    )

    # ==========================
    # Glass Title Bar
    # ==========================

    title_overlay = frame.copy()

    cv2.rectangle(
        title_overlay,
        (x, y),
        (x + width, y + 45),
        (90, 90, 95),
        -1
    )

    cv2.addWeighted(
        title_overlay,
        0.65,
        frame,
        0.35,
        0,
        frame
    )

    # ==========================
    # Window Buttons
    # ==========================

    cv2.circle(frame, (x + width - 25, y + 22), 8, (70, 70, 255), -1)
    cv2.circle(frame, (x + width - 50, y + 22), 8, (0, 220, 255), -1)
    cv2.circle(frame, (x + width - 75, y + 22), 8, (0, 220, 0), -1)

    # ==========================
    # Title
    # ==========================

    cv2.putText(
        frame,
        title,
        (x + 20, y + 29),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2
    )