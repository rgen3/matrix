import random, string, time, os

class matrix:

    """
    current matrix array
    """
    area = []

    """
    Size of the matrix
    """
    dim = {
        'x' : 56,
        'y' : 35
    }

    """
    element index to change sign
    """
    current_index = {
        'x' : 1,
        'y' : 2
    }

    """
    Max possible letter changes in matrix
    """
    max_random = 999

    """
    Min possible letter changes in matrix
    """
    min_random = 0

    """
    Timeout for matrix scrolling
    """
    timeout = 1

    """
    Max quantity spaces in matrix raw
    """
    spaces = 40

    def __init__(self):
        for i in range(0, self.dim['x']):
            self.area.append([])
            for j in range(0, self.dim['y']):
                self.area[i].append(self.randomChoice())

    def __get__(self, instance, owner):
        pass

    """
    Run the matrix
    """
    def run(self):
        while True:
            self.draw()
            time.sleep(self.timeout)
            for i in range(1000, 1490):
                self.getRandomIndex()
                self.changeRandomIndex()
            self.moveMatrix()
            self.clear()

    """
    Move the matrix row
    """
    def moveMatrix(self):
        self.area.pop()

        list = []
        for i in range(0, self.dim['x']):
            list.append(self.randomChoice())

        self.area.insert(0, list)

    """
    Draw the matrix
    """
    def draw(self):

        for i in range(0, self.dim['x']):
            line = ''

            for j in range(0, self.dim['y']):
                line += '{0:4s}'.format(self.area[i][j])

            print line
        return True

    """
    Clear screen
    """
    def clear(self):
        os.system('clear')

    """
    Get random element in matrix to change
    """
    def getRandomIndex(self):
        self.current_index['x'] = random.randint(0, self.dim['x'] - 1)
        self.current_index['y'] = random.randint(0, self.dim['y'] - 1)

    """
    Changes random matrix element
    """
    def changeRandomIndex(self):
        x = self.current_index['x']
        y = self.current_index['y']
        self.area[x][y] = self.randomChoice()

    """
    Choose random element
    """
    def randomChoice(self):
        return random.choice(string.letters + string.digits + (" " * self.spaces))

m = matrix()
m.run()

