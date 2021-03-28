import pygame
import sys
from colors import Colors
from car import Car
from road import Road

class Game:
    def __init__(self):
        pygame.init()
        self.colors = Colors()
        #self.car = Car()
        self.road = Road([(10, 10), (400, 600), (600, 600), (210, 10)])
        self.car = Car(400, 400)

        self.WIDTH = self.HEIGHT = 800
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Racing Game")
        self.clock = pygame.time.Clock()
        self.FPS = 30

        self.moving_left = False
        self.moving_right = False

        self.car_img = pygame.image.load('car.png')
        self.car_img = pygame.transform.scale(self.car_img, (66, 28))

    def run(self):
        while True:
            self.clock.tick(self.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.moving_left = True
                    if event.key == pygame.K_RIGHT:
                        self.moving_right = True

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.moving_left = False
                    if event.key == pygame.K_RIGHT:
                        self.moving_right = False

            if self.moving_left:
                self.car.angle -= 5

            if self.moving_right:
                self.car.angle += 5

            self.car.move()

            self.screen.fill(self.colors.WHITE)
            self.road.draw(self.screen)
            self.car.draw(self.screen, self.car_img)
            pygame.display.flip()

if __name__ == '__main__':
    g = Game()
    g.run()
