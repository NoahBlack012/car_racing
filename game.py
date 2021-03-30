import pygame
import sys
from colors import Colors
from car import Car
from road import Road
from track import Track

class Game:
    def __init__(self):
        pygame.init()
        self.colors = Colors()
        self.corners = [
            [(5, 775), (155, 775), (155, 5), (5, 5)],
            [(155, 5), (155, 155), (300, 155), (300, 5)],
            [(300, 5), (450, 5), (450, 600), (300, 600)],
            [(450, 450), (450, 600), (800, 600), (800, 450)],
            [(650, 450), (800, 450), (800, 250), (650, 250)],
            [(650, 400), (650, 250), (500, 250), (500, 400)],
            [(500, 250), (650, 250), (650, 50), (500, 50)],
            [(650, 50), (650, 200), (1150, 200), (1150, 50)],
            [(1150, 200), (1000, 200), (1000, 775), (1150, 775)],
            [(1000, 775), (1000, 625), (155, 625), (155, 775)],
        ]

        self.roads = [Road(i) for i in self.corners]

        self.track = Track(self.roads)
        self.starting_pos = [(self.roads[0].corners[0][0] + self.roads[0].corners[1][0]) // 2, self.roads[0].corners[0][1] - 100]
        self.car = Car(self.starting_pos[0], self.starting_pos[1])


        self.WIDTH = 1200
        self.HEIGHT = 800
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Racing Game")
        self.clock = pygame.time.Clock()
        self.FPS = 30

        self.moving_left = False
        self.moving_right = False
        self.accelerating = False
        self.braking = False

        self.car_img = pygame.image.load('car.png')
        self.car_img = pygame.transform.scale(self.car_img, (66, 28))
        self.font = pygame.font.Font('freesansbold.ttf', 40)
        self.seconds = 0
        self.frames = 0

    def run(self):
        while True:
            self.clock.tick(self.FPS)
            self.frames += 1
            if self.frames % self.FPS == 0:
                self.seconds += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.moving_left = True
                    if event.key == pygame.K_RIGHT:
                        self.moving_right = True
                    if event.key == pygame.K_UP:
                        self.accelerating = True
                    if event.key == pygame.K_DOWN:
                        self.braking = True

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.moving_left = False
                    if event.key == pygame.K_RIGHT:
                        self.moving_right = False
                    if event.key == pygame.K_UP:
                        self.accelerating = False
                    if event.key == pygame.K_DOWN:
                        self.braking = False


            if self.moving_left:
                self.car.angle -= 5

            if self.moving_right:
                self.car.angle += 5

            if self.car.center[1] < 0:
                self.car.y = 0
                self.car.speed = 0
                self.seconds = 0

            if self.car.center[1] > self.HEIGHT:
                self.car.y = self.HEIGHT - self.car.HEIGHT
                self.car.speed = 0
                self.seconds = 0

            if self.car.center[0] < 0:
                self.car.x = 0
                self.car.speed = 0
                self.seconds = 0

            if self.car.center[0] > self.WIDTH:
                self.car.x = self.WIDTH - self.car.WIDTH
                self.car.speed = 0
                self.seconds = 0


            if not self.car.check_in_track(self.corners):
                self.car.x = self.starting_pos[0]
                self.car.y = self.starting_pos[1]
                self.car.speed = 0
                self.car.angle = -90
                self.seconds = 0

            y_vals = [self.roads[-1].corners[-1][-1], self.roads[-1].corners[-2][-1]]
            y_vals.sort()
            x_val = self.roads[-1].corners[-1][0]
            if self.car.x >= x_val - 5 and self.car.x <= x_val + 5 and self.car.y >= y_vals[0] and self.car.y <= y_vals[1]:
                print (self.seconds)
                self.seconds = 0


            self.car.get_speed(self.accelerating, self.braking)
            self.car.get_center()
            self.car.move()

            self.screen.fill(self.colors.BLACK)
            self.track.draw(self.screen)
            self.car.draw(self.screen, self.car_img)


            time = self.font.render(str(self.seconds), False, self.colors.BLACK)
            self.screen.blit(time, (self.WIDTH//2, self.HEIGHT - 150))
            pygame.display.flip()

if __name__ == '__main__':
    g = Game()
    g.run()
