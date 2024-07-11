"""
Author: Xaen, xkaifee@purdue.edu
Assignment: 04.3 -  Avg Grade
Date: 09/22/2023

Description:
    This program will take 5 scores from the user and calculate the average of the scores.
    It will then determine the letter grade for the average score.

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

def get_valid_score(): # This function gets a valid score from the user

    score = float(input("Enter a score: "))
        
    while score < 0.00 or score > 100.00:
        print("  Invalid Input. Please try again.")
        score = float(input("Enter a score: "))
    
    return score

def calc_average(grade_sheet): # This function calculates the average of the scores
    total = sum(grade_sheet)
    average = total / len(grade_sheet)
    return average

def determine_grade(score): # This function determines the letter grade for the score
    
    if score >= 92.00 and score <= 100.00:
        return "A"
    elif score >= 82.00 and score <= 91.99:
        return "B"
    elif score >= 73.00 and score <= 81.99:
        return "C"
    elif score >= 64.00 and score <= 72.99:
        return "D"
    else:
        return "F"
    
    
def main():
    list_size = 5
    count = 0
    grade_sheet = []

    while count < list_size:
        credit = get_valid_score()
        grade_sheet.append(credit)  # Use append to add the credit to the list
        count += 1

        grade = str(determine_grade(credit))
        print(f"  The letter grade for {credit} is {grade}.") # Print the letter grade for the credit

    average = calc_average(grade_sheet)

    
    print("")
    print("Results:")
    print(f"  The average score is {average:.2f}.")  # Print average with two decimal places

    final_grade = determine_grade(average)  # Store the final grade in a variable
    print(f"  The letter grade for {average:.2f} is {final_grade}.") # Print the letter grade for the average


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
