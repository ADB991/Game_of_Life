import random
import math

import cells

def mouseCoords():
    return (mouseX // 10, mouseY // 10)

class Board(object):
    ''' Keeps track of cells of a game.
        Contains relevant methods and can be initialised in various ways.
    '''
    
    def __init__(self, init='blank'):
        self.x_cells, self.y_cells = width // 10, height // 10
        self.board = { (x,y) : self.new_cell(x,y) 
                      for x in range(self.x_cells)
                      for y in range(self.y_cells) }
        if init=='blank': pass
        elif init == 'random':
            # random.seed(1) # activate for reproducibility
            for cell in self.cells:
                if random.random() > 0.5 : cell.birth()
    
    def new_cell(self, x, y):
        return cells.Cell(x,y)
    
    @property
    def cells(self):
        return self.board.values()
    
    def __str__(self):
        num_cells = float(len(self.board))
        alive_cells = float(sum([cell.alive for cell in self.cells])) 
        return 'Game of Life board with {}% cells alive'.format(alive_cells/num_cells*100)
    
    def show(self):
        for each in self.cells: each.show()
    
    def update(self):
        actions = self.get_actions_list()
        for action in actions : action()
        
    def get_actions_list(self):
        ''' Return a list containing the methods
            that need to be called to update it.
        '''
        actions = [ self.determine_action(cell)
                    for cell in self.cells ]
        return actions
    
    def determine_action(self, cell):
        ''' Given a cell, it looks the neighbours up on the board,
            counts how many are alive and returns the
            method to be actuated.
        '''
        n_alive = self.alive_neighbours(cell)
        return cell.action(n_alive)
    
    def alive_neighbours(self, cell):
        ''' Returns the number of alive neighbours of a given cell
        '''
        neighbours = self.neighbours_list(cell)
        return len([ x for x in neighbours if x.alive])
    
    def neighbours_list(self,cell) :
        neighbours_coords = self.neighbours(cell) 
        return [ self.board[coords] for coords in neighbours_coords ]
    
    def neighbours(self, cell):
        ''' Calculate the neighbouring cells' coords using toroidal coords
        '''
        w, h = self.x_cells - 1, self.y_cells-1
        result =  [ ( (cell.x+i)%w, (cell.y+j)%h )
                     for i in (-1,0,1) for j in (-1,0,1)
                     if i or j ]
        return result

    def print_cell_state(self):
        cell = self.board[mouseCoords()]
        alive = self.alive_neighbours(cell)
        print( str(cell) + ' with {} alive neighbours.'.format(alive) )

class InteractiveBoard(Board):
    ''' Move the mouse to the left side
        to pause the simulation
        and to the right side to start it.
        
        Click on a cell to add or kill it.
    '''
    
    def __init__(self, init='blank'):
        self.paused = False
        super(InteractiveBoard, self).__init__(init)
                
    def pause_unpause(self):
        if self.paused and mouseCoords()[0] >= self.x_cells-1:
            self.paused = False
        if not self.paused and mouseCoords()[0] <= 0:
            self.paused = True
            
    def update(self):
        if not self.paused:
            super(InteractiveBoard,self).update()
            
    def show(self,force=True):
        if force or not self.paused:
            super(InteractiveBoard,self).show()
        
    def switch_cell(self):
        self.board[mouseCoords()].switch()


class ColourBoard(InteractiveBoard):
    ''' A class with an added colour habdling routine.
    '''
    
    def __init__(self, init='random'):
        super(ColourBoard, self).__init__(init)

    def new_cell(self,x,y):
        col = tuple((random.randint(0,255) for i in range(3) ))
        return cells.ColourCell(x,y,alive_colour=col)
    
    def determine_action(self, cell):
        ''' Performs the logic of GoL, then calls a 
            determine_colour method before returning a
            cell method which could potentially change the colour
            of the cell
        '''
        candidate = super(ColourBoard, self).determine_action(cell)
        if candidate == cell.birth:
            colour = self.determine_colour(cell)
            candidate = lambda : cell.birth(colour=colour) 
        return candidate
    
    def determine_colour(self, cell):
        ''' This method determines the colour of newborn cells,
            intentionally left blank in this class
        '''
        return None


class RedInteractiveBoard(ColourBoard):
    def new_cell(self, x, y):
        return cells.ColourCell(x,y,alive_colour=(255,0,0))
    
class TrackerBoard(ColourBoard):
    ''' Insert tracker cells by right-clicking,
        see their progeny live and die.
    '''
    
    #random.seed(1)
    
    def new_cell(self, x, y):
        return cells.Tracker(x,y)
    
    def switch_cell(self):
        cell = self.board[mouseCoords()]
        if mouseButton == RIGHT:
            if cell.alive : cell.switch_tracker()
            else : cell.tracker_birth()
        else:
            cell.switch()
        cell.show()
    
    def determine_colour(self, cell):
        if self.tracker_neighbour(cell):
            return type(cell).tracker_colour
        else: return None

    def tracker_neighbour(self, cell):
        ''' Returns true if one of the neighbouring cells
            is an alive tracker
        '''
        for cell in self.neighbours_list(cell):
            if cell.colour == type(cell).tracker_colour :
                return True
        else:
            return False