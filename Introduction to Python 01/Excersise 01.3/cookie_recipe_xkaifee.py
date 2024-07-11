"""
Author: Xaen, xkaifee@purdue.edu
Assignment: 01.3 -  Cookie Recipe
Date: 09/03/2023

Description:
    This program will ask the user how many cookies they want to make.

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
    butter_per_cookie = 1.25 / 48.0
    sugar_per_cookie = 1.5 / 48.0
    flour_per_cookie = 2.5 / 48.0


    no_of_cookies = int(input("How many cookies do you want to make? ")) #ask user for input
    formated_value = format(no_of_cookies, ',') #format the input

    butter_needed = no_of_cookies * butter_per_cookie #calculate the amount of butter needed
    sugar_needed = no_of_cookies * sugar_per_cookie #calculate the amount of sugar needed
    flour_needed = no_of_cookies * flour_per_cookie #calculate the amount of flour needed

    print("To make", formated_value, "cookies, you will need:")
    formated_value_butter = "{:10,.2f}".format(butter_needed) #format the output
    formated_value_sugar = "{:10,.2f}".format(sugar_needed) #format the output
    formated_value_flour = "{:10,.2f}".format(flour_needed) #format the output

    print(formated_value_butter, "cups of butter") 
    print(formated_value_sugar, "cups of sugar")
    print(formated_value_flour, "cups of flour")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
