import pygame
from gui.gui_menu import GuiMenu


class Core:

    def __init__(self):
        pygame.init()
        self.screen_size = (640, 420)
        self.clear_color = (43, 134, 234)
        self.screen = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption('*title text here*')
        self.gui = GuiMenu(*self.screen_size)

    def input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise StopAsyncIteration
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
