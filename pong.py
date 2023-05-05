import pygame
from data import *
from random import *
import time
import json


class Board(pygame.Rect):
    def __init__(self, x, y, width, height, image= None, speed= 5):
        super().__init__(x, y, width, height)
        self.IMAGE = image
        self.SPEED = speed
        self.MOVE = {"UP": False, "DOWN": False}
    
    def move(self):
        if self.MOVE["UP"] and self.y > 0:
            self.y -= self.SPEED
        elif self.MOVE["DOWN"] and self.y < setting_win["HEIGHT"] - setting_board["HEIGHT"]:
            self.y += self.SPEED

class Point():
    def __init__(self, name_left, name_right):
        self.NAME_LEFT = name_left
        self.NAME_RIGHT = name_right
        self.LEFT_POINT = 0
        self.RIGHT_POINT = 0
        self.FONT = pygame.font.Font(None, 40)
    
    def blit_point(self, window):
        window.blit(self.FONT.render(f"{self.LEFT_POINT} : {self.RIGHT_POINT}", True, (200,255,255)), (setting_win["WIDTH"] // 2 - 50, 10))

class Ball():
    def __init__(self, x, y, radius, image= None, speed= 5):
        self.X = x
        self.Y = y
        self.RADIUS = radius
        self.RECT = pygame.Rect(x - radius, y - radius, (radius ** 2 + radius ** 2) ** 0.5, (radius ** 2 + radius ** 2) ** 0.5)
        self.IMAGE = image
        self.SPEED = choice([-speed, speed])
        self.CONST = speed
        self.ANGLE = 0
        self.POINT = Point("left", "right")
        self.a = {-1}

    def make_angle(self, ang):
        if self.SPEED < 0:
            self.SPEED = - self.CONST
        elif self.SPEED > 0:
            self.SPEED = self.CONST
        self.ANGLE = ang * uniform(abs(self.SPEED // 2), abs(self.SPEED))
        coff = abs(self.SPEED) / abs((self.SPEED ** 2 + self.ANGLE ** 2) ** 0.5)
        #print("1",self.ANGLE, self.SPEED, coff)
        self.ANGLE *= coff
        self.SPEED *= coff
        #print("2",self.ANGLE, self.SPEED)

    def restart(self, board_left, board_right, window):
        if self.POINT.LEFT_POINT == 1 or self.POINT.RIGHT_POINT == 1:
            history[str(time.time())] = {self.POINT.NAME_LEFT: self.POINT.LEFT_POINT, self.POINT.NAME_RIGHT: self.POINT.RIGHT_POINT}
            with open("history.json", "w", encoding= "utf-8") as file:
                json.dump(history, file, indent= 4)

        self.SPEED = choice([-self.CONST, self.CONST])
        self.ANGLE = 0
        self.X, self.Y = restart["RESTART_BALL"]
        self.RECT.center = restart["RESTART_BALL"]
        board_left.y = restart["RESTART_BOARD_LEFT"][1]
        board_right.y = restart["RESTART_BOARD_RIGHT"][1]
        window.fill((0,0,0))
        pygame.draw.rect(window, (255,255,255), board_left)
        pygame.draw.rect(window, (255,255,255), board_right)
        pygame.draw.circle(window, (255, 255, 255), self.RECT.center, self.RADIUS)
        self.POINT.blit_point(window)
        pygame.display.flip()
        time.sleep(2)

    def move(self, board_left, board_right, window):
        if self.X - self.RADIUS <= 0:
            self.POINT.RIGHT_POINT += 1
            self.restart(board_left, board_right, window)
        elif self.X + self.RADIUS >= setting_win["WIDTH"]:
            self.POINT.LEFT_POINT += 1
            self.restart(board_left, board_right, window)
        
        if self.Y - self.RADIUS <= 0 or self.Y + self.RADIUS >= setting_win["HEIGHT"]:
            self.ANGLE *= -1
        elif board_left.collidepoint(self.X - self.RADIUS, self.Y) or board_left.colliderect(self.RECT):
            self.SPEED *= -1
            if board_left.MOVE["UP"]:
                #self.ANGLE = - uniform(abs(self.SPEED // 2), abs(self.SPEED))
                self.make_angle(-1)
            elif board_left.MOVE["DOWN"]:
                self.make_angle(1)
                #self.ANGLE = uniform(abs(self.SPEED // 2), abs(self.SPEED))
        elif board_right.collidepoint(self.X + self.RADIUS, self.Y) or board_right.colliderect(self.RECT):
            self.SPEED *= -1
            if board_right.MOVE["UP"]:
                self.make_angle(-1)
                #self.ANGLE = - uniform(abs(self.SPEED // 2), abs(self.SPEED))
            elif board_right.MOVE["DOWN"]:
                self.make_angle(1)
                #self.ANGLE = uniform(abs(self.SPEED)// 2, abs(self.SPEED))
        
        self.Y += self.ANGLE
        self.RECT.y = self.Y
        self.X += self.SPEED
        self.RECT.x = self.X
        #print(self.X - self.CONST, self.Y - self.CONST, self.RECT.x, self.RECT.y)
        #print((self.SPEED ** 2 + self.ANGLE ** 2) ** 0.5)
        self.a.add((self.SPEED ** 2 + self.ANGLE ** 2) ** 0.5)

class Menu():
    def __init__(self, width, height, count):
        #super().__init__(x, y, width, height)
        self.BUTTONS = list()
        self.width = width
        self.height  = height
        self.count = count
        self.FONT = pygame.font.SysFont("Comic Sans MS", 40)
        for button in range(count):
            self.BUTTONS.append(pygame.Rect(setting_win["WIDTH"] // 2 - width // 2,
                                            setting_win["HEIGHT"] // 2 - count * ((height + 15) // 2 ) + (height + 15) * button,
                                            width,
                                            height))
        
    def draw_menu(self, window):
        window.fill((255,255,200))
        for button in self.BUTTONS:
            pygame.draw.rect(window, (100,130,200), button)
        window.blit(self.FONT.render("Start", True, (0,0,0)), 
        (setting_win["WIDTH"] // 2 - self.width // 2 + 50, setting_win["HEIGHT"] // 2 - self.count * ((self.height + 15) // 2 ) + (self.height + 15) * 0 - 7))
        window.blit(self.FONT.render("Mode", True, (0,0,0)), 
        (setting_win["WIDTH"] // 2 - self.width // 2 + 50, setting_win["HEIGHT"] // 2 - self.count * ((self.height + 15) // 2 ) + (self.height + 15) * 1 - 7))
        window.blit(self.FONT.render("History", True, (0,0,0)), 
        (setting_win["WIDTH"] // 2 - self.width // 2 + 30, setting_win["HEIGHT"] // 2 - self.count * ((self.height + 15) // 2 ) + (self.height + 15) * 2 - 7))
        window.blit(self.FONT.render("Exit", True, (0,0,0)), 
        (setting_win["WIDTH"] // 2 - self.width // 2 + 58, setting_win["HEIGHT"] // 2 - self.count * ((self.height + 15) // 2 ) + (self.height + 15) * 3 - 7))

    
    def click(self, cord):
        if self.BUTTONS[0].collidepoint(cord):
            return 1
        if self.BUTTONS[2].collidepoint(cord):
            return 3
        
        return 0
    
    def show_history(self, window):
        window.fill((255,255,200))
        font = pygame.font.Font(None, 25)
        y= 10
        x = 50
        for key_main  in history.keys():
            window.blit(font.render(f"-", True, (0,0,0)), (225, y))
            for key, value in zip(history[key_main].keys(), history[key_main].values()):
                window.blit(font.render(f"{key} : {value}", True, (0,0,0)), (x, y))
                x += 300
            x = 50
            y += 50


