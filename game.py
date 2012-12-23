import random
import blocks


class Game:

    WIDTH = 10
    HEIGHT = 10

    def __init__(self):
        self._gameMap = self.__initGameMap()
        self._currentBlock = self.__makeRandomBlock()
        self._position = [4, 0]
        self._timeCounter = 0

    def __initGameMap(self):
        gameMap = []
        for y in range(10):
            gameMap.append([])
            for x in range(10):
                gameMap[y].append(0)
        return gameMap

    def __makeRandomBlock(self):
        rand = random.randint(1, 6)
        if rand == 1:
            return blocks.Block1()
        elif rand == 2:
            return blocks.Block2()
        elif rand == 3:
            return blocks.Block3()
        elif rand == 4:
            return blocks.Block4()
        elif rand == 5:
            return blocks.Block5()
        elif rand == 6:
            return blocks.Block6()

    def __addBlockToGameMap(self):
        """Takes the current block (which the player moves) and adds it to the
        game map, making it a part of the "environment".
        """
        for y in range(self._currentBlock.getHeight()):
            for x in range(self._currentBlock.getWidth()):
                value = self._currentBlock.getRotatedShape()[y][x]
                if value is 0:  # Avoid overwriting nonzero numbers in gameMap
                    continue
                y2 = self._position[1] + y
                x2 = self._position[0] + x
                self._gameMap[y2][x2] = value

    def __doesBlockCollide(self):
        for y in range(self._currentBlock.getHeight()):
            for x in range(self._currentBlock.getWidth()):
                shapeValue = self._currentBlock.getRotatedShape()[y][x]
                y2 = self._position[1] + y
                x2 = self._position[0] + x
                mapValue = self._gameMap[y2][x2]
                if shapeValue and mapValue:
                    return True
        return False

    def update(self, time):
        self._timeCounter += time
        if self._timeCounter < 1000:  # Only move down block every 1 second
            return
        self._timeCounter -= 1000

        self._position[1] += 1  # Move down block

        # If the block has reach the bottom or collides with a solid tile
        if self._position[1] + self._currentBlock.getHeight() > Game.HEIGHT or \
           self.__doesBlockCollide():
            self._position[1] -= 1
            self.__addBlockToGameMap()
            self._position = [4, 0]
            self._currentBlock = self.__makeRandomBlock()

    def rotate(self):
        self._currentBlock.rotateCounterclockwise()

    def moveLeft(self):
        if self._position[0]:
            self._position[0] -= 1
            if self.__doesBlockCollide():
                self._position[0] += 1

    def moveRight(self):
        if self._position[0] + self._currentBlock.getWidth() < Game.WIDTH:
            self._position[0] += 1
            if self.__doesBlockCollide():
                self._position[0] -= 1

    def getPosition(self):
        return self._position

    def getGameMap(self):
        return self._gameMap

    def getBlock(self):
        return self._currentBlock
