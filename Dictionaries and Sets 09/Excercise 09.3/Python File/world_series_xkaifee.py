"""
Author: Xaem, xkaifee@purdue.edu
Assignment: 09.2 - World Series
Date: 10/28/2023

Description:
    This program will read the data from the file WorldSeriesWinners.txt and store it in a dictionary. 
    Then It will ask the user to enter a year and it will print the team that won the World Series
    in that year and how many times they have won the World Series.

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
def load_winners_data(): # This function calls the data from the file and stores it in a dictionary
    winners = {}
    years = {}
    with open('WorldSeriesWinners.txt', 'r') as f:
        year = 1903
        for line in f:
            line = line.strip()
            if line:
                if year == 1904:
                    year += 1
                if year == 1994:
                    year += 1
                if year <= 2022:
                    if line not in winners:
                        winners[line] = 1
                    else:
                        winners[line] += 1
                    years[year] = line
                year += 1
    return winners, years

def main():# This function prints the data from the dictionary
    winners, years = load_winners_data() 
    year = int(input("Enter a year in the range 1903 -- 2022: ")) 
    if year < 1903 or year > 2022:
        print(f"  Data for the year {year} is not included in this system.")
    elif year not in years:
        print(f"  The World Series wasn't played in the year {year}.")
    else:
        team = years[year]
        times = winners[team]
        print(f"  The {team} won the World Series in {year}.")
        print(f"  They have won the World Series {times} times.")


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
