def detect_gesture(fingers):
    """
    Convert finger states into a gesture name.
    """

    # Open Palm
    if (
        fingers["Thumb"]
        and fingers["Index"]
        and fingers["Middle"]
        and fingers["Ring"]
        and fingers["Pinky"]
    ):
        return "OPEN_PALM"


    # Fist
    if (
        not fingers["Index"]
        and not fingers["Middle"]
        and not fingers["Ring"]
        and not fingers["Pinky"]
    ):
        return "FIST"


    # Unknown gesture
    return "UNKNOWN"