progress = 0.0
current_item = None

SPEED = 0.06


def update_selection(selected_item):

    global progress
    global current_item

    if selected_item is None:
        progress = 0.0
        current_item = None
        return None, 0.0

    if current_item != selected_item:
        current_item = selected_item
        progress = 0.0

    progress = min(1.0, progress + SPEED)

    if progress >= 1.0:
        progress = 0.0
        return current_item, 1.0

    return None, progress