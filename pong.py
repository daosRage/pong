import pygame
from data import *
from random import *


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

class Ball():
    def __init__(self, x, y, radius, image= None, speed= 5):
        self.X = x
        self.Y = y
        self.RADIUS = radius
        self.IMAGE = image
        self.SPEED = choice([-speed, speed])
        self.CONST = speed
        self.ANGLE = 0
        self.a = {-1}

    def make_angle(self, ang):
        if self.SPEED < 0:
            self.SPEED = - self.CONST
        elif self.SPEED > 0:
            self.SPEED = self.CONST
        self.ANGLE = ang * uniform(abs(self.SPEED // 2), abs(self.SPEED))
        coff = abs(self.SPEED) / abs((self.SPEED ** 2 + self.ANGLE ** 2) ** 0.5)
        print("1",self.ANGLE, self.SPEED, coff)
        self.ANGLE *= coff
        self.SPEED *= coff
        print("2",self.ANGLE, self.SPEED)

    def move(self, board_left, board_right):
        
        if self.Y - self.RADIUS <= 0 or self.Y + self.RADIUS >= setting_win["HEIGHT"]:
            self.ANGLE *= -1
        elif board_left.collidepoint(self.X - self.RADIUS, self.Y):
            self.SPEED *= -1
            if board_left.MOVE["UP"]:
                #self.ANGLE = - uniform(abs(self.SPEED // 2), abs(self.SPEED))
                self.make_angle(-1)
            elif board_left.MOVE["DOWN"]:
                self.make_angle(1)
                #self.ANGLE = uniform(abs(self.SPEED // 2), abs(self.SPEED))
        elif board_right.collidepoint(self.X + self.RADIUS, self.Y):
            self.SPEED *= -1
            if board_right.MOVE["UP"]:
                self.make_angle(-1)
                #self.ANGLE = - uniform(abs(self.SPEED // 2), abs(self.SPEED))
            elif board_right.MOVE["DOWN"]:
                self.make_angle(1)
                #self.ANGLE = uniform(abs(self.SPEED)// 2, abs(self.SPEED))
        
        self.Y += self.ANGLE
        self.X += self.SPEED
        print((self.SPEED ** 2 + self.ANGLE ** 2) ** 0.5)
        self.a.add((self.SPEED ** 2 + self.ANGLE ** 2) ** 0.5)
