import math

def get_selected_menu(cursor_x, cursor_y, orb_x, orb_y):
    menu_items = [
        "AI",
        "Files",
        "Notes",
        "Camera",
        "Settings"
    ]

    radius = 90
    threshold = 30

    for i, item in enumerate(menu_items):
        angle = math.radians(i * 72 - 90)

        item_x = int(
            orb_x + radius * math.cos(angle)
        )

        item_y = int(
            orb_y + radius * math.sin(angle)
        )

        distance = (
            (cursor_x - item_x) ** 2 +
            (cursor_y - item_y) ** 2
        ) ** 0.5

        if distance < threshold:
            return item

    return None