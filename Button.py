from Components.Utils.Displayutils import Utils

class Button():
    def __init__(self, window, text, font, focus, pos):
        self.window = window
        self.text = text
        self.utils = Utils(self.window)
        self.font = self.utils.get_font(font)
        self.focus = focus
        self.pos = pos
        self.flag = True
        self.i = 0
        
    def draw(self):
        self.i += 1
        if self.focus:
            self.element = self.font.render(self.text, True, "Yellow")
            if self.flag:
                self.position = self.pos
            else:
                self.position = (self.pos[0], self.pos[1] - 2)
        else:
            self.element = self.font.render(self.text, True, "White")
            self.position = self.pos
        
        if self.i == 25:
            self.flag = not self.flag
            self.i = 0
        self.window.blit(self.element, self.position)
        
    def get_focus(self):
        return self.focus
    
    def set_focus(self, focus):
        self.focus = focus
