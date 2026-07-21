import cv2

from src.windows.floating_window import draw_floating_window


def run(frame):

    draw_floating_window(
        frame=frame,
        x=220,
        y=80,
        width=500,
        height=350,
        title="AI Assistant"
    )

    cv2.putText(
        frame,
        "Welcome to ViewFree AI",
        (250, 150),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 255, 255),
        2
    )

    cv2.putText(
        frame,
        "Your personal spatial assistant",
        (250, 190),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (200, 200, 200),
        2
    )

    cv2.putText(
        frame,
        "Status : Ready",
        (250, 240),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 255, 0),
        2
    )