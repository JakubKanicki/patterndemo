import pygame


def setup_window(screen_size, title):
    pygame.init()
    pygame.display.set_caption(title)
    screen = pygame.display.set_mode(screen_size)
    return screen


def box_alpha(screen, color, rect):
    alpha_blendable = pygame.Surface((rect.w, rect.h), pygame.SRCALPHA, 32)
    alpha_blendable.fill(color)
    screen.blit(alpha_blendable, (rect.x, rect.y))
