"""
Author: Xaen, xkaifee@purdue.edu
Assignment: 02.1 -  Leap Year
Date: 09/10/2023

Description:
    This program will ask the user for a year and then determine if the year is a leap year or not. 

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
    year = int(input("Enter a year: "))

    if (year % 100 == 0 and year % 400 == 0) or (year % 100 != 0 and year % 4 == 0): # Leap year formula
        print(f"The year {year} is a leap year.") # Leap year formula
        print(f"February of {year} has 29 days.") # Leap year has 29 days in February
    else:
        print(f"The year {year} is not a leap year.") # Not a leap year formula
        print(f"February of {year} has 28 days.") # Not a leap year has 28 days in February


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
