"""
Author: Your Name, login@purdue.edu
Assignment: 09.1 - Capital Quiz
Date: 10/27/2023

Description:
    This program will quiz the user on the capitals of the states. 
    It will ask the user for the capital of a state and tell them if they are correct or not.
    It will also tell the user the percentage of questions they got correct.

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
import random

"""Write new functions below this line (starting with unit 4)."""
def get_state_data():
    state_capitals = {}
    with open('state_capitals.txt', 'r') as f:
        for line in f:
            capital, state = map(str.strip, line.split(','))
            # Clean up the state name and capital
            state = state.strip()
            capital = capital.strip()
            # Store the data in the dictionary
            state_capitals[state] = capital
    return state_capitals



def main():
    state_capitals = get_state_data()
    states = list(state_capitals.keys())
    random.shuffle(states)
    correct = 0
    incorrect = 0
    answered = set()

    for state in states:  # Loop through the states without popping them from the list.
        capital = state_capitals[state]
        answer = input(f"What is the capital of {state} (enter 0 to quit)? ").strip().lower()

        if answer == '0':
            break  # Exit the loop only when the user enters '0'.
        elif answer == capital.lower():
            correct += 1
            answered.add(state)
            print("  That is correct!")
        else:
            incorrect += 1
            print(f"  That is incorrect.\n  The capital of {state} is {capital}.")

    total = correct + incorrect

    if total == 0:
        print("You didn't answer any questions.")
    else:
        percentage = correct / (correct + incorrect) * 100
        print(f"You answered {percentage:.1f}% of the questions correctly.")


        
"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
