"""
Author: Xaen, xkaifee@purdue.edu
Assignment: 10.2 - Gas Prices
Date: 11/06/2023

Description:
    This program reads the contents of the 2008_Weekly_Gas_Averages.txt file and uses matplotlib to plot the data as a line graph.

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
import matplotlib.pyplot as plt

"""Write new functions below this line (starting with unit 4)."""


def main():
   
    with open("2008_Weekly_Gas_Averages.txt", "r") as file:
        data = file.read().splitlines()

    weeks = list(range(1, 53)) # This line creates the list of weeks
    gas_prices = [float(price) for price in data] # This line creates the list of gas prices

    plt.figure(figsize=(10, 6)) # This line changes the size of the graph
    plt.plot(weeks, gas_prices, color='b', linestyle='-') # This line plots the graph

    # The lines below are the titles for the axis and the graph
    plt.xlabel("Weeks (by number)")
    plt.ylabel("Average Price (dollars/gallon)")
    plt.title("2008 Weekly Gas Prices (xkaifee)")  

    # This line below create the grid lines, x axis and y axis
    plt.ylim(1.5, 4.25)
    plt.xticks(range(0, 53, 10))
    plt.xlim(1, 52)
    plt.grid(True)


    plt.savefig("gas_prices_xkaifee.pdf")

    plt.show()

    
"""Do not change any code below this line."""
if __name__ == "__main__":
    main()
