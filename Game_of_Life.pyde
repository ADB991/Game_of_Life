import random
from cells import Cell


colours = [(0,)*3,(256,)*3]
i = 0

def setup():
    size(600,600)
    global current
    current = { (x,y) : Cell(x,y) for x in range(60) for y in range(60) }
    # random initialisation
    # random.seed(1) # activate for reproducibility
    for cell in current.values():
        if random.random() < 0.5 : cell.birth()
    
    
def draw():
    frameRate(10)
    for each in current.values(): each.show()
    actions = get_actions_list(current)
    for action in actions : action()

def mouseClicked():
    cell = current[mouseCoords()]
    alive = alive_neighbours(cell, current)
    print( str(cell) + ' with {} alive neighbours'.format(alive) )
    
def mouseCoords():
    return (mouseX // 10, mouseY // 10)

def get_actions_list(board):
    ''' Given a board of cells, it returns the list
        of methods to run it in order to update it
    '''
    actions = [ determine_action(cell, board)
                for cell in board.values() ]
    return actions

def determine_action(cell, board):
    ''' Given a cell, it looks the neighbours up on the board,
        counts how many are alive and returns the
        method to be actuated.
    '''
    alive = alive_neighbours(cell, board)
    return cell.action(alive)

def alive_neighbours(cell, board):
    ''' Returns the number of alive neighbours of a given cell
    '''
    neighbours_coords = cell.neighbours() 
    neighbours_list = [ board[coords] for coords in neighbours_coords ]
    return len([ x for x in neighbours_list if x.alive])
    