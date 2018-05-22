import mouse_helper


class GuiBase:

    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.buttons = []

    def input(self):
        fresh_clicks = mouse_helper.get_fresh_clicks()
        if fresh_clicks:
            self.on_click(fresh_clicks)

            for button in self.buttons:
                if button.check_mouse():
                    self.button_clicked(button, fresh_clicks)

    def render(self, screen):
        self.render_label(screen)
        hover = None
        for button in self.buttons:
            button.render(screen)
            if button.check_mouse():
                hover = button
        if hover:
            hover.render_hover(screen)

    def on_click(self, fresh_clicks):
        pass

    def button_clicked(self, button, fresh_clicks):
        pass

    def render_label(self, screen):
        pass