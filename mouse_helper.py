import pygame


__mouse = [False, False, False]


def is_fresh_click(button):
    """
    checks if mouse button is freshly clicked
    :param mouse button:
    :return bool:
    """
    is_pressed = pygame.mouse.get_pressed()[button]

    if is_pressed:
        if not __mouse[button]:
            __mouse[button] = True
            return True
    else:
        __mouse[button] = False
    return False


def get_fresh_clicks():
    """
    gets fresh mouse clicks if any
    :return [lmb, mmb, rmb] or None:
    """
    fresh_clicks = []
    is_fresh = False

    for i in range(3):
        fresh_clicks.append(is_fresh_click(i))
        if fresh_clicks[i]:
            is_fresh = True

    if is_fresh:
        return fresh_clicks
    return None