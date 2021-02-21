import pygame


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen, board, font, score, lose, pause):
        for i in range(self.width):
            for j in range(self.height):
                pygame.draw.rect(screen, (255, 255, 255), [self.cell_size * i + self.top,
                                                           self.cell_size * j + self.left,
                                                           self.cell_size,
                                                           self.cell_size], 1)
                if board[j][i] == 2:
                    pygame.draw.rect(screen, (0, 0, 255), [self.cell_size * i + self.top,
                                                           self.cell_size * j + self.left,
                                                           self.cell_size,
                                                           self.cell_size])
                if board[j][i] == 3:
                    pygame.draw.rect(screen, (255, 0, 0), [self.cell_size * i + self.top,
                                                           self.cell_size * j + self.left,
                                                             self.cell_size,
                                                             self.cell_size])
                if board[j][i] == 4:
                    pygame.draw.rect(screen, (0, 255, 0), [self.cell_size * i + self.top,
                                                             self.cell_size * j + self.left,
                                                             self.cell_size,
                                                             self.cell_size])
                if board[j][i] == 5:
                    pygame.draw.rect(screen, (255, 255, 0), [self.cell_size * i + self.top,
                                                             self.cell_size * j + self.left,
                                                             self.cell_size,
                                                             self.cell_size])
                if board[j][i] == 6:
                    pygame.draw.rect(screen, (255, 165, 0), [self.cell_size * i + self.top,
                                                             self.cell_size * j + self.left,
                                                             self.cell_size,
                                                             self.cell_size])
        text = font.render(str(score), 1, (230, 230, 250))
        text_x = 460
        text_y = 50
        screen.blit(text, (text_x, text_y))
        if lose:
            font = pygame.font.Font(None, 150)
            text_ = font.render('END GAME', 1, (255, 0, 0))
            text_x = 60
            text_y = 350
            screen.blit(text_, (text_x, text_y))
        elif pause:
            font = pygame.font.Font(None, 150)
            text_ = font.render('PAUSE', 1, (255, 255, 255))
            text_x = 60
            text_y = 350
            screen.blit(text_, (text_x, text_y))