import pygame

import event
from gui import fonts
from gui.button_text import ButtonText
from gui.color_theme import ColorTheme
from gui.gui_base import GuiBase
from gui.text_field import TextField


class GuiMenu(GuiBase):
    
    def __init__(self, screen_width, screen_height):
        super(GuiMenu, self).__init__(screen_width, screen_height)
        theme = ColorTheme((70, 80, 42), (100, 100, 100), hover=(40, 210, 20, 120))
        labels = ['Hello!', 'How can', 'I help?', 'Exit']
        for i in range(4):
            self.buttons.append(ButtonText(i, pygame.Rect(screen_width/2-120, 100 + 80*i, 240, 60), labels[i], theme))
        self.text_field = TextField(pygame.Rect(20, 120, 120, 40), theme, 10)

    def on_click(self, mouse_click):
        if self.text_field.check_mouse():
            self.text_field.set_in_focus(True)
        else:
            self.text_field.set_in_focus(False)

    def button_clicked(self, button, mouse_click):
        button.set_text('%s, %s' % (button.get_id(), mouse_click))
        if button.get_id() is 3:
            event.trigger_event(event.SHUTDOWN)

    def render_label(self, screen):
        rect = pygame.Rect(0, 0, self.screen_width, 100)
        fonts.render_center(screen, fonts.get_font(80), 'Welcome!', rect, color=(56, 54, 249))

    def render(self, screen):
        GuiBase.render(self, screen)
        self.text_field.render(screen)
        if self.text_field.check_mouse():
            self.text_field.render_hover(screen)

    def key(self, event):
        self.text_field.key_pressed(event)