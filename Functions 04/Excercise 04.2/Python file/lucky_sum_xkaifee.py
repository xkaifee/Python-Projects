"""
Author: Xaen, xkaifee@purdue.edu
Assignment: 04.2 -  Lucky Sum
Date: 09/22/2023

Description:
    This program will ask the user for two integers, a and b, and then
    compute the sum of all the lucky numbers between a and b, inclusive.
    A lucky number is a number that is divisible by 7.  For example, if
    a is 10 and b is 20, then the lucky numbers between a and b are 14
    and 21, so the sum is 35.

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
def lucky_sum(a, b):
   
    temp = 0

    if a > b: # swap the values of a and b if a is greater than b
        temp = a
        a = b
        b = temp
        
    sum = 0

    for num in range(a, b + 1): # range is inclusive of the last number
        if num % 7 == 0:
            sum += num
    return sum

def main():
    
    first_integer = int(input("Enter the first integer: "))
    second_integer = int(input("Enter the second integer: "))

    result = lucky_sum(first_integer, second_integer) # function call

    print(f"The sum of the lucky numbers is {result:,}.") # f-string

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
