class Block:

    def __init__(self, shape):
        """Creates a Tetris block out of a 2D array made out of characters.

        Args:
            shape: A 2D array made out of text characters.
        """
        self._shape = shape
        self._angle = 0

    def getShape(self):
        return self._shape

    def rotateClockwise(self):
        if self._angle:   # If the angle 90, 180 or 270
            self._angle = (self._angle - 90)
        else:   # If the angle is 0
            self._angle = 270 

    def rotateCounterClockwise(self):
        self._angle = (self._angle + 90) % 360

    def getRotatedShape(self):
        rotatedShape = self._shape
        for n in range(int(self._angle / 90)):
            rotatedShape = list(zip(*rotatedShape))[::-1]
        return rotatedShape
