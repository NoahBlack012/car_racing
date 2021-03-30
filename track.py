import pygame
from colors import Colors
class Track:
    def __init__(self, roads):
        self.roads = roads
        self.colors = Colors()

    def draw_vert_finish_line(self, screen):

        x_val = self.roads[-1].corners[-1][0]
        y_val = max([self.roads[-1].corners[-1][-1], self.roads[-1].corners[-2][-1]])
        n = 0
        for x in range(x_val, x_val + 20, 5):
            if n % 2 == 0:
                col_val = 0
            else:
                col_val = 1
            for y in range(y_val - 10, y_val - 150, -5):
                if col_val % 2 == 0:
                    col = self.colors.WHITE
                else:
                    col = self.colors.BLACK
                pygame.draw.rect(screen, col, [x, y, 5, 5])
                col_val += 1
            n += 1

    def draw(self, screen):
        for road in self.roads:
            road.draw(screen)
        self.draw_vert_finish_line(screen)
