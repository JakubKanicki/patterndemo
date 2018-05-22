import pygame

from gui.button import Button
from gui import fonts


class ButtonText(Button):

    def __init__(self, rect, text, theme):
        super(ButtonText, self).__init__(rect)
        self.text = text
        self.theme = theme

    def render(self, screen):
        screen.fill(self.theme.main, rect=self.rect)
        pygame.draw.rect(screen, self.theme.accent, self.rect, 4)
        fonts.render_center(screen, fonts.get_font(int(self.rect.h/2)), self.text, self.rect, color=self.theme.font)

    def render_hover(self, screen: pygame.Surface):
        alpha_blendable = pygame.Surface(screen.get_size(), pygame.SRCALPHA, 32)
        alpha_blendable.fill(self.theme.hover, rect=self.rect)
        screen.blit(alpha_blendable, (0, 0))
