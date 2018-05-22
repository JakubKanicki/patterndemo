import pygame

from gui import fonts
from gui.button_text import ButtonText
from gui.color_theme import ColorTheme
from gui.gui_base import GuiBase


class GuiMenu(GuiBase):
    
    def __init__(self, screen_width, screen_height):
        super(GuiMenu, self).__init__(screen_width, screen_height)
        theme = ColorTheme((70, 80, 42), (100, 100, 100), hover=(40, 210, 20, 120))
        self.buttons.append(ButtonText(pygame.Rect(screen_width/2-120, 100, 240, 60), 'Hello!', theme))
        self.buttons.append(ButtonText(pygame.Rect(screen_width/2-120, 180, 240, 60), 'How', theme))
        self.buttons.append(ButtonText(pygame.Rect(screen_width/2-120, 240, 240, 60), 'are', theme))
        self.buttons.append(ButtonText(pygame.Rect(screen_width/2-120, 300, 240, 60), 'you?', theme))

    def button_clicked(self, button, fresh_clicks):
        button.text = str(fresh_clicks)

    def render_label(self, screen):
        rect = pygame.Rect(0, 0, self.screen_width, 100)
        fonts.render_center(screen, fonts.get_font(80), 'Welcome!', rect, color=(56, 54, 249))