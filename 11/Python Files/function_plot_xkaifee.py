"""
Author: Xaen, xkaifee@purdue.edu
Assignment: 10.4 - Function Plot
Date: 11/07/2023

Description:
   This program plots two functions on the same graph. Using the formula for the first function, 
   the program plots the function in green. Using the formula for the second function, 
   the program plots the function in blue. The program also adds a legend, labels the axes, 
   and sets the x-axis tick labels using LaTeX notation.

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
import numpy as np
import matplotlib.pyplot as plt

"""Write new functions below this line (starting with unit 4)."""


def main():

    x = np.linspace(0, 2 * np.pi, 100)

    # Two function formulas below
    y1 = (5 * np.sin(x))**2 - 10
    y2 = (10 * np.cos(x**2)) + (x**2) - 20 


    # The line below creates the plot
    plt.figure(figsize=(8, 6))
    plt.plot(x, y1, label=r'$(5\sin{x})^2 - 10$', color='g')
    plt.plot(x, y2, label=r'$10\cos{(x^2)} + x^2 - 20$', color='b')

    # These lines set the plot title and labels
    plt.title('Function Plot (xkaifee)')
    plt.xlabel('x')
    
    # The lies below set the x-axis tick labels using LaTeX notation
    plt.xticks([np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi],
           [r'$\frac{\pi}{2}$', r'$\pi$', r'$\frac{3\pi}{2}$', r'$2\pi$'])

    plt.yticks([-20, -10, 10, 20], ['−20', '−10', '10', '20']) # Sets y-axis tick labels

    plt.legend([r'$(5\sin{x})^2 - 10$', r'$10\cos{(x^2)} + x^2 - 20$'], loc='lower right')  # Adds a legend

   # These lines below set plot spines
    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_position('zero')  # Move the x-axis to y=0
    ax.spines['left'].set_position('zero')    # Move the y-axis to x=0

    #plt.savefig('function_plot_xkaifee.pdf', format='pdf')

    plt.show()

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
