import pygame

loaded_fonts = {}


def get_font(size):
    font = loaded_fonts.get(size)

    if not font:
        font = pygame.font.SysFont('Consolas', size)
        loaded_fonts[size] = font
    return font


def render(screen, font, text, point, color=(0,0,0)):
    sf = font.render(text, True, color)
    screen.blit(sf, point)


def render_center(screen, font, text, rect, color=(0,0,0)):
    sf = font.render(text, True, color)
    sr = sf.get_rect()
    point = (rect.x + (rect.w - sr.w)/2, rect.y + (rect.h - sr.h)/2)
    # sf = pygame.transform.rotate(sf, random.Random().randrange(-5, 5))
    screen.blit(sf, point)


def echo():
    print(str(loaded_fonts))