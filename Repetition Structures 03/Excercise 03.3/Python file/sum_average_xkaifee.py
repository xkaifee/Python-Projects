"""
Author: Xaen, xkaifee@purdue.edu
Assignment: 03.2 -  Sum Average
Date: 09/18/2023

Description:
    This program will ask the user to enter a non-negative number. 
    It will output the sum and average of the numbers entered. 
    If the user enters a negative number, the program will stop and 
    output the sum and average of the numbers entered. 
    If the user enters no numbers, the program will output that no numbers were entered.

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
    count = 0
    sum = 0
    avg = 0
    while True: #loop until user enters negative number
        num = float(input("Enter a non-negative number (negative to quit): "))
   
        if num < 0: #break loop if negative number is entered
          break
        else:
         count += 1
         sum = float(sum + num) #add number to sum
         avg = float(sum / count) #calculate average
    
    if count > 0:
        print(f"  You entered {count} numbers.") #print count
        print(f"  Their sum is {sum:.3f} and their average is {avg:.3f}.") #print sum and average
    else:
        print("  You didn't enter any numbers.")
    

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
