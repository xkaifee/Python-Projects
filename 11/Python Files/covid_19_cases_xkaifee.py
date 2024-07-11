"""
Author: Xaen, xkaifee@purdue.edu
Assignment: 10.3 - COVID-19 Cases
Date: 11/06/2023

Description:
    This program reads data from a text file and creates a bar chart of the COVID-19 cases in Indiana.

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
   
    week_start_dates = []
    total_cases = []

    with open("indiana_covid-19_data_spring_2023.txt", "r") as file:
        lines = file.readlines()
        cumulative_cases = 0.0  
        for line in lines:
            date_start, date_end, new_cases, new_deaths = line.split()
            cumulative_cases += float(new_cases) 
            week_start_dates.append(date_start)
            total_cases.append(cumulative_cases)

    plt.figure(figsize=(10, 6))
    plt.bar(week_start_dates, total_cases, width=7, color='blue')

    plt.xlabel('Date')
    plt.ylabel('Number of Cases (in thousands)')
    plt.title('Weekly Positive COVID-19 Cases in Indiana (xkaifee)')
    plt.xticks(rotation=45)  
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    plt.savefig('covid_19_cases_login.pdf', format='pdf', bbox_inches='tight')

    plt.show()

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
