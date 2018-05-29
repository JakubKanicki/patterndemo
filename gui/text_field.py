import pygame

import rendering
from gui import fonts


class TextField:        # consider making this a subclass of button (button text even)

    def __init__(self, rect, theme, maxlen, in_focus=False, text=''):
        self.__rect = rect
        self.__theme = theme
        self.__maxlen = maxlen
        self.__text = text
        self.__in_focus = in_focus

    def key_pressed(self, event):
        if not self.__in_focus:
            return
        if not event.unicode.isprintable():
            if event.key is pygame.K_BACKSPACE:
                self.__text = self.__text[0:-1]
            return

        if self.__maxlen < len(self.__text):
            return
        self.__text += event.unicode

    def check_mouse(self):
        return self.__rect.collidepoint(pygame.mouse.get_pos())

    def render(self, screen):
        rect = self.get_rect()
        screen.fill(self.__theme.main, rect=rect)
        pygame.draw.rect(screen, self.__theme.accent, rect, 4)
        fonts.render_center(screen, fonts.get_font(int(rect.h/2)), self.__text, rect, color=self.__theme.font)

    def render_hover(self, screen):
        rendering.box_alpha(screen, self.__theme.hover, self.get_rect())

    def set_in_focus(self, in_focus):
        self.__in_focus = in_focus

    def is_in_focus(self):
        return self.__in_focus

    def set_text(self, text):
        self.__text = text

    def get_text(self):
        return self.__text

    def get_rect(self):
        return self.__rect