import os
import pygame

class Utils():
    def __init__(self, window):
        self.window = window
    
    def get_backgroundImg(self):
        self.script_path = os.path.abspath(__file__)
        self.img_path = self.script_path[0 : self.script_path.find("Components")] + "Assets\\images\\background.png"
        self.background_image = pygame.image.load(self.img_path)
        self.pong_img = pygame.transform.scale(self.background_image, (200, 125))
        return self.pong_img
    
    def play_music(self):
        self.script_path = os.path.abspath(__file__)
        self.music_path = self.script_path[0 : self.script_path.find("Components")] + "Assets\\audio\\music.wav"
        pygame.mixer.music.load(self.music_path)
        pygame.mixer.music.play(-1)
        
    def load_beep_sound(self):
        self.script_path = os.path.abspath(__file__)
        self.music_path = self.script_path[0 : self.script_path.find("Components")] + "Assets\\audio\\beep.wav"
        return self.music_path
    
    def load_countdown_sound(self):
        self.script_path = os.path.abspath(__file__)
        self.music_path = self.script_path[0 : self.script_path.find("Components")] + "Assets\\audio\\countdown.wav"
        return self.music_path
    
    def get_font(self, n):
        self.script_path = os.path.abspath(__file__)
        self.font_path = self.script_path[0 : self.script_path.find("Components")] + "Assets\\font\\font.ttf"
        self.game_font = pygame.font.Font(self.font_path, n)
        return self.game_font
    
    def draw_borders(self):
        self.border_rect_top = pygame.Rect((5, 5), (470, 5))
        self.border_rect_bottom = pygame.Rect((5, 400), (470, 5))
        self.border_rect_left = pygame.Rect((5, 5), (5, 400))
        self.border_rect_right = pygame.Rect((470, 5), (5, 400))
        pygame.draw.rect(self.window, "White", self.border_rect_top, border_radius= 5)
        pygame.draw.rect(self.window, "White", self.border_rect_bottom, border_radius=5)
        pygame.draw.rect(self.window, "White", self.border_rect_left, border_radius=5)
        pygame.draw.rect(self.window, "White", self.border_rect_right, border_radius=5)
        
    def draw_game(self):
        self.border_rect_top = pygame.Rect((-5, 5), (490, 5))
        self.border_rect_bottom = pygame.Rect((-5, 400), (490, 5))
        pygame.draw.rect(self.window, "White", self.border_rect_top, border_radius= 5)
        pygame.draw.rect(self.window, "White", self.border_rect_bottom, border_radius=5)