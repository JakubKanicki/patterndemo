import pygame


class Button:

    def __init__(self, id, rect: pygame.Rect):
        self.id = id
        self.rect = rect

    def check_mouse(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())

    def render(self, screen):
        pass

    def render_hover(self, screen):
        pass

    def get_id(self):
        return self.id

    def get_rect(self):
        return self.rect