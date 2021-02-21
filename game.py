import pygame
import random

from board import Board
pygame.init()
size = [700, 900]
screen = pygame.display.set_mode(size)


class Game:
    def __init__(self):
        self.board = Board(10, 20)
        self.board.set_view(50, 50, 40)
        self.figure = None
        self.color = None
        self.coords = None
        self.color_ = None
        self.position = None
        self.pause = False
        self.font = pygame.font.Font(None, 50)
        self.score = 0
        self.FPS = 10
        self.clock = pygame.time.Clock()
        self.draw = False
        self.lose = False
        self.board_ = [[0] * 10 for _ in range(20)]
        self.board_col = [[0] * 10 for _ in range(20)]

    def generate_figures(self):
        figures = ['O', 'I', 'L', 'J', 'S', 'Z', 'T']
        self.figure = random.choice(figures)
        self.position = 1

    def random_color(self):
        colors = ['blue', 'red', 'green', 'yellow', 'orange']
        col = {'blue': 2,
               'red': 3,
               'green': 4,
               'yellow': 5,
               'orange': 6}
        color = random.choice(colors)
        self.color_ = col[color]
        self.color = pygame.Color(color)

    def spawn(self):
        if self.figure == 'O':
            self.coords = [[0, 4], [0, 5], [1, 4], [1, 5]]
        if self.figure == 'I':
            self.coords = [[0, 3], [0, 4], [0, 5], [0, 6]]
        if self.figure == 'L':
            self.coords = [[0, 4], [1, 4], [2, 4], [2, 5]]
        if self.figure == 'J':
            self.coords = [[0, 5], [1, 5], [2, 5], [2, 4]]
        if self.figure == 'T':
            self.coords = [[0, 4], [1, 4], [2, 4], [1, 5]]
        if self.figure == 'Z':
            self.coords = [[0, 4], [0, 5], [1, 5], [1, 6]]
        if self.figure == 'S':
            self.coords = [[0, 4], [0, 5], [1, 3], [1, 4]]
        for elem in self.coords:
            x, y = elem
            self.board_[x][y] = 2
            self.board_col[x][y] = self.color_

    def render(self):
        screen.fill((55, 55, 55))
        self.board.render(screen, self.board_col, self.font, self.score, self.lose, self.pause)
        pygame.display.flip()

    def down(self):
        if self.check_down():
            for i in range(4):
                x, y = self.coords[i]
                self.board_[x][y] = 0
                self.board_col[x][y] = 0
                self.coords[i] = [x + 1, y]
            for i in range(4):
                x, y = self.coords[i]
                self.board_[x][y] = 2
                self.board_col[x][y] = self.color_
        else:
            for i in range(4):
                x, y = self.coords[i]
                self.board_[x][y] = 1
            self.draw = False

    def right(self):
        if self.check_right():
            for i in range(4):
                x, y = self.coords[i]
                self.board_[x][y] = 0
                self.board_col[x][y] = 0
                self.coords[i] = [x, y + 1]
            for i in range(4):
                x, y = self.coords[i]
                self.board_[x][y] = 2
                self.board_col[x][y] = self.color_

    def left(self):
        if self.check_left():
            for i in range(4):
                x, y = self.coords[i]
                self.board_[x][y] = 0
                self.board_col[x][y] = 0
                self.coords[i] = [x, y - 1]
            for i in range(4):
                x, y = self.coords[i]
                self.board_[x][y] = 2
                self.board_col[x][y] = self.color_

    def turn(self):
        if self.check_turn():
            if self.figure == 'I':
                if self.position == 1:
                    for i in range(4):
                        x, y = self.coords[i]
                        self.board_[x][y] = 0
                        self.board_col[x][y] = 0
                        self.coords[i] = [x + i, y - i]
                    self.position = 2
                elif self.position == 2:
                    for i in range(4):
                        x, y = self.coords[i]
                        self.board_[x][y] = 0
                        self.board_col[x][y] = 0
                        self.coords[i] = [x - i, y + i]
                    self.position = 1
            if self.figure == 'L':
                for i in range(4):
                    x, y = self.coords[i]
                    self.board_[x][y] = 0
                    self.board_col[x][y] = 0
                if self.position == 1:
                    x, y = self.coords[0]
                    self.coords[0] = [x, y + 2]
                    x, y = self.coords[1]
                    self.coords[1] = [x - 1, y + 1]
                    x, y = self.coords[2]
                    self.coords[2] = [x - 2, y]
                    x, y = self.coords[3]
                    self.coords[3] = [x - 1, y - 1]
                    self.position = 2
                elif self.position == 2:
                    x, y = self.coords[0]
                    self.coords[0] = [x + 2, y]
                    x, y = self.coords[1]
                    self.coords[1] = [x + 1, y + 1]
                    x, y = self.coords[2]
                    self.coords[2] = [x, y + 2]
                    x, y = self.coords[3]
                    self.coords[3] = [x - 1, y + 1]
                    self.position = 3
                elif self.position == 3:
                    x, y = self.coords[0]
                    self.coords[0] = [x, y - 2]
                    x, y = self.coords[1]
                    self.coords[1] = [x + 1, y - 1]
                    x, y = self.coords[2]
                    self.coords[2] = [x + 2, y]
                    x, y = self.coords[3]
                    self.coords[3] = [x + 1, y + 1]
                    self.position = 4
                elif self.position == 4:
                    x, y = self.coords[0]
                    self.coords[0] = [x - 2, y]
                    x, y = self.coords[1]
                    self.coords[1] = [x - 1, y - 1]
                    x, y = self.coords[2]
                    self.coords[2] = [x, y - 2]
                    x, y = self.coords[3]
                    self.coords[3] = [x + 1, y - 1]
                    self.position = 1
            if self.figure == 'J':
                for i in range(4):
                    x, y = self.coords[i]
                    self.board_[x][y] = 0
                    self.board_col[x][y] = 0
                if self.position == 1:
                    x, y = self.coords[0]
                    self.coords[0] = [x + 2, y - 1]
                    x, y = self.coords[1]
                    self.coords[1] = [x + 1, y]
                    x, y = self.coords[2]
                    self.coords[2] = [x, y - 2]
                    x, y = self.coords[3]
                    self.coords[3] = [x - 1, y - 1]
                    self.position = 2
                elif self.position == 2:
                    x, y = self.coords[0]
                    self.coords[0] = [x, y - 1]
                    x, y = self.coords[1]
                    self.coords[1] = [x - 1, y - 2]
                    x, y = self.coords[2]
                    self.coords[2] = [x - 2, y]
                    x, y = self.coords[3]
                    self.coords[3] = [x - 1, y + 1]
                    self.position = 3
                elif self.position == 3:
                    x, y = self.coords[0]
                    self.coords[0] = [x - 2, y]
                    x, y = self.coords[1]
                    self.coords[1] = [x - 1, y + 1]
                    x, y = self.coords[2]
                    self.coords[2] = [x, y + 2]
                    x, y = self.coords[3]
                    self.coords[3] = [x + 1, y + 1]
                    self.position = 4
                elif self.position == 4:
                    x, y = self.coords[0]
                    self.coords[0] = [x, y + 2]
                    x, y = self.coords[1]
                    self.coords[1] = [x + 1, y + 1]
                    x, y = self.coords[2]
                    self.coords[2] = [x + 2, y]
                    x, y = self.coords[3]
                    self.coords[3] = [x + 1, y - 1]
                    self.position = 1
            if self.figure == 'Z':
                for i in range(4):
                    x, y = self.coords[i]
                    self.board_[x][y] = 0
                    self.board_col[x][y] = 0
                if self.position == 1:
                    x, y = self.coords[0]
                    self.coords[0] = [x, y + 1]
                    x, y = self.coords[1]
                    self.coords[1] = [x + 1, y]
                    x, y = self.coords[2]
                    self.coords[2] = [x, y - 1]
                    x, y = self.coords[3]
                    self.coords[3] = [x + 1, y - 2]
                    self.position = 2
                elif self.position == 2:
                    x, y = self.coords[0]
                    self.coords[0] = [x, y - 1]
                    x, y = self.coords[1]
                    self.coords[1] = [x - 1, y]
                    x, y = self.coords[2]
                    self.coords[2] = [x, y + 1]
                    x, y = self.coords[3]
                    self.coords[3] = [x - 1, y + 2]
                    self.position = 1
            if self.figure == 'S':
                for i in range(4):
                    x, y = self.coords[i]
                    self.board_[x][y] = 0
                    self.board_col[x][y] = 0
                if self.position == 1:
                    x, y = self.coords[0]
                    self.coords[0] = [x, y - 1]
                    x, y = self.coords[1]
                    self.coords[1] = [x - 1, y - 2]
                    x, y = self.coords[2]
                    self.coords[2] = [x, y + 1]
                    x, y = self.coords[3]
                    self.coords[3] = [x - 1, y]
                    self.position = 2
                elif self.position == 2:
                    x, y = self.coords[0]
                    self.coords[0] = [x, y + 1]
                    x, y = self.coords[1]
                    self.coords[1] = [x + 1, y + 2]
                    x, y = self.coords[2]
                    self.coords[2] = [x, y - 1]
                    x, y = self.coords[3]
                    self.coords[3] = [x + 1, y]
                    self.position = 1
            if self.figure == 'T':
                for i in range(3):
                    x, y = self.coords[i]
                    self.board_[x][y] = 0
                    self.board_col[x][y] = 0
                if self.position == 1:
                    x, y = self.coords[0]
                    self.coords[0] = [x, y + 2]
                    x, y = self.coords[1]
                    self.coords[1] = [x - 1, y + 1]
                    x, y = self.coords[2]
                    self.coords[2] = [x - 2, y]
                    self.position = 2
                elif self.position == 2:
                    x, y = self.coords[0]
                    self.coords[0] = [x + 2, y]
                    x, y = self.coords[1]
                    self.coords[1] = [x + 1, y + 1]
                    x, y = self.coords[2]
                    self.coords[2] = [x, y + 2]
                    self.position = 3
                elif self.position == 3:
                    x, y = self.coords[0]
                    self.coords[0] = [x, y - 2]
                    x, y = self.coords[1]
                    self.coords[1] = [x + 1, y - 1]
                    x, y = self.coords[2]
                    self.coords[2] = [x + 2, y]
                    self.position = 4
                elif self.position == 4:
                    x, y = self.coords[0]
                    self.coords[0] = [x - 2, y]
                    x, y = self.coords[1]
                    self.coords[1] = [x - 1, y - 1]
                    x, y = self.coords[2]
                    self.coords[2] = [x, y - 2]
                    self.position = 1
            for i in range(4):
                x, y = self.coords[i]
                self.board_[x][y] = 2
                self.board_col[x][y] = self.color_

    def check_turn(self):
        if self.figure == 'O':
            return False
        if self.figure == 'I':
            for i in range(4):
                x, y = self.coords[i]
                if self.position == 1:
                    if x + 3 < 20:
                        if self.board_[x + i][y - i] == 1:
                            return False
                    else:
                        return False
                elif self.position == 2:
                    if y + 3 < 10:
                        if self.board_[x - i][y + i] == 1:
                            return False
                    else:
                        return False
            return True
        if self.figure == 'L':
            if self.position == 1:
                x, y = self.coords[0]
                if y + 2 < 10 and self.board_[x][y + 2] != 1:
                    x, y = self.coords[1]
                    if y + 1 < 10 and self.board_[x - 1][y + 1] != 1:
                        x, y = self.coords[2]
                        if self.board_[x - 2][y] != 1:
                            x, y = self.coords[3]
                            if self.board_[x - 1][y - 1] != 1 and y - 1 >= 0:
                                return True
            if self.position == 2:
                x, y = self.coords[0]
                if x + 2 < 20 and self.board_[x + 2][y] != 1:
                    x, y = self.coords[1]
                    if y + 1 < 10 and x + 1 < 20 and self.board_[x + 1][y + 1] != 1:
                        x, y = self.coords[2]
                        if y + 2 < 10 and self.board_[x][y + 2] != 1:
                            x, y = self.coords[3]
                            if y + 1 < 10 and self.board_[x - 1][y + 1] != 1:
                                return True
            if self.position == 3:
                x, y = self.coords[0]
                if self.board_[x][y - 2] != 1 and y - 2 >= 0:
                    x, y = self.coords[1]
                    if x + 1 < 20 and self.board_[x + 1][y - 1] != 1 and y - 1 >= 0:
                        x, y = self.coords[2]
                        if x + 2 < 20 and self.board_[x + 2][y] != 1:
                            x, y = self.coords[3]
                            if y + 1 < 10 and x + 1 < 20 and self.board_[x + 1][y + 1] != 1:
                                return True
            if self.position == 4:
                x, y = self.coords[0]
                if self.board_[x - 2][y] != 1:
                    x, y = self.coords[1]
                    if self.board_[x - 1][y - 1] != 1 and y - 1 >= 0:
                        x, y = self.coords[2]
                        if self.board_[x][y - 2] != 1 and y - 2 >= 0:
                            x, y = self.coords[3]
                            if x + 1 < 20 and self.board_[x + 1][y - 1] != 1 and y - 1 >= 0:
                                return True
        if self.figure == 'J':
            if self.position == 1:
                x, y = self.coords[0]
                if x + 2 < 20 and self.board_[x + 2][y - 1] != 1 and y - 1 >= 0:
                    x, y = self.coords[1]
                    if x + 1 < 20 and self.board_[x + 1][y] != 1:
                        x, y = self.coords[2]
                        if self.board_[x][y - 2] != 1 and y - 2 >= 0:
                            x, y = self.coords[3]
                            if self.board_[x - 1][y - 1] != 1 and y - 1 >= 0:
                                return True
            if self.position == 2:
                x, y = self.coords[0]
                if self.board_[x][y - 1] != 1 and y - 1 >= 0:
                    x, y = self.coords[1]
                    if self.board_[x - 1][y - 2] != 1 and y - 2 >= 0:
                        x, y = self.coords[2]
                        if self.board_[x - 2][y] != 1:
                            x, y = self.coords[3]
                            if y + 1 < 10 and self.board_[x - 1][y + 1] != 1:
                                return True
            if self.position == 3:
                x, y = self.coords[0]
                if self.board_[x - 2][y] != 1:
                    x, y = self.coords[1]
                    if y + 1 < 10 and self.board_[x - 1][y + 1] != 1:
                        x, y = self.coords[2]
                        if y + 2 < 10 and self.board_[x][y + 2] != 1:
                            x, y = self.coords[3]
                            if x + 1 < 20 and y + 1 < 10 and self.board_[x + 1][y + 1] != 1:
                                return True
            if self.position == 4:
                x, y = self.coords[0]
                if y + 2 < 10 and self.board_[x][y + 2] != 1:
                    x, y = self.coords[1]
                    if x + 1 < 20 and y + 1 < 10 and self.board_[x + 1][y + 1] != 1:
                        x, y = self.coords[2]
                        if x + 2 < 20 and self.board_[x + 2][y] != 1:
                            x, y = self.coords[3]
                            if x + 1 < 20 and self.board_[x + 1][y - 1] != 1 and y - 1 >= 0:
                                return True
        if self.figure == 'Z':
            if self.position == 1:
                x, y = self.coords[0]
                if y + 1 < 10 and self.board_[x][y + 1] != 1:
                    x, y = self.coords[1]
                    if x + 1 < 20 and self.board_[x + 1][y] != 1:
                        x, y = self.coords[2]
                        if self.board_[x][y - 1] != 1 and y - 1 >= 0:
                            x, y = self.coords[3]
                            if x + 1 < 20 and self.board_[x + 1][y - 2] != 1 and y - 2 >= 0:
                                return True
            if self.position == 2:
                x, y = self.coords[0]
                if self.board_[x][y - 1] != 1 and y - 1 >= 0:
                    x, y = self.coords[1]
                    if self.board_[x - 1][y] != 1:
                        x, y = self.coords[2]
                        if y + 1 < 10 and self.board_[x][y + 1] != 1:
                            x, y = self.coords[3]
                            if y + 2 < 10 and self.board_[x - 1][y + 2] != 1:
                                return True
        if self.figure == 'S':
            if self.position == 1:
                x, y = self.coords[0]
                if self.board_[x][y - 1] != 1 and y - 1 >= 0:
                    x, y = self.coords[1]
                    if self.board_[x - 1][y - 2] != 1 and x - 1 >= 0 and y - 2 >= 0:
                        x, y = self.coords[2]
                        if y + 1 < 10 and self.board_[x][y + 1] != 1:
                            x, y = self.coords[3]
                            if self.board_[x - 1][y] != 1:
                                return True
            if self.position == 2:
                x, y = self.coords[0]
                if y + 1 < 10 and self.board_[x][y + 1] != 1:
                    x, y = self.coords[1]
                    if y + 2 < 10 and x + 1 < 20 and self.board_[x + 1][y + 2] != 1:
                        x, y = self.coords[2]
                        if self.board_[x][y - 1] != 1 and y - 1 >= 0:
                            x, y = self.coords[3]
                            if x + 1 < 20 and self.board_[x + 1][y] != 1:
                                return True
        if self.figure == 'T':
            if self.position == 1:
                x, y = self.coords[0]
                if y + 2 < 10 and self.board_[x][y + 2] != 1:
                    x, y = self.coords[1]
                    if y + 1 < 10 and self.board_[x - 1][y + 1] != 1 and x - 1 >= 0:
                        x, y = self.coords[2]
                        if self.board_[x - 2][y] != 1 and x - 2 >= 0:
                            return True
            if self.position == 2:
                x, y = self.coords[0]
                if x + 2 < 20 and self.board_[x + 2][y] != 1:
                    x, y = self.coords[1]
                    if x + 1 < 20 and y + 1 < 10 and self.board_[x + 1][y + 1] != 1:
                        x, y = self.coords[2]
                        if y + 2 < 10 and self.board_[x][y + 2] != 1:
                            return True
            if self.position == 3:
                x, y = self.coords[0]
                if self.board_[x][y - 2] != 1 and y - 2 >= 0:
                    x, y = self.coords[1]
                    if x + 1 < 20 and self.board_[x + 1][y - 1] != 1 and y - 1 >= 0:
                        x, y = self.coords[2]
                        if x + 2 < 20 and self.board_[x + 2][y] != 1:
                            return True
            if self.position == 4:
                x, y = self.coords[0]
                if self.board_[x - 2][y] != 1 and x - 2 >= 0:
                    x, y = self.coords[1]
                    if self.board_[x - 1][y - 1] != 1 and x - 1 >= 0 and y - 1 >= 0:
                        x, y = self.coords[2]
                        if self.board_[x][y - 2] != 1 and y - 2 >= 0:
                            return True
        return False

    def check_left(self):
        for i in range(4):
            x, y = self.coords[i]
            if y - 1 < 0:
                return False
            if self.board_[x][y - 1] == 1:
                return False
        return True

    def check_right(self):
        for i in range(4):
            x, y = self.coords[i]
            if y + 1 > 9:
                return False
            if self.board_[x][y + 1] == 1:
                return False
        return True

    def check_down(self):
        for i in range(4):
            x, y = self.coords[i]
            if x + 1 > 19:
                return False
            if self.board_[x + 1][y] == 1:
                return False
        return True

    def check_win(self):
        winners = []
        for i in range(20):
            k = 0
            for j in range(10):
                if self.board_[i][j] == 1:
                    k += 1
            if k == 10:
                winners.append(i)
            k = 0
        for elem in winners:
            for i in range(elem):
                self.board_[elem - i] = self.board_[elem - i - 1]
                self.board_col[elem - i] = self.board_col[elem - i - 1]
            self.board_[0] = [0 for i in range(10)]
            self.board_col[0] = [0 for i in range(10)]
            self.score += 10

    def check_lose(self):
        for i in range(10):
            if self.board_[0][i] == 1:
                self.lose = True

    def main(self):
        i = 0
        pygame.mixer.music.load('music.mp3')
        pygame.mixer.music.play(loops=-1)
        pygame.mixer.music.set_volume(0.1)
        while True:
            self.render()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return False
                if event.type == pygame.KEYDOWN:
                    if not self.pause:
                        if event.key == pygame.K_DOWN:
                            self.down()
                        if event.key == pygame.K_RIGHT:
                            self.right()
                        if event.key == pygame.K_LEFT:
                            self.left()
                        if event.key == pygame.K_SPACE:
                            self.turn()
                    if event.key == pygame.K_ESCAPE:
                        if self.pause:
                            self.pause = False
                        else:
                            self.pause = True
            if not self.pause:
                if not self.lose:
                    if not self.draw:
                        self.random_color()
                        self.generate_figures()
                        self.spawn()
                        self.draw = True
                    self.clock.tick(self.FPS)
                    if i % 10 == 0:
                        self.down()
                    self.check_win()
                    self.check_lose()
                    i += 1
            else:
                self.render()


a = Game()
a.main()
