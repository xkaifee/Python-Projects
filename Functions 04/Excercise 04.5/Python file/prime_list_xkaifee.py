"""
Author: Xaen, xkaifee@purdue.edu
Assignment: 04.5 -  Prime List
Date: 09/25/2023

Description:
    This program will take a positive integer and print out all the prime numbers up to that integer.

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

def list_primes(limit): # This function lists all the prime numbers up to a limit
    primes = [2]

    for num in range(3, limit + 1):
        if is_prime(num):
            primes.append(num)

    return primes

def main():
    limit = int(input("Enter a positive integer: ")) # This function takes in a positive integer and prints out all the prime numbers up to that integer
    prime_list = list_primes(limit)
    count = len(prime_list)

    if count > 0: # This if statement checks if there are any prime numbers in the list and prints them out
        print(f"The primes up to {limit} are: {prime_list[0]}", end="")
    
    for i in range(1, count): # This for loop prints out the rest of the prime numbers in the list
        print(f", {prime_list[i]}", end="")

    print()  

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
