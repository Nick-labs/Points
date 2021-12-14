import pygame
import random

from Rays.settings import WHITE, WINDOW_WIDTH, WINDOW_HEIGHT


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dx = random.choice((-1, 1))
        self.dy = random.choice((-1, 1))

        self.color = None
        self.line_color = [random.randint(128, 255)] * 3
        # self.line_color = random.choice((RED, GREEN, BLUE))

    @property
    def pos(self) -> (int, int):
        return self.x, self.y

    def move(self):
        self.x += self.dx
        self.y += self.dy

        if self.x <= 0:
            self.x = 0
            self.dx *= -1

        if self.x >= WINDOW_WIDTH:
            self.x = WINDOW_WIDTH
            self.dx *= -1

        if self.y <= 0:
            self.y = 0
            self.dy *= -1

        if self.y >= WINDOW_HEIGHT:
            self.y = WINDOW_HEIGHT
            self.dy *= -1

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, self.pos, 3)

    def connect(self, p, screen):
        pygame.draw.line(screen, self.line_color, self.pos, p.pos)
        # pygame.draw.line(screen, random.choice((RED, GREEN, BLUE)), self.pos, p.pos)
