# Consider adding interactivity
# do some good super() heredity
# Refactor both board and cell to make it possible to add tracker cells.


# The rules of the Game of Life:
rules = { 'birth' : (3,), 'death' : (0,1,4,5,6,7,8) }
# If a cell is dead and has exactly three alive neighbours,
# it becomes alive.
# If it is alive, and has less than 2 or more than 3
# alive neighbours, it dies.
# Change the rules of the game to have different life.


class Cell(object):
    ''' Represents the cells in the Game of Life, and contains the rules of the game.
    '''
    size = 10
    colour = { 'alive' : (0,)*3, 'dead' : (255,)*3 } 
    
    def __init__(self, x, y, alive=False):
        self.x, self.y = x, y
        self.alive = alive
        
    def __repr__(self):
        return 'Cell({},{},alive={}'.format(self.x, self.y, self.alive)
    
    def __str__(self):
        state = 'Alive' if self.alive else 'Dead'
        return state + ' cell at ' + str((self.x, self.y))
                                     
    def show(self):
        fill(*self.choose_colour())
        size = Cell.size
        rect(self.x*size, self.y*size, size, size)
    
    def choose_colour(self):
        colour_dic = self.__class__.colour
        if self.alive : return colour_dic['alive']
        else : return colour_dic['dead']
    
    def death(self) : self.alive = False
    def birth(self) : self.alive = True
    def switch(self) : self.alive = not self.alive
    def keep(self) : pass
    
    def action(self, alive_neighbours):
        ''' Returns an object method. This method can
            then simply be called at update time.
        '''
        n_alive = alive_neighbours
        if self.alive and n_alive in rules['death']:
            return self.death 
        elif not self.alive and n_alive in rules['birth']:
            return self.birth
        else :
            return self.keep
    
class RedCell(Cell):
    ''' Same as normal cell, but red'''

    colour = { 'alive' : (255,0,0), 'dead' : (255,)*3 } 

class Tracker(Cell):
    ''' This cell can be in 3 states: alive, dead and tracker.
        The tracker cell is of a different colour, and any cell,
        born in its neighbourhood will also be a tracker
    '''
    
    colour = { 'alive' : (0,)*3, 'dead' : (255,)*3,
              'tracker' : (0,0,255) }
    
    def __init__(self, x, y, alive=False, tracker=False):
        super(Tracker,self).__init__(x, y, alive)
        self.tracker = tracker
        
    def choose_colour(self):
        colour_dic = self.__class__.colour
        if self.alive : 
            if self.tracker : return colour_dic['tracker']
            else : return colour_dic['alive'] 
        else : return colour_dic['dead']
        
    def death(self) :
        self.alive = False
        self.tracker = False
    
    def switch(self) : 
        self.alive = not self.alive
        if not self.alive : 
            self.tracker = False
    
    def tracker_birth(self):
        self.birth()
        self.tracker = True
    
    def switch_tracker(self):
        self.tracker = not self.tracker
    