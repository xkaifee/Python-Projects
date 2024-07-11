"""
Author: Xaen, xkaifee@purdue.edu
Assignment: 11.2 - Garage
Date: 11/09/2023

Description:
    This program manages two garages, using the Garage class.

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
class Garage: # The Garage class manages the garages
    def __init__(self, name, spaces, cars): # This function initializes the garages
        self.name = name
        self.spaces = spaces
        self.cars = cars

    def car_in(self): # This function adds a car to the garage
        if self.cars < self.spaces:
            self.cars += 1
            print("  Added a car to", self.name)
        else:
            print(f"  {self.name} is full. Can not add another car.")

    def car_out(self): # This function removes a car from the garage
        if self.cars > 0:
            self.cars -= 1
            print("  Removed a car from", self.name)
        else:
            print(f"  {self.name} is empty. There are no cars to remove.")

    def status(self): # This function prints the status of the garage
        empty_spaces = self.spaces - self.cars
        print(self.name + ":", empty_spaces, "out of", self.spaces, "spaces are available.")


def main(): 
    garage_a = Garage("Lot A", 10, 8) 
    garage_b = Garage("Lot B", 15, 1) 

    print("Welcome to the Garage Manager!") 
    print("------------ Menu ------------") 
    print("  0. Exit") 
    print("  1. Print current status.")
    print("  2. Add a car to A lot.")
    print("  3. Add a car to B lot.")
    print("  4. Remove a car from A lot.")
    print("  5. Remove a car from B lot.")

    while True: # This loop runs the menu
        choice = input("Please choose an option (0-5): ")
        if choice == "0": 
            print("End of the Day Garage Status:")
            garage_a.status()
            garage_b.status()
            break
        elif choice == "1": 
            print("Current Garage Status:")
            garage_a.status()
            garage_b.status()
        elif choice == "2": 
            garage_a.car_in()
        elif choice == "3": 
            garage_b.car_in()
        elif choice == "4": 
            garage_a.car_out()
        elif choice == "5": 
            garage_b.car_out()
        else:
            print("Invalid choice!")
            print("------------ Menu ------------")
            print("  0. Exit")
            print("  1. Print current status.")
            print("  2. Add a car to A lot.")
            print("  3. Add a car to B lot.")
            print("  4. Remove a car from A lot.")
            print("  5. Remove a car from B lot.")


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
