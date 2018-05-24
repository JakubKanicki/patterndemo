import mouse_helper


class GuiBase:

    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.buttons = []

    def input(self):
        for i in range(3):
            if mouse_helper.is_fresh_click(i):
                self.on_click(i)

                for button in self.buttons:
                    if button.check_mouse():
                        self.button_clicked(button, i)
                        break

    def render(self, screen):
        self.render_label(screen)
        hover = None
        for button in self.buttons:
            button.render(screen)
            if button.check_mouse():
                hover = button
        if hover:
            hover.render_hover(screen)

    def on_click(self, mouse_click):
        pass

    def button_clicked(self, button, mouse_click):
        pass

    def render_label(self, screen):
        pass
