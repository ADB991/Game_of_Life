import random

from cells import Cell

def mouseCoords():
    return (mouseX // 10, mouseY // 10)

grid_length = 60

class Board():
    ''' Keeps track of cells of a game.
        Contains relevant methods and can be initialised in various ways.
    '''
    
    def __init__(self, init='blank'):
        self.board = { (x,y) : Cell(x,y) 
                      for x in range(60) for y in range(60) }
        if init=='blank': pass
        elif init == 'random':
            # random.seed(1) # activate for reproducibility
            for cell in self.board.values():
                if random.random() > 0.5 : cell.birth()
    
    @property
    def cells(self):
        return self.board.values()
    
    def __str__(self):
        num_cells = float(len(self.board))
        alive_cells = float(sum([cell.alive for cell in self.cells])) 
        return 'Game of Life board with {}% cells alive'.format(alive_cells/num_cells*100)
    
    def show(self):
        for each in self.board.values(): each.show()
    
    def update(self):
        actions = self.get_actions_list()
        for action in actions : action()
        
    def get_actions_list(self):
        ''' Return a list containing the methods
            that need to be called to update it.
        '''
        actions = [ self.determine_action(cell)
                    for cell in self.board.values() ]
        return actions
    
    def determine_action(self, cell):
        ''' Given a cell, it looks the neighbours up on the board,
            counts how many are alive and returns the
            method to be actuated.
        '''
        alive = self.alive_neighbours(cell)
        return cell.action(alive)
    
    def alive_neighbours(self, cell):
        ''' Returns the number of alive neighbours of a given cell
        '''
        neighbours_coords = self.neighbours(cell) 
        neighbours_list = [ self.board[coords] for coords in neighbours_coords ]
        return len([ x for x in neighbours_list if x.alive])
    
    def neighbours(self, cell):
        ''' Calculate the neighbouring cells coords using toroidal coords
        '''
        g = grid_length - 1
        result =  [ ( (cell.x+i)%g, (cell.y+j)%g )
                     for i in (-1,0,1) for j in (-1,0,1)
                     if i or j ]
        return result

    def print_cell_state(self):
        cell = self.board[mouseCoords()]
        alive = self.alive_neighbours(cell)
        print( str(cell) + ' with {} alive neighbours.'.format(alive) )
  