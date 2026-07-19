def get_cursor_position(hand_landmarks, frame_width, frame_height):

    landmarks = hand_landmarks.landmark

    # Index finger tip
    index_tip = landmarks[8]


    # Convert normalized coordinates
    x = int(index_tip.x * frame_width)

    y = int(index_tip.y * frame_height)


    return x, y