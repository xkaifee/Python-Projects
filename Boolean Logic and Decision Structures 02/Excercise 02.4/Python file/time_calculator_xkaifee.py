"""
Author: Xaen, xkaifee@purdue.edu
Assignment: 02.4 -  Time Calculator
Date: 09/11/2023

Description:
    This program will take a number of seconds and convert it into days, hours, minutes, and seconds.

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
    seconds = int(input("Please enter a time in seconds: "))
    time = f"{seconds:,}"

    result = ""

    if seconds < 60 and seconds >= 0:  
        print(f"  {time} seconds is less than one minute.")  
    else:
        days = seconds // 86400  # Get the number of days
        seconds %= 86400  # Get the remaining seconds
        hours = seconds // 3600  # Get the number of hours
        seconds %= 3600  # Get the remaining seconds
        minutes = seconds // 60  # Get the number of minutes
        seconds %= 60  # Get the remaining seconds

        if days > 0 and hours > 0 and minutes > 0 and seconds > 0:
             result += f"{days} day(s), {hours} hour(s), {minutes} minute(s), and {seconds} second(s)"
        elif days > 0 and hours > 0 and minutes > 0:
            result += f"{days} day(s), {hours} hour(s), and {minutes} minute(s)"
        elif days > 0 and hours > 0 and seconds > 0:
            result += f"{days} day(s), {hours} hour(s), and {seconds} second(s)"
        elif days > 0 and minutes > 0 and seconds > 0:
            result += f"{days} day(s), {minutes} minute(s), and {seconds} second(s)"
        elif hours > 0 and minutes > 0 and seconds > 0:
            result += f"{hours} hour(s), {minutes} minute(s), and {seconds} second(s)"
        elif days > 0 and hours > 0:
            result += f"{days} day(s) and {hours} hour(s)"
        elif days > 0 and minutes > 0:
            result += f"{days} day(s) and {minutes} minute(s)"
        elif days > 0 and seconds > 0:
            result += f"{days} day(s) and {seconds} second(s)"
        elif hours > 0 and minutes > 0:
            result += f"{hours} hour(s) and {minutes} minute(s)"
        elif hours > 0 and seconds > 0:
            result += f"{hours} hour(s) and {seconds} second(s)"
        elif minutes > 0 and seconds > 0:
            result += f"{minutes} minute(s) and {seconds} second(s)"
        elif days > 0:
            result += f"{days} day(s)"
        elif hours > 0:
            result += f"{hours} hour(s)"
        elif minutes > 0:
            result += f"{minutes} minute(s)"
        elif seconds > 0:
            result += f"{seconds} second(s)"
            
        print(f"  {time} seconds equals {result}.")
        

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
