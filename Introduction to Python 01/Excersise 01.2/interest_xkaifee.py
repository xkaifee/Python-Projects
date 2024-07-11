"""
Author: Xaen, xkaifee@purdue.edu
Assignment: 01.2 -  Interest
Date: 09/03/2023

Description:
    This program will calculate the balance of an account after a specified number of years.

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
    print("Enter the following parameters.")
    P = float(input("  The initial deposit? ")) # P = the amount of principal originally deposited into the account
    r = float(input("  The annual interest rate in percent? ")) # r = the annual interest rate paid by the account, in percent
    t = float(input("  The number of years the account earn interest? ")) # t = the number of years the account will be left to earn interest
    n = float(input("  The number of times interest is compounded each year: ")) # n = he number of times per year that the interest is compounded
    r = r / 100
    FV = P * ( 1 + r / n ) ** ( n * t )

    formated_value = "{:,.2f}".format(FV)
    print(f"The balance of this account will be ${formated_value} after", t, "years.")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
