import math
import pygame
from colors import Colors
class Car:
    def __init__(self, x, y):
        self.speed = 0
        self.x = x
        self.y = y
        self.angle = 90
        self.accel = 0
        self.max_speed = 100
        self.colors = Colors()
        self.col = self.colors.BLUE

        self.WIDTH = 80
        self.HEIGHT = 100

    def move(self):
        self.x = self.x + math.cos(math.radians(self.angle)) * self.speed
        self.y = self.y + math.sin(math.radians(self.angle)) * self.speed

    def draw(self, screen, image):
        topleft = (self.x, self.y)
        rotated_image = pygame.transform.rotate(image, -self.angle)
        new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)
        screen.blit(rotated_image, new_rect.topleft)


    def get_speed(self, accelerating, braking):
        if accelerating and braking:
            accelerating = False

        if not accelerating and not braking:
            self.accel = 0

        if accelerating and self.time_accel == 0:
            self.accel = 30
        elif accelerating:
            self.accel -= 3


        if braking:
            self.accel = -10

        if self.speed > self.max_speed:
            self.speed = self.max_speed

        self.speed += self.accel
