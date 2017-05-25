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


class Cell():
    ''' Represents the cells in the Game of Life, and contains the rules of the game.
    '''
    size = 10
    
    def __init__(self, x, y, alive=False):
        self.x, self.y = x, y
        self.alive = alive
        
    def __repr__(self):
        return 'Cell({},{},alive={}'.format(self.x, self.y, self.alive)
    
    def __str__(self):
        state = 'Alive' if self.alive else 'Dead'
        return state + ' cell at ' + str((self.x, self.y))
                                     
    def show(self):
        if self.alive : fill(0)
        else : fill(255)
        size = Cell.size
        rect(self.x*size, self.y*size, size, size)
    
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
    
        
        