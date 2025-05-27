
import pygame
import sys
import math

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Latihan Memandu (Web)")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 28)
WHITE, RED, BLUE = (255,255,255), (255,0,0), (0,0,255)

class Car:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.angle, self.speed = 0, 0

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]: self.speed = min(self.speed + 0.1, 3)
        elif keys[pygame.K_DOWN]: self.speed = max(self.speed - 0.1, -1.5)
        else: self.speed *= 0.95
        if keys[pygame.K_LEFT]: self.angle += 3
        if keys[pygame.K_RIGHT]: self.angle -= 3
        rad = math.radians(self.angle)
        self.x += self.speed * math.cos(rad)
        self.y -= self.speed * math.sin(rad)

    def draw(self):
        surf = pygame.Surface((40, 20), pygame.SRCALPHA)
        pygame.draw.polygon(surf, BLUE, [(0,0),(40,10),(0,20)])
        rotated = pygame.transform.rotate(surf, self.angle)
        rect = rotated.get_rect(center=(self.x, self.y))
        screen.blit(rotated, rect)

car = Car(100, 500)

def main():
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit(); sys.exit()
        screen.fill(WHITE)
        car.move()
        car.draw()
        pygame.display.flip()
        clock.tick(60)

main()
