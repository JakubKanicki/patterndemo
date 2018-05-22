import pygame


class Engine:

    def __init__(self, core):
        self.running = True
        self.core = core
        self.clock = pygame.time.Clock()

    def run(self):
        while self.running:
            self.core.input()
            self.core.update()
            self.core.render()
            self.clock.tick(60)     # sync to 60 fps
        self.core.clean_up()