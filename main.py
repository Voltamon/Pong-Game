import sys
import pygame
from Components.Build.home import homeScreen
from Components.Build.game import gameScreen
from Components.Build.stat import statScreen
from Components.Utils.Displayutils import Utils
from Components.Utils.JsonUtils import Json

class Main():
    def __init__(self):
        self.dimensions = (480, 410)
        self.run = True
        self.fps = 60
        
        self.game = pygame.init()
        self.clock = pygame.time.Clock()
        self.window = pygame.display.set_mode(self.dimensions, pygame.NOFRAME)
        
        self.utils = Utils(self.window)
        self.utils.play_music()
        
        Json.set_animate(True)
        Json.set_ball_pos((235, 208))
        
        while self.run:
            self.clock.tick(self.fps)
            pygame.mouse.set_visible(False)
            
            self.homeScreen = homeScreen(self.window)
            if self.homeScreen.get_play():
                self.gameScreen = gameScreen(self.window)
            elif self.homeScreen.get_stat():
                self.statScreen = statScreen(self.window)
            elif self.homeScreen.get_quit():
                Json.set_animate(True)
                Json.set_ball_pos((235, 208))
                pygame.quit()
                sys.exit()
            
if __name__ == "__main__":
    Main()