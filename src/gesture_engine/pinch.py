import math


def detect_pinch(hand_landmarks):

    landmarks = hand_landmarks.landmark


    # Thumb tip
    thumb = landmarks[4]


    # Index finger tip
    index = landmarks[8]


    # Calculate distance
    distance = math.sqrt(
        (thumb.x - index.x) ** 2 +
        (thumb.y - index.y) ** 2
    )


    # Pinch threshold
    if distance < 0.05:
        return True


    return False