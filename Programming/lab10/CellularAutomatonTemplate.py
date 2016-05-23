from copy import deepcopy
import time

SIZE = 20 # size of the 2D cellular automaton
ALIVE = 'alive'
DEAD = 'dead'

class Cell:
    """ Class Cell used to create 'cells' for the automation
        Constructor method, state changing method and method
        returning current state of the cell
    """
    state = DEAD

    def changeState(self, s):
        self.state = s

    def getState(self):
        return self.state

def neighboursState(world, row, column):
    counter = 0
    try:
        if world[row-1][column].getState() == ALIVE: counter += 1
    except:
        pass
    try:
        if world[row][column-1].getState() == ALIVE: counter += 1
    except:
        pass
    try:
        if world[row][column+1].getState() == ALIVE: counter += 1
    except:
        pass
    try:
        if world[row+1][column].getState() == ALIVE: counter += 1
    except:
        pass
    try:
        if world[row-1][column+1].getState() == ALIVE: counter += 1
    except:
        pass
    try:
        if world[row-1][column-1].getState() == ALIVE: counter += 1
    except:
        pass
    try:
        if world[row+1][column-1].getState() == ALIVE: counter += 1
    except:
        pass
    try:
        if world[row+1][column+1].getState() == ALIVE: counter += 1
    except:
        pass
    return counter

def printSep(border):
    for ctr in range(0, border+2):
        print('-', end='')
    print('')

def printWorld(world):
    printSep(len(world))

    for row in range(len(world)):
        print('|', end = '')
        for column in range(len(world)):
            print('x', end = '') if world[row][column].getState() == ALIVE else print(' ', end = '')
        print('|', 'row', row)

    printSep(len(world))

def generateZero(world):
    world[0][1].changeState(ALIVE)
    world[1][1].changeState(ALIVE)
    world[2][1].changeState(ALIVE)

    world[10][11].changeState(ALIVE)
    world[10][12].changeState(ALIVE)
    world[10][13].changeState(ALIVE)

    world[11][11].changeState(ALIVE)

    world[12][11].changeState(ALIVE)
    world[12][12].changeState(ALIVE)
    world[12][13].changeState(ALIVE)

    printWorld(world)

def nextGeneration(world):
    prevWorld = deepcopy(world)
    for row in range(len(prevWorld)):
        for column in range(len(prevWorld)):
            neighbours = neighboursState(prevWorld, row, column)
            if prevWorld[row][column].getState() == ALIVE:
                if neighbours < 2 or neighbours > 3:
                    world[row][column].changeState(DEAD)
                elif neighbours == 2 or neighbours == 3:
                    world[row][column].changeState(ALIVE)
            elif prevWorld[row][column].getState() == DEAD and neighbours == 3:
                world[row][column].changeState(ALIVE)
    printWorld(world)

# Get user input for size and generation:
size = int(input('Grid sidelength (default 20): ') or SIZE)
gen = int(input('Max generation: '))

# Initialize Generation 0
work = [[Cell() for x in range(size)] for y in range(size)]
generateZero(work)

# Compute:
for generation in range(0, gen):
    nextGeneration(work)
    time.sleep(1)
