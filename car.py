import math
import pygame
from colors import Colors
class Car:
    def __init__(self, x, y):
        self.speed = 0
        self.x = x
        self.y = y
        self.angle = -90
        self.accel = 0
        self.max_speed = 20
        self.colors = Colors()
        self.col = self.colors.BLUE
        self.past_accel = False

        self.WIDTH = 66
        self.HEIGHT = 28
        self.center = [self.x + self.WIDTH // 2, self.y + self.HEIGHT // 2]


    def move(self):
        self.x = self.x + math.cos(math.radians(self.angle)) * self.speed
        self.y = self.y + math.sin(math.radians(self.angle)) * self.speed

    def get_center(self):
        self.center = [self.x + self.WIDTH // 2, self.y + self.HEIGHT // 2]

    def draw(self, screen, image):
        topleft = (self.x, self.y)
        rotated_image = pygame.transform.rotate(image, -self.angle)
        new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)
        screen.blit(rotated_image, new_rect.topleft)

    def check_in_track(self, corners):
        for corner in corners:
            x_min = min([i[0] for i in corner])
            x_max = max([i[0] for i in corner])
            y_min = min([i[1] for i in corner])
            y_max = max([i[1] for i in corner])

            if self.center[0] > x_min and self.center[0] < x_max and self.center[1] > y_min and self.center[1] < y_max:
                return True
        return False


    def get_speed(self, accelerating, braking):
        if accelerating and braking:
            accelerating = False

        if not accelerating and not braking:
            self.accel = 0

        if not accelerating:
            self.past_accel = False

        if accelerating and not self.past_accel:
            self.accel = 2
            self.past_accel = True
        elif accelerating and self.accel <= 0:
            self.accel = 0
            self.past_accel = False
        elif accelerating and self.past_accel:
            self.accel -= 0.01

        if braking:
            self.accel = -3

        if self.speed > self.max_speed:
            self.speed = self.max_speed
            self.accel = 0

        self.speed += self.accel
        if self.speed <= 0:
            self.speed = 0
