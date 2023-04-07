import pygame
from data import *

pygame.init()

window = pygame.display.set_mode((setting_win["WIDTH"], setting_win["HEIGHT"]))
pygame.display.set_caption("Ping Pong")

def run():
    game = True

    board = pygame.Rect(15, 
                        setting_win["HEIGHT"] // 2 - setting_board["HEIGHT"] // 2,
                        setting_board["WIDTH"],
                        setting_board["HEIGHT"])

    while game:
        window.fill((0,0,0))
        pygame.draw.rect(window, (255,255,255), board)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False

        pygame.display.flip()


run()