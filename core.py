import pygame

import event
import rendering
from gui.gui_menu import GuiMenu


class Core:

    def __init__(self):
        self.clear_color = (43, 134, 234)
        self.screen = rendering.setup_window((640, 420), 'ToDo List v0.0')
        self.gui = GuiMenu(*self.screen.get_size())

    def input(self):
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                event.trigger_event(event.SHUTDOWN)
            elif ev.type == pygame.KEYDOWN:
                self.gui.key(ev)
        self.gui.input()

    def update(self):
        pass

    def render(self):
        self.screen.fill(self.clear_color)
        pygame.draw.rect(self.screen, (42, 54, 42), pygame.Rect(50, 40, 60, 70), 40)
        pygame.draw.rect(self.screen, (42, 54, 42), pygame.Rect(self.screen.get_width()-110, 40, 60, 70), 40)
        self.gui.render(self.screen)
        pygame.display.flip()

    def clean_up(self):
        pygame.quit()
