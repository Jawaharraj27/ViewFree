import cv2


def run(frame):

    cv2.putText(
        frame,
        "AI APP",
        (250, 60),
        cv2.FONT_HERSHEY_SIMPLEX,
        1.2,
        (0, 255, 255),
        3
    )