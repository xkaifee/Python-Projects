"""
Author: Xaen Kaifee, xkaifee@purdue.edu
Assignment: 05.3 - Star Pattern
Date: 10/02/2023

Description:
    This program will draw a star pattern based on the number of points the user inputs.

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
    width(7)
    side_length = 60 # Also the radius of a circle enclosed by the star.
    penup()
    goto(0, -side_length) # Start at the bottom of the star.
    pendown()


def main():
    
    points = int(input("Enter an number of points: "))
    angle =(360/points) # This is the angle the turtle will turn.
    
    fillcolor("pink") 
    begin_fill() 
    
    right((180 - 2*angle)/2)
  
    for i in range(points): # This loop draws the star.
        forward(60)
        right(-(180 - angle)) # The turtle turns -(180 - angle) degrees.
        
        forward(60)
        right(180 - 2*angle) # The turtle turns 180 - (2*angle) degrees.
             
    end_fill() # This ends the fillcolor.
       
        

"""Do not change anything below this line."""
if __name__ == '__main__':
    start()
    main()
    done()
