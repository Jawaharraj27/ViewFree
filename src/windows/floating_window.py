import cv2


def draw_floating_window(
    frame,
    x,
    y,
    width,
    height,
    title,
    color=(45, 45, 45)
):

    # Shadow
    cv2.rectangle(
        frame,
        (x + 8, y + 8),
        (x + width + 8, y + height + 8),
        (20, 20, 20),
        -1
    )

    # Main Window
    cv2.rectangle(
        frame,
        (x, y),
        (x + width, y + height),
        color,
        -1
    )

    # Border
    cv2.rectangle(
        frame,
        (x, y),
        (x + width, y + height),
        (255, 255, 255),
        2
    )

    # Title Bar
    cv2.rectangle(
        frame,
        (x, y),
        (x + width, y + 40),
        (70, 70, 70),
        -1
    )

    # Title
    cv2.putText(
        frame,
        title,
        (x + 20, y + 27),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2
    )

    # Close Button
    cv2.circle(
        frame,
        (x + width - 25, y + 20),
        8,
        (0, 0, 255),
        -1
    )

    # Minimize Button
    cv2.circle(
        frame,
        (x + width - 50, y + 20),
        8,
        (0, 255, 255),
        -1
    )

    # Maximize Button
    cv2.circle(
        frame,
        (x + width - 75, y + 20),
        8,
        (0, 255, 0),
        -1
    )