"""
Author: Xaen, xkaifee@purdue.edu
Assignment: 02.3 -  Roulette Colors
Date: 09/10/2023

Description:
    This program will ask the user to input a pocket number and then it will print the color of the pocket.

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


"""Write new functions below this line (starting with unit 4)."""


def main():
    """Write your mainline logic below this line (then delete this line)."""
    pocket = int(input("Please choose a pocket number: "))
    color = " "
    if pocket == 0: #if pocket is 0, then color is green
     color = "green"
     print(f"  Pocket number {pocket} is {color}.") 
    elif pocket > 0 and pocket <= 36:
        if 1 <= pocket <= 10:
            if pocket % 2 == 0:
                color = "black"
            else:
                color = "red"
        elif 11 <= pocket <= 18: #if pocket is between 11-18, then color is red
             if pocket % 2 == 0:
                color = "red"
             else:
                  color = "black"
        elif 19 <= pocket <= 28: #if pocket is between 19-28, then color is black
            if pocket % 2 == 0:
                color = "black"
            else:
                color = "red"
        elif 29 <= pocket <= 36: #if pocket is between 29-36, then color is red
            if pocket % 2 == 0:
                color = "red"
            else:
                color = "black"
        print(f"  Pocket number {pocket} is {color}.") #print the pocket number and color
    else:
        print("  Invalid Input!")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
