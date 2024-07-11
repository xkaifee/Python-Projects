"""
Author: Xaen, xkaifee@purdue.edu
Assignment: 11.1 - Dice
Date: 11/09/2023

Description:
    This program rolls a dice n times, using the Dice class.

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
import random

"""Write new functions below this line (starting with unit 4)."""
class Dice: # This class runs the dice rolling program
    def __init__(self, sides): # This function initializes the dice
        self.sides = sides

    def roll(self): # This function rolls the dice
        return random.randint(1, self.sides)

    def n_rolls(self, n): # This function rolls the dice n times
        rolls = [self.roll() for i in range(n)]
        print(f"Rolling a {self.sides} sided die {n} times: {', '.join(map(str, rolls))}")


def main():
    d6 = Dice(6)
    d10 = Dice(10)
    d20 = Dice(20)

    d6.n_rolls(10)
    d10.n_rolls(10)
    d20.n_rolls(10)



"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
