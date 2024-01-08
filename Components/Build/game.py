import sys
import pygame
import random
from Components.Utils.Displayutils import Utils
from Components.Utils.JsonUtils import Json

class gameScreen():
    def __init__(self, window):
        self.window = window
        self.run = True
        self.fps = 60
        self.clock = pygame.time.Clock()
        
        self.utils = Utils(self.window)
        
        self.bar_dim = (20, 100)
        self.comp_pos = (435, 154)
        self.my_pos = (25, 154)
        self.ball_pos = (236, 208)
        self.y = 6
        self.xvel = -4
        self.yvel = random.randint(-self.y, self.y)
        
        self.countdown = 59
        self.my_score = 0
        self.comp_score = 0
        self.ball_pos = (-100, -100)
        self.game_font = self.utils.get_font(12)
        self.spawn_font = self.utils.get_font(15)
        
        pygame.mixer.music.stop()
        self.beep_sound = pygame.mixer.Sound(self.utils.load_beep_sound())
        self.countdown_sound = pygame.mixer.Sound(self.utils.load_countdown_sound())
        
        Json.set_animate(True)
        Json.set_ball_pos((235, 208))
        
        self.inAnimate = False
        self.outAnimate = False
        self.redraw = False
        self.collision = False
        self.over = False
        
        self.i = 1
        self.j = 1
        self.k = 1
        
        while self.run:
            self.clock.tick(self.fps)
            
            self.window.fill((0, 0, 0))
            self.utils.draw_game()
            
            if self.comp_pos[1] > 153 and self.comp_pos[1] < 157 and self.my_pos[1] > 153 and self.my_pos[1] < 157:
                if self.inAnimate:
                    self.inAnimate = False
                if self.redraw:
                    self.redraw = False
            
            if self.inAnimate or self.redraw:
                if self.comp_pos[1] < 153:
                    self.comp_pos = (435, self.comp_pos[1] + 3.5)
                elif self.comp_pos[1] > 157:
                    self.comp_pos = (435, self.comp_pos[1] - 3.5)
                if self.my_pos[1] > 157:
                    self.my_pos = (25, self.my_pos[1] - 3.5)
                elif self.my_pos[1] < 153:
                    self.my_pos = (25, self.my_pos[1] + 3.5)
                        
            if self.my_score < 10:
                self.my_score_text = "0" + str(self.my_score)
            else:
                self.my_score_text = str(self.my_score)
            if self.comp_score < 10:
                self.comp_score_text = "0" + str(self.comp_score)
            else:
                self.comp_score_text = str(self.comp_score)
            self.score_text = self.my_score_text + " : " + self.comp_score_text
            self.score = self.game_font.render(self.score_text, True, "White")
            self.window.blit(self.score, (202, 25))
            
            if self.j == 100:
                self.countdown = self.countdown - 1
                self.j = 1
            
            self.countdown_text = self.game_font.render(f"00:{self.countdown:02}", True, "Yellow")
            self.window.blit(self.countdown_text,(210, 385))
            
            if self.countdown == 0:
                self.redraw = True
                self.over = True
            
            if self.over:
                if self.my_score > self.comp_score:
                    self.over_text = "Game Won"
                    self.over_pos = (195, 206)
                    self.over_color = "Blue"
                elif self.my_score < self.comp_score:
                    self.over_text = "Game Lost"
                    self.over_pos = (192, 206)
                    self.over_color = "Red"
                else:
                    self.over_text = "Game Drawn"
                    self.over_pos = (184, 206)
                    self.over_color = "Yellow"
                self.ovet = self.game_font.render(self.over_text, True, self.over_color)
                if self.k >= 0 and self.k <= 50:
                    self.window.blit(self.ovet, self.over_pos)
                if self.k == 100:
                    self.k = 1
                self.k = self.k + 1
                
            if (self.ball_pos[0] < -50 or self.ball_pos[0] > 530) and not self.over:
                if self.i >= 0 and self.i <= 50:
                    if self.i == 2:
                        pygame.mixer.Sound.play(self.countdown_sound)
                    self.redraw = True
                    self.spawn_text = self.spawn_font.render("3", True, "Yellow")
                    self.window.blit(self.spawn_text, (235, 208))
                elif self.i >= 100 and self.i <= 150:
                    if self.i == 102:
                        pygame.mixer.Sound.play(self.countdown_sound)
                    self.spawn_text = self.spawn_font.render("2", True, "Yellow")
                    self.window.blit(self.spawn_text, (235, 208))
                elif self.i >= 200 and self.i <= 250:
                    if self.i == 202:
                        pygame.mixer.Sound.play(self.countdown_sound)
                    self.spawn_text = self.spawn_font.render("1", True, "Yellow")
                    self.window.blit(self.spawn_text, (235, 208))
                elif self.i >= 275:
                    self.i = 0
                    self.ball_pos = (235, 208)
                    self.redraw = False
                    self.yvel = -random.randint(-self.y, self.y)
                self.i = self.i + 1
            else:
                if not self.over:
                    pygame.draw.circle(self.window, "Yellow", self.ball_pos, 10)
                
            if (self.ball_pos[1] < 20 or self.ball_pos[1] > 390) and self.i == 1 and not self.inAnimate and not self.redraw:
                pygame.mixer.Sound.play(self.beep_sound)
                self.yvel = -self.yvel
            self.ball_pos = (self.ball_pos[0] + self.xvel, self.ball_pos[1] + self.yvel)
            
            if not self.collision:
                if self.ball_pos[0] >= 50 and self.ball_pos[0] <= 54:
                    for x in range(int(self.ball_pos[1] - 10), int(self.ball_pos[1] + 10)):
                        for y in range(int(self.my_pos[1]), int(self.my_pos[1] + 100)):
                            if x == y:
                                self.collision = True
                                break
                if self.ball_pos[0] >= 430 and self.ball_pos[0] <= 434:
                    for x in range(int(self.ball_pos[1] - 10), int(self.ball_pos[1] + 10)):
                        for y in range(int(self.comp_pos[1]), int(self.comp_pos[1] + 100)):
                            if x == y:
                                self.collision = True
                                break
            
            if self.collision and self.i == 1:
                if self.yvel > 0:
                    self.xvel = -self.xvel
                    self.yvel = random.randint(1, self.y)
                else:
                    self.xvel = -self.xvel
                    self.yvel =  random.randint(1, self.y)
                    self.yvel = -self.yvel
                pygame.mixer.Sound.play(self.beep_sound)
                self.collision = False
            else:
                if not self.inAnimate and self.i == 1 and not self.over:
                    if self.ball_pos[0] <= -4 and self.ball_pos[0] >= -8:
                        self.comp_score = self.comp_score + 1
                        pygame.mixer.Sound.play(self.beep_sound)
                    if self.ball_pos[0] >= 484 and self.ball_pos[0] <= 488:
                        self.my_score = self.my_score + 1
                        pygame.mixer.Sound.play(self.beep_sound)
            
            if self.ball_pos[0] >= 60 and self.xvel > 0 and self.i == 1 and not self.inAnimate and not self.redraw:
                if self.ball_pos[1] + 10 < self.comp_pos[1]:
                    self.comp_pos = (self.comp_pos[0], self.comp_pos[1] - 6)
                if self.ball_pos[1] > self.comp_pos[1] + 100:
                    self.comp_pos = (self.comp_pos[0], self.comp_pos[1] + 6)
                        
            self.bar1_rect = pygame.Rect(self.comp_pos, self.bar_dim)
            self.bar2_rect = pygame.Rect(self.my_pos, self.bar_dim)
            pygame.draw.rect(self.window, "Red", self.bar1_rect, border_radius=15)
            pygame.draw.rect(self.window, "Blue", self.bar2_rect, border_radius=15)
            
            pygame.display.update()
            
            self.events =  pygame.event.get()
            for self.event in self.events:
                if self.event.type == pygame.KEYDOWN:
                    if self.over and not self.outAnimate:  
                        self.utils.play_music()
                        self.run = False
                        if self.over_pos[0] == 195:
                            Json.set_wins(Json.get_wins() + 1)
                        elif self.over_pos[0] == 192:
                            Json.set_losses(Json.get_losses() + 1)
                        else:
                            Json.set_draws(Json.get_draws() + 1)
                    if self.event.key == pygame.K_ESCAPE:
                        Json.set_animate(True)
                        Json.set_ball_pos((235, 208))
                        pygame.quit()
                        sys.exit()
                            
            if not self.inAnimate and self.i == 1 and not self.over:
                self.j = self.j + 1
                self.keys = pygame.key.get_pressed()
                if self.keys[pygame.K_UP] and self.my_pos[1] > 15:
                    self.my_pos = (25, self.my_pos[1] - 4) 
                elif self.keys[pygame.K_DOWN] and self.my_pos[1] < 295:
                    self.my_pos = (25, self.my_pos[1] + 4)
