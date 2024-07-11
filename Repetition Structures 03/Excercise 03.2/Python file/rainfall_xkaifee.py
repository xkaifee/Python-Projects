"""
Author: Xaen, xkaifee@purdue.edu
Assignment: 03.3 - Rainfall
Date: 09/18/2023

Description:
    This program will calculate the total rainfall and average rainfall per month over a period of years.

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
    tmonths = 0
    trainfall = 0.0
    years = 0
    mon_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", \
        "Nov", "Dec"]
    years = int(input("Enter the number of years: "))
   
    if years <= 0:
        print("Invalid input; years must be greater than 0.")
    else:
        for year in range(1, years + 1): # Outer loop for years
            print(f"  For year No. {year}")
            for month in range(1, 13): # Inner loop for months
                while True:
                 rainfall = float(input(f"    Enter the rainfall for {mon_names[month - 1]}.: "))
        
                 if rainfall >= 0: # If rainfall is greater than or equal to 0, break out of loop
                    break
                 else:
                    print("    Invalid input; rainfall cannot be negative.")

                tmonths += 1
                trainfall += rainfall

    if tmonths > 0: # If total months is greater than 0, calculate average rainfall
        average_rainfall = trainfall / tmonths
        
        print(f"There are {tmonths} months.") # Print total months, total rainfall, and average rainfall
        print(f"The total rainfall was {trainfall:.2f} inches.") # Format total rainfall to 2 decimal places
        print(f"The monthly average rainfall was {average_rainfall:.2f} inches.") # Format average rainfall to 2 decimal places
        
    else:
        average_rainfall = 0.0

        


    

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
