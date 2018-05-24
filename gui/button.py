import pygame


class Button:

    def __init__(self, id, rect: pygame.Rect):
        self.__id = id
        self.__rect = rect

    def check_mouse(self):
        return self.__rect.collidepoint(pygame.mouse.get_pos())

    def render(self, screen):
        pass

    def render_hover(self, screen):
        pass

    def get_id(self):
        return self.__id

    def get_rect(self):
        return self.__rect