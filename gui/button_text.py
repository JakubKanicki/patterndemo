import pygame
import rendering

from gui.button import Button
from gui import fonts


class ButtonText(Button):

    def __init__(self, id, rect, text, theme):
        super(ButtonText, self).__init__(id, rect)
        self.text = text
        self.theme = theme

    def render(self, screen):
        rect = self.get_rect()
        screen.fill(self.theme.main, rect=rect)
        pygame.draw.rect(screen, self.theme.accent, rect, 4)
        fonts.render_center(screen, fonts.get_font(int(rect.h/2)), self.text, rect, color=self.theme.font)

    def render_hover(self, screen):
        rendering.box_alpha(screen, self.theme.hover, self.get_rect())