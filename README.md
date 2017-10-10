# Game of Life

What are the simplest rules that can create life-like patterns of growth, reproduction, evolution and decay? British mathematician John Conway was looking to answer this question when he developed the rules of the [Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) in the 70s.

Each cell on the board can either be dead or alive. At each turn, the state of the cell is determined by the state of its 8 nearest neighbours. If the is dead, and exactly three of its neighbours are alive, the cell is born, otherwise it stays dead. An alive cell dies if it has less than 2 and more than 4 neighbours.

At the time he used pencil and paper to calculate the evolution of various initial boards. These deceptively simple rules give life to a whole hoard of stable patterns dynamical patterns, including a variety of “crawlers” that move about the board. He eventually managed to prove that the Game of Life is [Turing complete](https://en.wikipedia.org/wiki/Turing_completeness), which in turn means that there is no general way to tell if the board is going to eventually die or go on indefinitely.

## How to use

In the current version, the sketch is launched with a random configuration. By moving the cursor off the right side of the window, the simulation starts. One can stop the simulation by moving the cursor off the left side of the window.

One can birth or kill a cell at anytime by left-clicking it. By right clicking a cell, one adds a special tracker cell. This cell is of a different colour, and so are any of its “offsprings” cells that are born in its immediate neighbourhood. One can use these cells to visualise how the effects of adding a single cell propagate to the whole board.

## Technical notes on the implementation.

This implementation was an exercise in refactoring and pythonic coding, from a simple script that did all the basics, to having two main parent classes (boards and cells) from which more specific and capable classes inherit.

The classes are designed to make it easy to create different kind of cells or rules.

The code and comments should be intelligible enough.

Any feedback is welcome!
