"""
Author: Xaen Kaifee, xkaifee@purdue.edu
Assignment: 05.4 -  Turtle Writing
Date: MM/DD/YYYY

Description:
    This program uses the turtle module to draw the letters of the words "Hammer Down" in purple.

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
    setup(600, 400)
    width(9)
    color("purple")


def draw_D():
    penup()
    goto(-250, -65)
    right(75)
    
    pendown()
    forward(100)
    right(90)
    forward(-24)
    circle(-30, -90)
    setheading(90)
    forward(50)
    circle(30, 90)
    setheading(180)
    forward(24)
    left(90)
    forward(100)

def draw_H(): 
    penup()
    goto(-250, 175)
    pendown()
    goto(-250, 0)
    goto(-250, 87.5)
    forward(50)
    goto(-200, 175)
    goto(-200, 0)
    penup()


def draw_a():
    penup()
    goto(-150, 0)
    pendown()
    circle(30, 360)
    penup()
    goto(-120,65)
    pendown()
    goto(-120,-2)
    penup()


def draw_e(): 
    penup()
    goto(87, 30)
    left(90)
    pendown()
    forward(45)
    left(90)
    circle(33, 310)
    penup()
    goto(87, 30)
    left(140)
    pendown()
    forward(15)
    

def draw_m():
    # First M
    penup()
    goto(-97, 51)
    pendown()
    goto(-97, -2)
    goto(-97, 51)
    goto(-97, 51)
    
    right(90)
    circle(15, -180)
    
    right(180)
    forward(52)
    
    right(180)
    forward(52)
    circle(-15, 180)
    
    forward(53)
    
    
    #Second M
    penup()
    goto(-15, 51)
    pendown()
    goto(-15, -2)
    goto(-15, 51)
    goto(-15, 51)
   
    right(180)
    circle(-15, 180)
    
    forward(53)
    right(180)
    
    forward(52)
    circle(-15, 180)
    
    forward(52)

  
def draw_n(): # This function draws the letter n
   penup()
   goto(-15, -106)
   pendown()
   forward(56)
   right(180)
   forward(40)
   circle(-15, 180)
   forward(40)
   


def draw_o(): # This function draws the letter o
    penup()
    goto(-177, -135)
    pendown()
    circle(30)


def draw_r(): # This function draws the letter r
    penup()
    goto(155, 65)
    left(90)
    pendown()
    forward(69)
    right(180)
    forward(45)
    right(15)
    circle(-30, 90)
    


def draw_w():
    penup()
    goto(-97, -108)
    pendown()
    forward(40)
    circle(16,180)
    forward(40)
    right(180)
    forward(40)
    circle(16,180)
    forward(40)
    right(180)
    forward(53)


def main(): 
    
    draw_H() 
    draw_a() 
    draw_m() 
    draw_e() 
    draw_r() 
    draw_D() 
    draw_o() 
    draw_w() 
    draw_n() 
    

"""Do not change anything below this line."""
if __name__ == "__main__":
    start()
    main()
    done()
