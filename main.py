import pygame

from Point import Point
from PointList import PointList
from features import random_coords
from settings import FPS, WINDOW_SIZE, BLACK


def pause(clock):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.update()
        clock.tick(FPS)


def run(screen, clock, plist):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pause(clock)

        # логика
        plist.move_points()

        # отрисовка
        screen.fill(BLACK)
        plist.connect_points()
        plist.draw_points()

        # обновление
        pygame.display.update()
        clock.tick(FPS)
        print(clock.get_fps())


def main():
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption('Точки')
    clock = pygame.time.Clock()

    plist = PointList([Point(*random_coords()) for _ in range(10)], screen)

    run(screen, clock, plist)


if __name__ == '__main__':
    main()
