"""
Author: Xaen, xkaifee@purdue.edu
Assignment: 09.3 - Course Info
Date: 10/28/2023

Description:
    This program creats and returns a dictionary of course data.

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
def get_course_data(): # This function creates and returns a dictionary of course data.
    course_data = {
        'CS101': {'room': '1461', 'instructor': 'Django', 'time': '9:00 a.m.'},
        'CS102': {'room': '4815', 'instructor': 'Idle', 'time': '11:00 a.m.'},
        'CS103': {'room': '3634', 'instructor': 'Rich', 'time': '10:00 a.m.'},
        'NT110': {'room': '1188', 'instructor': 'Marshal', 'time': '2:00 p.m.'},
        'CM241': {'room': '2451', 'instructor': 'Pickle', 'time': '12:00 p.m.'}
    }
    return course_data

def main(): # This function prints the course data for a given course number.
    course_data = get_course_data()
    course_number = input('Enter a course number: ')
    if course_number in course_data:
        print(f"  The details for course {course_number} are:")
        print(f"    Instructor: {course_data[course_number]['instructor']}")
        print(f"          Room: {course_data[course_number]['room']}")
        print(f"          Time: {course_data[course_number]['time']}")
    else:
        print(f"  {course_number} is an invalid course number.")


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
