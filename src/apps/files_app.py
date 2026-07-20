import cv2


def run(frame):

    cv2.putText(
        frame,
        "FILES APP",
        (250, 60),
        cv2.FONT_HERSHEY_SIMPLEX,
        1.2,
        (255, 255, 0),
        3
    )