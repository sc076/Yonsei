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

def generateZero(world):
    world[0][0].changeState(ALIVE)
    world[1][0].changeState(ALIVE)
    world[2][0].changeState(ALIVE)

    world[10][11].changeState(ALIVE)
    world[10][12].changeState(ALIVE)
    world[10][13].changeState(ALIVE)

    world[11][11].changeState(ALIVE)

    world[12][11].changeState(ALIVE)
    world[12][12].changeState(ALIVE)
    world[12][13].changeState(ALIVE)

def printSep(border):
    '''Print a separator'''
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
    #print('printWorld not yet implemented')

# Get user input for size and generation:
size = int(input('Grid sidelength (default 20): ') or SIZE)
gen = int(input('Max generation: ')) + 1

# Initialize Generation 0
work = [[Cell() for x in range(size)] for y in range(size)]
generateZero(work)

# Compute:
printWorld(work)
'''
for generation in range(0, gen+1):
    printWorld(work)
    time.sleep(1)
'''
