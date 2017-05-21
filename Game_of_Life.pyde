from boards import Board


colours = [(0,)*3,(256,)*3]
i = 0

def setup():
    size(600,600)
    global current
    current = Board('random')
    print(current)
    
    
def draw():
    frameRate( 80*(1 + mouseY / 60.))
    current.show()
    current.update()

def mouseClicked():
    current.print_cell_state()


    