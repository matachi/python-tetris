#!/usr/bin/python3

import sys
import pygame

import blocks
import game

tetris = game.Game()

# Block colors
colors = {1: (255, 0, 0), 2: (0, 255, 0), 3: (0, 0, 255), 4: (255, 255, 0),
    5: (0, 255, 255), 6: (255, 0, 255)}

def main():
    block = blocks.Block6()

    # Initialize the screen
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption('Tetris')

    # A tetris tile
    rect = pygame.Surface((50, 50)).convert()

    gameMap = initGameMap()

    lastTick = pygame.time.get_ticks()
    #i = 0
    while 1:
        newTick = pygame.time.get_ticks()
        diff = newTick - lastTick
        lastTick = newTick
        update(diff)
        #render()

        screen.fill((0, 0, 0))

        drawBlock(screen, rect, tetris.getGameMap(), (0, 0))
        drawBlock(screen, rect, tetris.getBlock().getRotatedShape(),
                  tetris.getPosition())

        pygame.display.flip()
        pygame.time.wait(10)

        #i += 1
        #if i % 100 == 0:
        #    print(i)


def update(time):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                tetris.moveLeft()
            elif event.key == pygame.K_RIGHT:
                tetris.moveRight()
            elif event.key == pygame.K_UP:
                tetris.rotate()
    tetris.update(time)


def render():
    pass


def initGameMap():
    gameMap = []
    for y in range(10):
        gameMap.append([])
        for x in range(10):
            gameMap[y].append(0)
    return gameMap


def drawBlock(screen, rect, shape, position):
    for y in range(len(shape)):
        for x in range(len(shape[0])):
            if not shape[y][x] == 0:
                rect.fill(colors[shape[y][x]])
                screen.blit(rect, (50 * (x + position[0]), 50 * (y + position[1])))


if __name__ == '__main__':
    main()
