import pygame
from colors import Colors

class Road:
    def __init__(self, corners):
        self.corners = corners
        #self.angle = angle
        self.colors = Colors()
        self.col = self.colors.WHITE

    def draw(self, screen):
        pygame.draw.polygon(screen, self.col, self.corners)

    def check_collision(self, car):
        pass
