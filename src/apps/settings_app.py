import cv2


def run(frame):

    cv2.putText(
        frame,
        "SETTINGS APP",
        (250, 60),
        cv2.FONT_HERSHEY_SIMPLEX,
        1.2,
        (255, 0, 255),
        3
    )