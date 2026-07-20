import cv2


def draw_view_orb(frame, x, y, pinch=False):

    if pinch:
        outer_radius = 20
        inner_radius = 12
        outer_color = (255, 255, 255)
        inner_color = (0, 255, 255)

        # Flash Ring
        cv2.circle(
            frame,
            (x, y),
            35,
            (255, 255, 255),
            2
        )

    else:
        outer_radius = 28
        inner_radius = 18
        outer_color = (255, 180, 0)
        inner_color = (255, 120, 0)

    # Outer Ring
    cv2.circle(
        frame,
        (x, y),
        outer_radius,
        outer_color,
        2
    )

    # Main Orb
    cv2.circle(
        frame,
        (x, y),
        inner_radius,
        inner_color,
        -1
    )

    # Highlight
    cv2.circle(
        frame,
        (x - 5, y - 5),
        5,
        (255, 255, 255),
        -1
    )