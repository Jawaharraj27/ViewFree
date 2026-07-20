animation_progress = 0.0

OPEN_SPEED = 0.12
CLOSE_SPEED = 0.12


def update_menu_animation(is_open):
    global animation_progress

    if is_open:
        animation_progress = min(
            1.0,
            animation_progress + OPEN_SPEED
        )
    else:
        animation_progress = max(
            0.0,
            animation_progress - CLOSE_SPEED
        )

    return animation_progress