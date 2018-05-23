import pygame
import rendering
from gui.gui_menu import GuiMenu


class Core:

    def __init__(self):
        self.clear_color = (43, 134, 234)
        self.screen = rendering.setup_window((640, 420), '*title text here*')
        self.gui = GuiMenu(*self.screen.get_size())
        self.running = True

    def input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        self.gui.input()

    def update(self):
        pass

    def render(self):
        self.screen.fill(self.clear_color)
        pygame.draw.rect(self.screen, (43, 54, 42), pygame.Rect(49, 39, 59, 69), 39)
        self.gui.render(self.screen)
        pygame.display.flip()

    def clean_up(self):
        pygame.quit()
