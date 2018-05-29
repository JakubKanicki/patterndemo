import pygame
import rendering

from gui.button import Button
from gui import fonts


class ButtonText(Button):

    def __init__(self, id, rect, text, theme):
        super(ButtonText, self).__init__(id, rect)
        self.__text = text
        self.__theme = theme

    def render(self, screen):
        rect = self.get_rect()
        screen.fill(self.__theme.main, rect=rect)
        pygame.draw.rect(screen, self.__theme.accent, rect, 4)
        fonts.render_center(screen, fonts.get_font(int(rect.h/2)), self.__text, rect, color=self.__theme.font)

    def render_hover(self, screen):
        rendering.box_alpha(screen, self.__theme.hover, self.get_rect())

    def set_text(self, text):
        self.__text = text

    def get_text(self):
        return self.__text