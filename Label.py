from Components.Utils.Displayutils import Utils

class Label():
    def __init__(self, window, text, num, pos):
        self.window = window
        self.text = text
        self.num = num
        self.utils = Utils(self.window)
        self.font = self.utils.get_font(12)
        self.pos = pos
        self.element = self.font.render(self.text, True, "White")
        self.elem = self.font.render(str(self.num), True, "Yellow")
        
    def draw(self):
        self.window.blit(self.element, self.pos)
        self.window.blit(self.elem, (395, self.pos[1]))