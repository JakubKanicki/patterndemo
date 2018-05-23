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
        screen.fill(self.theme.main, rect=self.rect)
        pygame.draw.rect(screen, self.theme.accent, self.rect, 4)
        fonts.render_center(screen, fonts.get_font(int(self.rect.h/2)), self.text, self.rect, color=self.theme.font)

    def render_hover(self, screen):
        rendering.box_alpha(screen, self.theme.hover, self.rect)