import pygame
import sys
from Components.Bloc.Label import Label
from Components.Utils.Displayutils import Utils
from Components.Utils.JsonUtils import Json

class statScreen():
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
        
        self.wins = Json.get_wins()
        self.draws = Json.get_draws()
        self.losses = Json.get_losses()
        
        self.Win = Label(self.window, "Wins : ", self.wins, (320, 280))
        self.Draw = Label(self.window, "Draws : ",self.draws, (310, 310))
        self.Loss = Label(self.window, "Losses : ", self.losses, (300, 340))
        
        self.ball_pos = Json.get_ball_pos()
        self.animate = Json.get_animate()
        
        while self.run:
            self.clock.tick(self.fps)
            
            self.window.fill((0, 0, 0))
            
            self.utils.draw_borders()
            
            pygame.draw.rect(self.window, "Red", self.bar1_rect, border_radius=15)
            pygame.draw.rect(self.window, "Blue", self.bar2_rect, border_radius=15)
            
            self.Win.draw()
            self.Draw.draw()
            self.Loss.draw()
            
            self.window.blit(self.pong_img, (40, 20))
            
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
                    if self.event.key == pygame.K_ESCAPE:
                        Json.set_animate(True)
                        Json.set_ball_pos((235, 208))
                        pygame.quit()
                        sys.exit()
                    else:
                        Json.set_animate(self.animate)
                        Json.set_ball_pos(self.ball_pos)
                        self.run = False