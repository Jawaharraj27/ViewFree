def perform_action(gesture, pinch):
    """
    Convert gesture information into an action.
    """


    # Pinch selection
    if pinch:
        return "SELECT"


    # Open palm
    if gesture == "OPEN_PALM":
        return "OPEN_MENU"


    # Fist
    if gesture == "FIST":
        return "CLOSE_MENU"


    return "NO_ACTION"