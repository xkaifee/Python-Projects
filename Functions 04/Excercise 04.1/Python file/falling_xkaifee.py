"""
Author: Xaen, xkaifee@purdue.edu
Assignment: 04.1 -  Falling
Date: 09/22/2023

Description:
    This program will calculate the distance an object falls in a given time.

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
def falling_dist(time): #define the function
    g = 8.87  
    distance = 0.5 * g * time**2
    return distance

def main():
    
    print(f"{'Time (s)'}  {'Distance (m)'}")
    print("----------------------   ")

    for time in range(5, 51, 5): #range(start, stop, step)
     distance = falling_dist(time) #call the function
     print(f"{time:>8} {distance:>13.1f}")  #print the results


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
