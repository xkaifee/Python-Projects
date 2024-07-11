"""
Author: Xaen Kaifee, xkaifee@purdue.edu
Assignment: 05.1 - Maze
Date: 10/01/2023

Description:
    This program will draw a path through a maze. Guiding the turtle through the maze to the exit.

Contributors:
    Name, login@purdue.edu [repeat for each]

My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [ ] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""

"""Import additional modules below this line (starting with unit 6)."""
from turtle import *

"""Write new functions below this line (starting with unit 4)."""
 

def start():
    """This function initializes the window and the turtle.
    Do not modify this function or any of the properties it sets.
    """
    setup(564, 564)
    bgpic("maze.png")
    shape("turtle")
    color("green")
    width(5)

    
def main():
 goto(0,-10) # down
 forward(35) # right
 
 goto(35,-35) # down
 forward(25) # right
 
 goto(60,-85) # down
 forward(72) # right
 
 goto(132,-107) # down
 forward(72) # right
 
 goto(203,-83) # up
 forward(23) # right
 
 goto(227,0) # up
 forward(28) # right


"""Do not change anything below this line."""
if __name__ == "__main__":
    start()
    main()
    done()
