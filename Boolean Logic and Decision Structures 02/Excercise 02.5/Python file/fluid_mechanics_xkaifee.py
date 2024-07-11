"""
Author: Xaen, xkaifee@purdue.edu
Assignment: Fluid Mechanics -  Fluid Mechanics
Date: 09/11/2023

Description:
    This program will take a temperature, velocity, and diameter and calculate the Reynolds number.

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
    temp = float(input("Enter the temperature in °C as 5, 20, or 50: ")) # Get the temperature
    velocity = float(input("Enter the velocity of water in the pipe (m/s): ")) # Get the velocity
    diameter = float(input("Enter the pipe's diameter (m): ")) # Get the diameter

    if temp == 5:
        viscosity = 1.52 * (10 ** -6) # Calculate the viscosity
    if temp == 20:
        viscosity = 1.00 * (10 ** -6) 
    if temp == 50:
        viscosity = 5.54 * (10 ** -7) 

    reynolds_number = float((velocity * diameter) / (viscosity)) # Calculate the Reynolds number
    reynolds_number = f"{reynolds_number:.2e}"

    print(f"At {temp}°C, the Reynolds number for flow at {velocity} m/s in a {diameter} m diameter pipe is {reynolds_number}.") # Print the result
    

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
