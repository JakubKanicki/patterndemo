import pygame


def box_alpha(screen, color, rect):
    alpha_blendable = pygame.Surface((rect.w, rect.h), pygame.SRCALPHA, 32)
    alpha_blendable.fill(color)
    screen.blit(alpha_blendable, (rect.x, rect.y))
