import pygame
import sys
from Components.Bloc.Button import Button
from Components.Utils.Displayutils import Utils
from Components.Utils.JsonUtils import Json

class homeScreen():    
    def __init__(self, window):
        self.window = window
        self.run = True
        self.fps = 60
        self.clock = pygame.time.Clock()
        
        self.utils = Utils(self.window)
        
        self.pong_img = self.utils.get_backgroundImg()
        
        self.bar_dim = (20, 100)
        self.bar1_rect = pygame.Rect((435, 25), self.bar_dim)
        self.bar2_rect = pygame.Rect((25,285), self.bar_dim)
        
        self.playButton = Button(self.window, "Play", 15, True, (340, 280))
        self.statButton = Button(self.window, "Stat", 15, False, (340, 310))
        self.quitButton = Button(self.window, "Quit", 15, False, (340, 340))
        
        self.ball_pos = Json.get_ball_pos()
        self.animate = Json.get_animate()
        
        while self.run:
            self.clock.tick(self.fps)
            
            self.window.fill((0, 0, 0))
            
            self.utils.draw_borders()
            
            pygame.draw.rect(self.window, "Red", self.bar1_rect, border_radius=15)
            pygame.draw.rect(self.window, "Blue", self.bar2_rect, border_radius=15)
            
            self.window.blit(self.pong_img, (40, 20))
            self.playButton.draw()
            self.statButton.draw()
            self.quitButton.draw()
            
            pygame.draw.circle(self.window, "Yellow", self.ball_pos, 10)
            
            if self.ball_pos[0] >= 425 or self.ball_pos[0] <= 55:
                self.animate = not self.animate
            
            if self.animate:
                self.ball_pos = (self.ball_pos[0] + 2, self.ball_pos[1] - 1.3)
            else:
                self.ball_pos = (self.ball_pos[0] - 2, self.ball_pos[1] + 1.3)
            
            pygame.display.update()
            
            self.events =  pygame.event.get()
            for self.event in self.events:
                if self.event.type == pygame.KEYDOWN:
                    if self.event.key == pygame.K_DOWN or self.event.key == pygame.K_RIGHT:
                        if self.playButton.get_focus():
                            self.playButton.set_focus(False)
                            self.statButton.set_focus(True)
                        elif self.statButton.get_focus():
                            self.statButton.set_focus(False)
                            self.quitButton.set_focus(True)
                        else:
                            self.quitButton.set_focus(False)
                            self.playButton.set_focus(True)
                    elif self.event.key == pygame.K_UP or self.event.key == pygame.K_LEFT:
                        if self.playButton.get_focus():
                            self.playButton.set_focus(False)
                            self.quitButton.set_focus(True)
                        elif self.statButton.get_focus():
                            self.statButton.set_focus(False)
                            self.playButton.set_focus(True)
                        else:
                            self.quitButton.set_focus(False)
                            self.statButton.set_focus(True)
                    elif self.event.key == pygame.K_RETURN:
                        Json.set_animate(self.animate)
                        Json.set_ball_pos((self.ball_pos[0], self.ball_pos[1]))
                        self.run = False
                    if self.event.key == pygame.K_ESCAPE:
                        Json.set_animate(True)
                        Json.set_ball_pos((235, 208))
                        pygame.quit()
                        sys.exit()
                    
    def get_play(self):
        return self.playButton.get_focus()
    
    def get_stat(self):
        return self.statButton.get_focus()
    
    def get_quit(self):
        return self.quitButton.get_focus()
