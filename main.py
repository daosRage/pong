import pygame
from data import *
from pong import *

pygame.init()

window = pygame.display.set_mode((setting_win["WIDTH"], setting_win["HEIGHT"]))
pygame.display.set_caption("Ping Pong")
ball = Ball(    setting_win["WIDTH"] // 2 - setting_ball["RADIUS"],
                    setting_win["HEIGHT"] // 2 - setting_ball["RADIUS"],
                    setting_ball["RADIUS"]
    )
def run():
    game = True

    clock = pygame.time.Clock()
    board_left = Board(     15, 
                            setting_win["HEIGHT"] // 2 - setting_board["HEIGHT"] // 2,
                            setting_board["WIDTH"],
                            setting_board["HEIGHT"],)
    board_right = Board(    setting_win["WIDTH"] - setting_board["WIDTH"] - 15, 
                            setting_win["HEIGHT"] // 2 - setting_board["HEIGHT"] // 2,
                            setting_board["WIDTH"],
                            setting_board["HEIGHT"],)
    
    print(ball.SPEED)
    while game:
        window.fill((0,0,0))
        pygame.draw.rect(window, (255,255,255), board_left)
        pygame.draw.rect(window, (255,255,255), board_right)
        pygame.draw.circle(window, (255, 255, 255), ball.RECT.center, ball.RADIUS)
        board_left.move()
        board_right.move()
        ball.move(board_left, board_right, window)
        ball.POINT.blit_point(window)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    board_left.MOVE["UP"] = True
                if event.key == pygame.K_s:
                    board_left.MOVE["DOWN"] = True
                if event.key == pygame.K_UP:
                    board_right.MOVE["UP"] = True
                if event.key == pygame.K_DOWN:
                    board_right.MOVE["DOWN"] = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    board_left.MOVE["UP"] = False
                if event.key == pygame.K_s:
                    board_left.MOVE["DOWN"] = False
                if event.key == pygame.K_UP:
                    board_right.MOVE["UP"] = False
                if event.key == pygame.K_DOWN:
                    board_right.MOVE["DOWN"] = False

        clock.tick(90)
        pygame.display.flip()


run()
print(ball.a)