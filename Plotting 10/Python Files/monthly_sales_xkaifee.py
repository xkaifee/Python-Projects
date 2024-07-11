"""
Author: Xaen, xkaifee@purdue.edu
Assignment: 10.1 - Monthly Sales
Date: 11/06/2023

Description:
    This program asks the user for sales data for each month of the year,
    and then creates a pie chart of the data.

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
    colors = ['#4D4038', '#BAA892', '#5B6870', '#6E99B4', '#A3D6D7', '#085C11', '#849E2A', '#C3BE0B', '#E9E45B', '#6B4536', '#B46012', '#FF9B1A']

    sales_data = []

    month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    for month in month_names: # This for loop asks the user for sales data for each month.
     sales = int(input(f"Enter the sales for {month}: "))
     sales_data.append(sales)


    plt.pie(sales_data, labels=month_names, colors=colors) # This line creates the pie chart.
    plt.title('Monthly Sales') # This line adds a title to the pie chart.
    plt.savefig('monthly_sales_login.pdf') # This line saves the pie chart as a PDF file.
    plt.show() # This line displays the pie chart.

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
