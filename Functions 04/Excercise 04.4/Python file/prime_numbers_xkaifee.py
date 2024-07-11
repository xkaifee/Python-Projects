"""
Author: Xaen, xkaifee@purdue.edu
Assignment: 04.4 -  Prime Numbers
Date: 09/24/2023

Description:
    This program determines if a number is prime or not

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
def is_prime(num): # This function determines if a number is prime or not
    
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False

    i = 5
    
    while i * i <= num:
        
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6

    return True

def main():
    while True: # This loop keeps asking for a number until the user enters -1
        
        num = int(input("Enter a positive integer (-1 to quit): "))
        
        if num == -1: # This breaks the loop if the user enters -1
            break
        if is_prime(num): # This prints if the number is prime or not
            print(f"  {num} is prime!")
        else:
            print(f"  {num} is not prime.")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
