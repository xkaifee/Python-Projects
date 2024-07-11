"""
Author: Xaen, xkaifee@purdue.edu
Assignment: 11.3 - Rockets
Date: 11/09/2023

Description:
    This program creates a class called Rocket that has a constructor that takes 
    in the name of the rocket, the cost of the booster, upper stage, and fuel. 
    

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
class Rocket: # Create a class called Rocket
    def __init__(self, name, booster_cost, upper_stage_cost, fuel_cost):
        self.name = name
        self.booster_cost = booster_cost
        self.upper_stage_cost = upper_stage_cost
        self.fuel_cost = fuel_cost

    def cost_per_launch(self): # Create a method called cost_per_launch
        cost = self.booster_cost + self.upper_stage_cost + self.fuel_cost
        print(f"This {self.name} cost ${cost:.2f} million per launch.")


class ReusableRocket(Rocket): # Create a class called ReusableRocket that inherits from Rocket
    def __init__(self, name, booster_cost, upper_stage_cost, fuel_cost, uses):
        super().__init__(name, booster_cost, upper_stage_cost, fuel_cost)
        self.uses = uses

    def cost_per_launch(self): # Create a method called cost_per_launch
        cost = self.booster_cost / self.uses + self.upper_stage_cost + self.fuel_cost
        print(f"This {self.name} cost ${cost:.2f} million per launch.")


def main():
    atlas_v = Rocket("Atlas V", 65.4, 42.6, 0.23) # Create instances of the Rocket class
    ariane_5 = Rocket("Ariane 5", 83.5, 55.6, 0.69) # Create instances of the Rocket class
    long_march_3b = Rocket("Long March 3B", 28.5, 19.0, 2.38)
    soyuz_2 = Rocket("Soyuz 2", 20.9, 13.9, 0.24)
    falcon_9 = ReusableRocket("Falcon 9", 43.0, 18.6, 0.45, 10)

    atlas_v.cost_per_launch()    # Call the cost_per_launch method for each instance
    ariane_5.cost_per_launch()
    long_march_3b.cost_per_launch()
    soyuz_2.cost_per_launch()
    falcon_9.cost_per_launch()
    


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
