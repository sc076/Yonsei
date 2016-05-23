from copy import deepcopy
import time

SIZE = 20 # size of the 2D cellular automaton

# Constant for the state of the cell
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
    """ Method checking in what state are the cells around given one and
        counting alive ones.
        As there can be risen overflow or underflow errors because of the
        borders, every check is in try-excepion block.
    """
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
    """ Prints separators for the board """

    for ctr in range(0, border+2):
        print('-', end='')
    print('')

def printWorld(world):
    """ Prints every generation of the cell automation.
        As first prints the side border and then prints X or space for
        Alive or Dead cell respectivly.
    """
    space = ' '

    # First prints the top separator of the board
    printSep(len(world))

    # Prints the side separators and the cells stored in world
    for row in range(len(world)):
        print('|', end = '')
        for column in range(len(world)):
            print('x', end = '') if world[row][column].getState() == ALIVE else print(space, end = '')
        print('|', 'row', row)

    # Prints the bottom separator of the boar
    printSep(len(world))

def generateZero(world):
    """ Function generating and printing Generation Zero.
        Following the cells placement from the Sample output file.
    """

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

    # Prints Generation Zero
    printWorld(world)

def nextGeneration(world):
    """ Generates every next generation after zero.
        Based on the conditions from the task changes
        the state of every cell.

        Works with a deepcopy of the world in order to save the old state of all
        cells and change the state in the current world.
    """

    # Deep copy of the world
    prevWorld = deepcopy(world)

    # Goes through every cell to check and change the state
    for row in range(len(prevWorld)):
        for column in range(len(prevWorld)):

            # Counts the neighbours of the current cell
            neighbours = neighboursState(prevWorld, row, column)

            # Checks the conditions for which a cell Dies or Lives
            if prevWorld[row][column].getState() == ALIVE:
                if neighbours < 2 or neighbours > 3:
                    world[row][column].changeState(DEAD)
                elif neighbours == 2 or neighbours == 3:
                    world[row][column].changeState(ALIVE)
            elif prevWorld[row][column].getState() == DEAD and neighbours == 3:
                world[row][column].changeState(ALIVE)

    # Finally prints the new generation
    printWorld(world)

# ----- MAIN --------
# Get user input for size and generation:
size = int(input('Grid sidelength (default 20): ') or SIZE)
gen = int(input('Max generation: '))

# Initialize Generation 0
work = [[Cell() for x in range(size)] for y in range(size)]
generateZero(work)

# Compute:
for generation in range(0, gen):
    nextGeneration(work)
    if generation >= 2 and generation%2 == 0:
        time.sleep(1)
