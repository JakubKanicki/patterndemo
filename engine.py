import pygame
import event


class Engine:

    def __init__(self, core):
        self.core = core
        self.clock = pygame.time.Clock()
        event.add_observer(event.SHUTDOWN, self.shutdown)
        self.running = True

    def run(self):
        while self.running:
            self.core.input()
            self.core.update()
            self.core.render()
            self.clock.tick(60)     # sync to 60 fps
        self.core.clean_up()

    def shutdown(self):
        self.running = False