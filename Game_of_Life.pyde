import boards


colours = [(0,)*3,(256,)*3]

def setup():
    size(600, 600)
    global current
    current = boards.RedInteractiveBoard('random')
    print(current)
    
    
def draw():
    frameRate(60)
    current.pause_unpause()
    current.show()
    current.update()

def mouseClicked():
    current.switch_cell()
    current.print_cell_state()


    