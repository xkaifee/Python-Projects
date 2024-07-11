"""
Author: Xaen, xkaifee@purdue.edu
Assignment: 03.4 -  Organisms
Date: 09/18/2023

Description:
    This program will calculate the population of organisms. The user will input the starting population, the average daily increase, and the number of days to multiply. The program will then print a table of the population for each day.

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
    population = float(input("Starting population, in thousands: ")) # Get user input
    percent = float(input("Average daily increase, in percent: ")) # Get user input
    days = int(input("Number of days to multiply: "))   # Get user input

    cp = population
    day = 0

    print(f"{'Day':>3}  {'Approx. Pop':>12}") # Print table header

    while day <= days: # Print table body
        print(f"{day:>3}  {cp:>12,.3f}",)
        cp = cp * (1 + percent / 100)
        day += 1
    

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
