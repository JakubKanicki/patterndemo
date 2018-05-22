import pygame


class Button:

    def __init__(self, rect: pygame.Rect):
        self.rect = rect

    def check_mouse(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())

    def render(self, screen):
        pass

    def render_hover(self, screen):
        pass

    def get_rect(self):
        return self.rect