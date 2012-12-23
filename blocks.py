class Block:

    def __init__(self, shape, name):
        """Creates a Tetris block out of a 2D array made out of characters.

        Args:
            shape: A 2D array made out of text characters.
        """
        self._shape = shape
        self._angle = 0
        self._name = name

    def getName(self):
        return self._name

    def getShape(self):
        return self._shape

    def rotateClockwise(self):
        if self._angle:   # If the angle 90, 180 or 270
            self._angle = (self._angle - 90)
        else:   # If the angle is 0
            self._angle = 270 

    def rotateCounterclockwise(self):
        self._angle = (self._angle + 90) % 360

    def getRotatedShape(self):
        rotatedShape = self._shape
        for n in range(int(self._angle / 90)):
            rotatedShape = list(zip(*rotatedShape))[::-1]
        return rotatedShape

    def getWidth(self):
        return len(self.getRotatedShape()[0])

    def getHeight(self):
        return len(self.getRotatedShape())


class Block1(Block):
    
    def __init__(self):
        Block.__init__(self, [[0, 1, 1], [1, 1, 0]], 1)


class Block2(Block):
    
    def __init__(self):
        Block.__init__(self, [[2, 2], [2, 2]], 2)


class Block3(Block):
    
    def __init__(self):
        Block.__init__(self, [[3, 3, 0], [0, 3, 3]], 3)


class Block4(Block):
    
    def __init__(self):
        Block.__init__(self, [[4], [4], [4], [4]], 4)


class Block5(Block):
    
    def __init__(self):
        Block.__init__(self, [[5, 5], [0, 5], [0, 5]], 5)


class Block6(Block):
    
    def __init__(self):
        Block.__init__(self, [[6, 6], [6, 0], [6, 0]], 6)
