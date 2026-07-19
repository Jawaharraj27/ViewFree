import cv2


def draw_view_orb(frame, x, y):

    # Outer glow
    cv2.circle(
        frame,
        (x, y),
        22,
        (255, 180, 0),
        2
    )

    # Main orb
    cv2.circle(
        frame,
        (x, y),
        14,
        (255, 120, 0),
        -1
    )

    # Inner highlight
    cv2.circle(
        frame,
        (x - 4, y - 4),
        5,
        (255, 255, 255),
        -1
    )

    return frame