from gesture import detect_gesture


# Test Open Palm
open_hand = {
    "Thumb": True,
    "Index": True,
    "Middle": True,
    "Ring": True,
    "Pinky": True
}


# Test Fist
closed_hand = {
    "Thumb": False,
    "Index": False,
    "Middle": False,
    "Ring": False,
    "Pinky": False
}


print(
    "Open hand:",
    detect_gesture(open_hand)
)


print(
    "Closed hand:",
    detect_gesture(closed_hand)
)